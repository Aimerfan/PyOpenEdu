import os
import yaml
import platform


class Config():
    def __init__(self):
        '''
         pyyaml 5.1 版本後，yaml.load() 方法需要指定 Loader 參數。 
        '''
        with open('config.yaml', 'r', encoding='utf-8') as file:
            self.__config = yaml.load(file, Loader=yaml.FullLoader)
               
        self.__log_dic_path = self.__config['log_dic_path']
        self.__log_path = self.__config['log_path']
        self.__zip_path = self.__config['zip_path']
        self.__survey_csv_path = self.__config['survey_csv_path']
        self.__student_grade_csv_path = self.__config['student_grade_csv_path']
        
        self.__log_csv_path = self.__config['log_csv_path']
        self.__clean_data_csv_path = self.__config['clean_data_csv_path']
        self.__student_pass_csv_path = self.__config['student_pass_csv_path']
        self.__analysis_data_csv_path = self.__config['analysis_data_csv_path']
        
    def set_config_path(self, field, dic_path, names):
        
        # 写入 yaml 文件
        with open('config.yaml', "w") as file:
            
            self.__config[field] = dic_path + "/" + names
            yaml.dump(self.__config, file)

    def get_log_dic_path(self):
        
        return self.__log_dic_path

    def get_log_path(self):
        return self.__log_path

    def get_zip_path(self):
        return self.__zip_path
    
    def get_log_csv_path(self):
        return self.__log_csv_path

    def get_survey_csv_path(self):
        return self.__survey_csv_path

    def get_clean_data_csv_path(self):
        return self.__clean_data_csv_path

    def get_student_pass_csv_path(self):
        return self.__student_pass_csv_path

    def get_analysis_data_csv_path(self):
        return self.__analysis_data_csv_path
    
    def get_student_grade_csv_path(self):
        return self.__student_grade_csv_path