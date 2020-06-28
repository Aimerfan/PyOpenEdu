from Course_Initialization import Course_Initialization
from Visualization import DataVis
from data_process import DataProcess
from export import Export
from loader import Loader
from Analysis import Analyzer
from Student_behavior import StudentBehavior
from Predictive_analysis import Predictive_Analysis
import pandas as pd
import numpy as np


class Course(object):
    

    def __init__(self, dic_path='..'):
        
        self.Analysis = Analyzer()
        self.dic_path = dic_path
        self.DataVis = DataVis()
        course_initialization = Course_Initialization()
        course_initialization.set_course_data_path(self.dic_path)
            
    def init(self):
        course_initialization = Course_Initialization()
        course_initialization.set_course_data_path(self.dic_path)
        course_initialization.initialization(self.dic_path)
        
    def get_clean_data(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        clean_data = ld.load_csv(course_initialization.config.get_clean_data_csv_path())
        
        return clean_data
    
    def get_student_behavior(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        analysis_data = ld.load_csv(course_initialization.config.get_analysis_data_csv_path())
        
        studentbehavior = StudentBehavior()
        studentbehavior.set_data(analysis_data)
        
        return studentbehavior
    
    def get_log(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        log_data = ld.load_csv(course_initialization.config.get_log_csv_path())
        
        return log_data
    
    def get_grade(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        student_grade_data = ld.load_csv(course_initialization.config.get_student_grade_csv_path())
        
        return student_grade_data
    
    def pass_or_not(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        student_pass_data = ld.load_csv(course_initialization.config.get_student_pass_csv_path())
        
        return student_pass_data
    
    def get_survey(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        survey_data = ld.load_csv(course_initialization.config.get_survey_csv_path())
        
        return survey_data
    
    def get_student_list(self):
        
        ld = Loader()
        data_processing = DataProcess()
        course_initialization = Course_Initialization()
        
        clean_data = ld.load_csv(course_initialization.config.get_clean_data_csv_path())
        student_list = data_processing.get_student_data(clean_data)
        
        return student_list
    
    def getAnalyzer(self):
        
        analyzer = Analyzer()
        
        return analyzer
    
    def getPrediction(self):
        
        predictive_analysis = Predictive_Analysis()
        
        return predictive_analysis
        
    #------------------------------------------------------------------------------------
    
    def show_log(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            log_csv_path = course_initialization.config.get_log_csv_path()
            
            log_data = ld.load_csv(log_csv_path)
            
            print("=======================================================")
            print(log_data.to_string())

        except:
            try:
                log_data = ld.load_all_log(course_initialization.config.get_log_dic_path())
            except:
                print("There are no log_data.csv or log dic.")  
            else:
                print("=======================================================")
                print(log_data.to_string())
               
    def show_clean_data(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            
            clean_data_csv_path = course_initialization.config.get_clean_data_csv_path()
            clean_data = ld.load_csv(clean_data_csv_path)
            
            print("=======================================================")
            print(clean_data.to_string())
        except:
            print("There are no clean_data.csv.")
            
    def show_analyzed_data(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            
            analysis_data_csv_path = course_initialization.config.get_analysis_data_csv_path()
            analysis_data = ld.load_csv(analysis_data_csv_path)
            
            print("=======================================================")
            print(analysis_data.to_string())
        except:
            print("There are no analysis_data.csv.")
    
    def show_grade(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            
            student_grade_csv_path = course_initialization.config.get_student_grade_csv_path()
            student_grade = ld.load_csv(student_grade_csv_path)
            
            print("=======================================================")
            print(student_grade.to_string())
        except:
            print("There are no student_grade.csv.")
    
    def show_passORNot(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            
            student_pass_csv_path = course_initialization.config.get_student_pass_csv_path()
            student_pass = ld.load_csv(student_pass_csv_path)
            
            print("=======================================================")
            print(student_pass.to_string())
        except:
            print("There are no student_pass.csv.")
    
    def show_survey(self):
        
        ld = Loader()
        course_initialization = Course_Initialization()
        
        try:
            
            questionnaire_csv_path = course_initialization.config.get_survey_csv_path()
            questionnarie = ld.load_csv(questionnaire_csv_path)
            
            print("=======================================================")
            print(questionnarie.to_string())
        except:
            print("There are no survey.csv.")
    # -----------------------------------------------------------------------------------------
    
    def predict_by_svm(self, x_data, y_data, test_size = 0.10, kernel='linear'):
        
        analysis = Analyzer()
        
        x_train, x_test, y_train, y_test = analysis.Predictive_Analysis.split_training_and_testing(x_data, y_data, test_size=test_size)
        analysis.Predictive_Analysis.svm(x_train, x_test, y_train, y_test, kernel=kernel)
        
    def predict_by_decision_tree(self, x_data, y_data, test_size = 0.10):
        
        analysis = Analyzer()
        
        x_train, x_test, y_train, y_test = analysis.Predictive_Analysis.split_training_and_testing(x_data, y_data, test_size=test_size)
        analysis.Predictive_Analysis.decision_tree(x_train, x_test, y_train, y_test)
        
    def predict_by_random_forest(self, x_data, y_data, test_size = 0.10, tree_amount=10, max_depth=2, random_state = 0):
        
        analysis = Analyzer()
        
        x_train, x_test, y_train, y_test = analysis.Predictive_Analysis.split_training_and_testing(x_data, y_data, test_size=test_size)
        analysis.Predictive_Analysis.random_forest(x_train, x_test, y_train, y_test, tree_amount=tree_amount, max_depth=max_depth, random_state=random_state)
        
