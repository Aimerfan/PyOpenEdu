# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:25:38 2020

@author: user
"""

from pyopenedu import OpenEdu
import pandas as pd
from data_process import DataProcess
from loader import Loader

openedu = OpenEdu()

python_course = openedu.import_course("../course_app")

#log_df = pd.read_csv("../course_python/log_data.csv")
#
#
#a = log_df[log_df.username == "nlh"]
#
#total_student = log_df.duplicated('username').items()
#
#for index, is_duplicated in log_df.duplicated('username').items():
#    if is_duplicated:
#        print (index)

#a = Loader.load_log("C:/Users/user/Desktop/資料分析/course_app/log/2020-04-20/course-v1_FCUx+QA+19004_27.log")

#b = Loader.load_log("C:/Users/user/Desktop/資料分析/course_app/log/2020-04-20/course-v1_FCUx+QA+19004_28.log")

#c = Loader.load_log("C:/Users/user/Desktop/資料分析/course_app/log/2020-04-20/course-v1_FCUx+QA+19004_39.log")

origin_log_data = pd.DataFrame()
origin_log_data = pd.concat([origin_log_data, a], axis=0, ignore_index=True)
origin_log_data = pd.concat([origin_log_data, b], axis=0, ignore_index=True)
origin_log_data = pd.concat([origin_log_data, c], axis=0, ignore_index=True)

a.to_csv('C:/Users/user/Desktop/資料分析/course_app/my_csv.csv', header=False)
print("a finish")
b.to_csv('C:/Users/user/Desktop/資料分析/course_app/log/2020-04-20/my_csv.csv', mode='a', header=False)
c.to_csv('C:/Users/user/Desktop/資料分析/course_app/log/2020-04-20/my_csv.csv', mode='a', header=False)