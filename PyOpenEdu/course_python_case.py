# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:33:17 2020

@author: user
"""

from pyopenedu import OpenEdu

openedu = OpenEdu()

python_course = openedu.import_course("../course_python")
#python_course.init()

studentBehavior = python_course.get_student_behavior()

t_grade = python_course.get_grade()
t_survey = python_course.get_survey()

#更改 t_survey 和 t_grade 的欄位 StudentID 名稱為user_id
t_grade_rename = openedu.rename_columns(t_grade[["Student ID","Grade"]], {'Student ID':'user_id'})
t_grade_rename.user_id = t_grade_rename.user_id.astype('str')



# 將 t_grade 加入 studentBehavior.data
# add_grade 中 0 將空白處補 0，1 將空白整列拿除
studentBehavior.add_grade(t_grade_rename, 1)


t_test = studentBehavior.t_pass_or_not(pass_grade=0.6, state=0)
studentBehavior.add_test(t_test)


y_data = studentBehavior.data.test
# 預測時不吃 Boolean 所以轉成 0 1
y_data = y_data.astype('int')
x_data = studentBehavior.data.drop(['user_id', 'test','Grade','username'], axis=1)

prediction = python_course.getPrediction()
x_train, x_test, y_train, y_test = prediction.split_training_and_testing(x_data, y_data, test_size=0.3)

prediction.svm(x_train, x_test, y_train, y_test)

# --------------------擴充-----------------------

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from Predictive_analysis import Predictive_Analysis

@Predictive_Analysis.new_function
def knn(x_train, x_test, y_train, y_test, n_clusters=2):
    
    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    
    print(classification_report(y_test,y_pred))
    
knn(x_train, x_test, y_train, y_test, 2)

# --------------修改----------

survey_start = openedu.load_csv("C:/Users/user/Desktop/資料分析/course_python/survey_start.csv")

log = openedu.load_csv("../course_python/log_data.csv")
survey_start = openedu.rename_columns(survey_start, {'您登入 OpenEdu 的帳號 (帳號為 email 信箱)':'Email'})

from Student_behavior import StudentBehavior
from data_process import DataProcess
from Course import Course
import pandas as pd
from loader import Loader
from Course_Initialization import Course_Initialization

class new_StudentBehavior(StudentBehavior):
    
    def add_survey(self, t_grade):
        
        dp = DataProcess()
    
        new_table = pd.merge(survey_start, t_grade, on='Email')
        new_table = new_table[['Student ID', 'Email', '我的年齡', '選修這門課之前，你對於課程主題的熟悉程度為何？', 
                       '這門課程為資料科學系列入門課程，目的希望透過主題式的實作學習打好Python基礎，請問你後續還會想學習哪些主題？(複選題)']]
    
        new_table = openedu.rename_columns(new_table,{'Student ID': 'user_id'})
        new_table.user_id = new_table.user_id.astype('str')
    
        self.data = dp.merge(self.data, new_table, on="user_id", how='left')
        print('new add_survey function')

def get_student_behavior(self):
        
    ld = Loader()
    course_initialization = Course_Initialization()
        
    analysis_data = ld.load_csv(course_initialization.config.get_analysis_data_csv_path())
        
    studentbehavior = new_StudentBehavior()
    studentbehavior.set_data(analysis_data)
    print('using new function now.')
    return studentbehavior  


Course.get_student_behavior = get_student_behavior 

openedu = OpenEdu()

python_course = openedu.import_course("../course_python")

studentBehavior = python_course.get_student_behavior()    

studentBehavior.add_survey(t_grade)

result = studentBehavior.data

t_grade = openedu.rename_columns(t_grade[["Student ID","Grade", "Email"]], {'Student ID':'user_id'})
t_grade.user_id = t_grade.user_id.astype('str')
#----------------------------
#test_excel.csv
from Descriptive_analysis import GeneralAnalyzer
openedu = OpenEdu()

answer_record = openedu.load_csv('../course_python/OJ_data.csv')
answer_record = openedu.rename_columns(answer_record, {'Author':'user_id'})

student_answer_record = openedu.get_student_data(answer_record)

@GeneralAnalyzer.new_function
def anwser_record(student_answer_record):
    openedu = OpenEdu()
    student_anwser_list = []

    for i in range(len(student_answer_record)):
    
        temp = openedu.classify_data(student_answer_record[i], 'Problem')
        #print(temp)
        student_anwser_list.append(temp)
        temp=[]

    # 準備要輸出的欄位   
    answer_record_problem_type = list(set(answer_record['Problem']))
    field_list = ['user_id', 'number_of_question', 'total_number_of_anwser']

    for i in answer_record_problem_type:
        field_list.append(i)
        error = i+'_error'
        field_list.append(error)

    # user_id、題數、總作答次數、12題記錄、12題錯誤次數
    anwser_analysis = pd.DataFrame(index=range(len(student_anwser_list)),columns=field_list)

    for i in range(len(student_anwser_list)):
    
        #嘗試題數
        number_of_question = len(student_anwser_list[i])
        anwser_analysis.iloc[i].number_of_question = number_of_question
        anwser_amount = 0
    
        for j in range(len(student_anwser_list[i])):
        
            student_anwser_list[i][j].reset_index(drop=True, inplace=True)
        
            # user_id
            anwser_analysis.iloc[i].user_id = student_anwser_list[i][j].iloc[0].user_id
    
            #作答次數
            anwser_amount += len(student_anwser_list[i][j])

            #該題總作答次數
            field_name = student_anwser_list[i][j].iloc[0].Problem
            anwser_analysis.iloc[i][field_name] = len(student_anwser_list[i][j])

            #只算錯誤次數
            right = openedu.filter_data(student_anwser_list[i][j], field='Status', field_value='Accepted')
            anwser_analysis.iloc[i][field_name+'_error'] = len(student_anwser_list[i][j]) - len(right)
        
        anwser_analysis.iloc[i].total_number_of_anwser = anwser_amount
        
    return anwser_analysis
        
anwser_analysis = anwser_record(student_answer_record)   
anwser_analysis = openedu.rename_columns(anwser_analysis,{'user_id':'username'}) 

#openedu.export_to_csv(anwser_analysis,'C:/Users/user/Desktop/資料分析/course_python/anwser_analysis.csv')
anwser_data = anwser_analysis[['username', 'number_of_question', 'total_number_of_anwser']]

from Student_behavior import StudentBehavior

studentBehavior = python_course.get_student_behavior()   

@StudentBehavior.new_function
def add_anwser_data(data, anwser_data):
    dp = DataProcess()
    
    data = dp.merge(data, anwser_data, on="username")
    
    return data
studentBehavior.add_grade(t_grade)
c = studentBehavior.data

a = add_anwser_data(studentBehavior.data, anwser_data)

a = a.dropna()
Relevance = a[["video_watch_count", "video_complete_rate", "login_count", "video_watch_time", "number_of_question", "total_number_of_anwser", "Grade"]]
b = anwser_data[anwser_data.username=='AlbertWong']

e = c[c.attempts_sum!=0]
Relevance_list_name = Relevance.columns
range(len(Relevance.columns))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Relevance_matrix = pd.DataFrame(index=range(len(Relevance_list_name)), columns=Relevance_list_name)
for i in range(len(Relevance.columns)):    
    for j in range(len(Relevance.columns)):
        pa, pb = python_course.Analysis.pearson(Relevance[Relevance_list_name[i]], Relevance[Relevance_list_name[j]], output=True)
        Relevance_matrix.iloc[i][j] = pa
        
Relevance_matrix = Relevance_matrix.set_index(Relevance_list_name)     

Relevance_list_name = [x.replace("_"," ") for x in Relevance_list_name] 
Relevance_matrix.index = Relevance_list_name
Relevance_matrix.columns = Relevance_list_name 

fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(Relevance_matrix.astype(float), annot=True, linewidths=.5)


#--------------------------------------------------------------------------------------------------------------
#from export import Export
#export = Export()
#export.export_clean_data_to_csv(log_data = log, dic_path='C:/Users/user/Desktop/資料分析/course_python')
#clean_data = openedu.load_csv('C:/Users/user/Desktop/資料分析/course_python/clean_data.csv')
#export.export_analysis_data_to_csv(clean_data,'C:/Users/user/Desktop/資料分析/course_python')

data = pd.read_excel('C:/Users/user/Desktop/資料分析/course_python/OJ_log.xlsx', sheet_name = None)
xlsx = pd.ExcelFile('C:/Users/user/Desktop/資料分析/course_python/OJ_log.xlsx')
xlsx.sheet_names
Question_list = data.get('For...in加法') 

from collections import OrderedDict
def OrderedDict_to_dict(arg):
    if isinstance(arg, (tuple, list)):
        return [OrderedDict_to_dict(item) for item in arg]

    if isinstance(arg, OrderedDict):
        arg = dict(arg)

    if isinstance(arg, dict):
        for key, value in arg.items():
            arg[key] = OrderedDict_to_dict(value)

    return arg

dict_result = OrderedDict_to_dict(data)
dict_result = list(dict_result)
anwserList = []
anwserList = ['Question_Type', 'Right_Rate', 'Anwser_Total', 'Anwser_People_Total', 'Accepted', 'Compile_Error', 'Wrong_Answer', 'Runtime_Error']

df_Question = pd.DataFrame(index=range(len(dict_result)-3), columns = anwserList)

count = 0
for i in range(len(dict_result)):

    Question_name = dict_result[i]

    if Question_name != 'EX列表':
        if Question_name != 'status表':
            if Question_name != '帳號列表':

                Question_data = data.get(dict_result[i])
                Question_Type = Question_data.iloc[0].Problem
                Anwser_Total = len(Question_data)
                Anwser_People_Total = len(set(Question_data.Author))
                Accepted = len(Question_data[Question_data.Status == 'Accepted'])
                Compile_Error = len(Question_data[Question_data.Status == 'Compile Error'])
                Wrong_Answer = len(Question_data[Question_data.Status == 'Wrong Answer'])
                Runtime_Error = len(Question_data[Question_data.Status == 'Runtime Error'])

                if Anwser_Total==0:
                    Right_Rate = 0
                else:
                    Right_Rate = Accepted / Anwser_Total

                df_Question.iloc[count].Question_Type = Question_Type
                df_Question.iloc[count].Anwser_Total = Anwser_Total
                df_Question.iloc[count].Anwser_People_Total = Anwser_People_Total
                df_Question.iloc[count].Accepted = Accepted
                df_Question.iloc[count].Compile_Error = Compile_Error
                df_Question.iloc[count].Wrong_Answer = Wrong_Answer
                df_Question.iloc[count].Runtime_Error = Runtime_Error
                df_Question.iloc[count].Right_Rate =  Right_Rate

                count += 1

#new_oj = pd.DataFrame()
#
#for i in range(len(dict_result)):
#
#    Question_name = dict_result[i]
#
#    if Question_name != 'EX列表':
#        if Question_name != 'status表':
#            if Question_name != '帳號列表':
#                Question_data = data.get(dict_result[i])
#                new_oj = pd.concat([new_oj, Question_data])
#                
#openedu.export_to_csv(new_oj,'../course_python/OJ_data.csv')
                