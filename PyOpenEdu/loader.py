"""
    Here import we need
"""
import os
import zipfile
import pandas as pd
import json


class Loader():
    '''
        這個類別負責資料的載入資料，比如 csv 檔或者是 log 檔
        包含方法有以下:
        load_csv() : 載入 CSV 檔使用
        load_log() : 載入 log 資料
        load_all_log() : 載入資料夾裡的 log 資料，並把資料合併
        unzip() : 解壓縮 zip
    '''

    def __init__(self):
        pass

    @classmethod
    def load_csv(cls, csv_path, encoding='utf-8'):
        '''
            載入 CSV 檔使用，csv_path = csv 檔案位置
            step 1 : make '\' to '/'
            step 2 : read csv
        '''

        try:
            load_csv_data = pd.read_csv(csv_path, encoding=encoding)

        except:
            load_csv_data = pd.read_csv(csv_path, encoding=encoding, engine='python')

        finally:
            file_name = csv_path.split('/')
            print('load', file_name[-1], 'finish')

        return load_csv_data

    @classmethod
    def load_log(cls, log_path):
        '''
            載入 log 資料，log_path = log 檔案位置
            step 1 : make '\' to '/'
            step 2 : read log
        '''
        dic = {}

        with open(log_path) as file:
            count = 0
            try:
                for line in file:
                    try:
                        j = json.loads(line)
                        dic[count] = j
                    except:
                        pass
                    count += 1
            except:
                pass

        log_data = pd.DataFrame.from_dict(dic, orient='index')

        print('load_log was finish')
        return log_data

    @classmethod
    def load_all_log(cls, log_dic_path):
        '''
            載入資料夾裡的 log 資料，並把資料合併，
            log_dic_path = 讀入log_dic 的 dic 位置
            step 1 : make '\' to '/'
            step 2 : read dic log
            step 3 : concat log into DataFrame
        '''

        origin_log_data = pd.DataFrame()

        for f_path in sorted(os.listdir(log_dic_path)):
            print("Processing the " + f_path + " log")

            log_path = log_dic_path + "/" + f_path
            log_list = os.listdir(log_path)
            dic = {}

            for log in log_list:
                print(log)
                with open(log_path + "/" + log) as file:
                    count = 0
                    try:
                        for line in file:
                            try:
                                j = json.loads(line)
                                dic[count] = j
                            except:
                                pass
                            count += 1
                    except:
                        pass

                temp = pd.DataFrame.from_dict(dic, orient='index')
                dic = {}
#                temp.to_csv('C:/Users/user/Desktop/資料分析/course_app/log_data.csv', mode='a')
                origin_log_data = pd.concat([origin_log_data, temp], axis=0, ignore_index=True)

        print('load_all_log was finish')
        return origin_log_data
    
    @classmethod
    def unzip(cls, zip_path):
        '''
            解壓縮 zip ，解壓縮到壓縮檔同一層目錄
        '''

        f = zip_path.split('/')
        f = f[:-1]

        zip_dic_path = ''
        for i in f:
            zip_dic_path += i+'/'

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(zip_dic_path)

        print('unzip was finish')
        