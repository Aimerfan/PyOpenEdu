'''
    Here we import we need
'''
import pandas as pd
import numpy as np
from filter_data import Filter_data

class DataProcess():
    '''
        對資料進行處理
    '''

    def __init__(self):
        self.filter_data_function = Filter_data()

    @classmethod
    def new_table(cls, data_table, columns):
        '''
            建立新的 data table
        '''
        data_table = data_table[columns]

        return data_table

    @classmethod
    def remove_columns(cls, data_table, columns, axis=1):
        '''
            刪除資料欄位
        '''

        data_table = data_table.drop(columns, axis=axis)

        return data_table

    @classmethod
    def rename_columns(cls, data, re_columns, inplase=True):
        '''
            重新命名欄位
        '''

        data.rename(columns=re_columns, inplace=inplase)

        return data

    @classmethod
    def get_pass(cls, row, pass_grade=0.6):
        """
            decide the grade pass or not
        """
        return row.Grade >= pass_grade

    @classmethod
    def time_split(cls, row):
        '''
            定義時間分割的方法
        '''
        return row.time.split('T')[0]

    @classmethod
    def time_process(cls, log_data):
        '''
            處理所有 log 的時間格式
        '''

        log_data['date'] = log_data.apply(cls.time_split, axis=1)
        log_data['date'] = pd.to_datetime(log_data['date'])

        return log_data

    @classmethod
    def get_student_data(cls, clean_data):
        '''
           # 將每一個學生的資料分別存放至 student_list
        '''

        student_list = []

        for user_id in sorted(set(clean_data.user_id)):
            student = clean_data[clean_data.user_id == user_id]
            student_list.append(student)

        return student_list

    @classmethod
    def filter_data(cls, origin_log_data, field, field_value=''):
        '''
            過濾欄位內容
        '''

        filter_data_done = origin_log_data[origin_log_data[field] == field_value]
        filter_data_done.reset_index(drop=True)

        return filter_data_done

    @classmethod
    def extract_event_and_context_data(cls, df, filters, _type):
        """
            定義提取資料的方法，利用定義的方法將相關的資料從 event 及 context 中取出(json 格式)。
            df：資料表
            filter：欲提取的資料列表
            _type：event 或 context 欄位
            return dic:
        """

        # 建立以欄位列表值中的欄位名稱為 key 值的 dictionary
        filtered_data = {key:[] for key in filters}

        # 從每一筆資料中提取相關的資料
        for data in df[_type]:
            for key in filters:
                try:
                    try:
                        filtered_data[key].append(data[key])
                    except:
                        filtered_data[key].append(eval(data)[key])
                except:
                    filtered_data[key].append(np.nan)

        return filtered_data

    @classmethod
    def classification_data(cls, data, _type=""):
        '''
            將資料分類
        '''

        #定義 _type 裡有幾種類型
        classification_type = list(set(data[_type]))
        print(classification_type)
        print("===============================")

        data_classification = []

        for i in classification_type:

            data_classification.append(data[data[_type] == i])

        return data_classification

    @classmethod
    def merge(cls, df1, df2, on, how="left"):
        """
            let data to a csv file
        """

        data = pd.merge(df1, df2, on=on, how=how)

        return data
