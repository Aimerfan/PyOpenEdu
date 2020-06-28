from Config import Config
from data_process import DataProcess
from loader import Loader
from export import Export

class Course_Initialization(object):
    '''
        課程初始化
    '''
    def __init__(self):
        self.config = Config()
        self.Loader = Loader()
        self.Export = Export()
        self.DataProcess = DataProcess()
        
    def set_course_data_path(self, dic_path):
        
        print("start to initialization of path.")
        self.config.set_config_path('student_grade_csv_path', dic_path, "student_grade.csv" )
        self.config.set_config_path('survey_csv_path', dic_path, "survey.csv")
        self.config.set_config_path('zip_path', dic_path, "log.zip")
        
        self.config.set_config_path('log_dic_path', dic_path, "log")
        self.config.set_config_path('log_path', dic_path, "log.csv")
        self.config.set_config_path('log_csv_path', dic_path, "log_data.csv")
        
        self.config.set_config_path('clean_data_csv_path', dic_path, "clean_data.csv")
        self.config.set_config_path('analysis_data_csv_path', dic_path, "analysis_data.csv")
        self.config.set_config_path('student_pass_csv_path', dic_path, "student_pass.csv")
        
    def initialization(self, dic_path):
        '''
            初始化課程資訊
        '''
        print("*******************************開始初始化*********************************")
        # 整理出學生是否通過成績
        try:
            student_grade_csv_path = self.config.get_student_grade_csv_path()
            grade_df = self.Loader.load_csv(student_grade_csv_path)
        except:
               print(dic_path + " has no " + self.config.get_student_grade_csv_path()) 
        
        grade_data = grade_df[['Student ID','Grade']]
        grade_data.rename(columns={'Student ID':'user_id'}, inplace=True)
        grade_data['target'] = grade_data.apply(self.DataProcess.get_pass, axis=1)
        grade_data = grade_data.drop('Grade', axis=1)
        grade_data = grade_data.sort_values("user_id").reset_index(drop=True)
        
        self.Export.export_data_to_csv(grade_data, dic_path+'/student_pass.csv')
        print("student_pass.csv processing completed.")
        
        print("****************************************************************")
        # 整理出 Log data
        try:
            
            self.Loader.unzip(self.config.get_zip_path())
            log_dic_path = self.config.get_log_dic_path()
            
            self.Export.export_log_data_from_zip(log_dic_path, dic_path)
        except:
            print(dic_path + " has no " + self.config.get_log_dic_path())
            
        print("log_data.csv processing completed.")
        
        print("****************************************************************")
        # 整理出 clean data
        try:
            log_csv_path = self.config.get_log_csv_path()
            print(log_csv_path)
            log_data = self.Loader.load_csv(log_csv_path)
        except:
            print(dic_path + " has no " + self.config.get_log_csv_path())
             
        self.Export.export_clean_data_to_csv(log_data, dic_path)  
        print("clean_data.csv processing completed.")
        
        print("****************************************************************")
        # 整理出 analysis_data
        try:
            clean_data_csv_path = self.config.get_clean_data_csv_path()
            clean_data = self.Loader.load_csv(clean_data_csv_path)
        except:
            print(dic_path + " has no " + self.config.get_clean_data_csv_path())
            
        self.Export.export_analysis_data_to_csv(clean_data, dic_path)
        print("analysis_data.csv processing completed.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       