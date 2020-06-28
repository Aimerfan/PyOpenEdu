"""
    Here import we need
"""
import pandas as pd
import numpy as np
from loader import Loader
from data_process import DataProcess
from Descriptive_analysis import GeneralAnalyzer


class Export():
    """
        let data to output.
    """

    def __init__(self):

        self.loader = Loader()
        self.data_process = DataProcess()

    def export_data_to_csv(self, export_data, file_name_path):
        """
            make data to csv.
        """

        export_data.to_csv(file_name_path, index=False)

    def export_log_data_from_zip(self, log_dic_path, dic_path):
        """
            get all the log data from zip.
        """

        log_data = self.loader.load_all_log(log_dic_path)
        log_data.to_csv(dic_path + '/log_data.csv')

    def export_clean_data_to_csv(self, log_data, dic_path):
        """
            clean_data was log data that only we need and let it to csv.
        """

        # 過濾資料，只留下所需的資料欄位
        browser_mask = log_data.event_source == "browser"
        server_mask = (log_data.event_source == "server") & (log_data.event_type == "problem_check")
        log_data = log_data[browser_mask | server_mask]
        # 將 index 重置
        log_data = log_data.reset_index(drop=True)

        log_data = self.data_process.time_process(log_data)

        context_filter = ["user_id", "course_id"]

        context_data = self.data_process.extract_event_and_context_data(log_data,
                                                                       context_filter, "context")
        context = pd.DataFrame(context_data)

        event_filter = ["code", "currentTime", "new_speed", "old_speed", "old_time", "new_time",
                        "problem_id", "attempts", "grade", "max_grade", "success"]

        event_data = self.data_process.extract_event_and_context_data(log_data,
                                                                     event_filter, "event")
        event = pd.DataFrame(event_data)

        clean_data = pd.DataFrame({"username":log_data.username,
                                   "event_source":log_data.event_source,
                                   "event_type":log_data.event_type,
                                   "session":log_data.session,
                                   "date":log_data.date})

        clean_data = pd.concat([clean_data, context], axis=1)
        clean_data = pd.concat([clean_data, event], axis=1)
        # 將資料欄位重新排序
        try:
            clean_data = clean_data[["user_id", "course_id", 'username', "event_source", "event_type",
                                     "code", "session", "date", "currentTime", "old_time",
                                     "new_time", "old_speed", "new_speed", "problem_id",
                                     "attempts", "grade", "max_grade", "success"]]
        except:
            clean_data = clean_data[["user_id", "course_id", 'username', "event_source", "event_type",
                                     "code", "date", "currentTime", "old_time", "new_time",
                                     "old_speed", "new_speed", "problem_id", "attempts",
                                     "grade", "max_grade", "success"]]

        # 輸出前處理後的資料
        self.export_data_to_csv(clean_data, dic_path +'/clean_data.csv')

    def export_analysis_data_to_csv(self, clean_data, dic_path):
        """
            analysis was get by clean_data then to csv.
        """

        # 將 clean_data 轉成針對學生的資料表
        student_list = self.data_process.get_student_data(clean_data)
        general_analyzer = GeneralAnalyzer()

        #透過 clean_data 去獲取影片總數
        video_total_numbers = general_analyzer.get_video_total_count(clean_data)

        dic = {}
        index = 0

        for student in student_list:

            # 計算觀看影片數量
            video_watch_count = len(set(student[student.code.notnull() == True].code))
            # 計算影片完看率
            video_complete_rate = video_watch_count/video_total_numbers
            # 計算登入天數
            login_count = len(set(student.date))

            # 計算影片觀看總時間
            video_watch_time = 0
            # 利用遮罩挑選 event_type 為 play_video 以及 pause_video 的資料
            play_mask = student.event_type == "play_video"
            pause_mask = student.event_type == "pause_video"
            temp_df = student[play_mask | pause_mask]
            temp_df.reset_index(drop=True)

            count = 0
            for event_type in temp_df.event_type:
                if event_type == "play_video":
                    try:
                        if temp_df.iloc[count+1].event_type == "pause_video":
                            # 暫停的 currentTime 減去 上一次撥放的 currentTime 即為觀看時間
                            video_watch_time += (temp_df.iloc[count+1].currentTime -
                                                 temp_df.iloc[count].currentTime)
                    except:
                        pass
                count += 1

            if np.isnan(video_watch_time):
                video_watch_time = 0

            # 利用遮罩挑選 success 為 correct 的資料
            correct_df = student[student.success == "correct"]
            # 重新設定 index
            correct_df = correct_df.reset_index(drop=True)

            # 宣告作答次數、總分的變數以及完成題數的變數
            success_count, attempts_sum, problem_grade_sum = 0, 0, 0
            # 當 success 為 correct 時，將作答次數及分數加總，並且完成題數 +1
            for success in correct_df.success:
                if success == "correct":
                    attempts_sum += correct_df.iloc[success_count].attempts
                    problem_grade_sum += correct_df.iloc[success_count].grade
                    success_count += 1

            # 將計算完的資料合併為 dict
            dic[index] = {"user_id": student.iloc[0].user_id,
                           "username":student.iloc[0].username,
                           "video_watch_count": video_watch_count,
                           "video_complete_rate": video_complete_rate,
                           "login_count": login_count,
                           "video_watch_time": video_watch_time,
                           "attempts_sum": attempts_sum,
                           "problem_grade_sum": problem_grade_sum,
                           "complete_problem_number": success_count}
            index += 1

        analysis_data = pd.DataFrame.from_dict(dic, orient='index')
        analysis_data.to_csv(dic_path + "/analysis_data.csv", index=False)
