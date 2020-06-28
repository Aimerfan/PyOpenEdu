import pandas as pd
from data_process import DataProcess
from Analysis import Analyzer


class StudentBehavior(object):
    
    def __init__(self):
        
        self.data = pd.DataFrame()
        pass
    
    def set_data(self, data):
        self.data = data
        self.data.user_id = self.data.user_id.astype('str')
    
    def add_grade(self, t_grade, state=0):
        
        dp = DataProcess()
        
        self.data = dp.merge(self.data, t_grade, on="user_id")
        
        if state == 0:
            self.data.Grade.fillna(0, inplace=True)
        elif state == 1:
            self.data = self.data[self.data.Grade.notnull()]
        
    def add_survey(self, t_survey):
        
        dp = DataProcess()
        
        self.data = dp.merge(self.data, t_survey, on="user_id")
        
    def add_test(self, t_test):
        
        dp = DataProcess()
        
        self.data = dp.merge(self.data,  t_test, on="user_id")
        
    def t_login(self):
        
        t_login = self.data[["user_id","login_count"]]
        
        return t_login
        
    def t_watch(self):
        t_watch = self.data[["user_id", "video_watch_count", "video_complete_rate", "video_watch_time"]]
        
        return t_watch
    
    def t_answer(self):
        
        t_answer = self.data[["user_id", "attempts_sum", "problem_grade_sum", "complete_problem_number"]]
        
        return t_answer
    
    def t_pass_or_not(self, pass_grade=0.6, state=0):
        
        t_passOrNot = pd.DataFrame()
            
        if state == 0:
            t_passOrNot['user_id'] = self.data.user_id
            t_passOrNot['test'] = self.data.Grade >= pass_grade
            
        else:
            
            t_passOrNot = self.data[self.data.Grade >= pass_grade]
        
        return t_passOrNot
    
    def new_function(func):
        def wrapper(self, *var, **dic):
        
            return func(self, *var, **dic)
        return wrapper
    
    


        