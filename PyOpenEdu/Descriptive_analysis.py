from data_process import DataProcess
from loader import Loader

class GeneralAnalyzer():
    
    def __init__(self):
        
        pass
    
    def number_of_students(self, student_data):
        '''
            How many students in course.
        '''
        
        num_student = len(set(student_data['Student ID']))
        
        return num_student
       
    def get_pass_rate(self, student_data, pass_grade=0.6):
        '''
            Student in course get pass rate.
        '''
        
        num_student = len(student_data)
        pass_student_amount = len(student_data[student_data.Grade >= pass_grade])
 
        if num_student != 0:
            
            pass_rate = pass_student_amount / num_student
            
            return pass_rate
            
        else:
            return 0
        
    def caculate_login_days(self,student_list, student):
        '''
            計算學生登入天數
        '''
    
        login_count = len(set(student_list[student].date))
        
        return login_count
    
    def get_video_total_count(self, clean_data):
        '''
            計算影片總數
        '''
        
        clean_code_mask = clean_data.code.notnull() == True
        video_total_numbers = len(set(clean_data[clean_code_mask].code))
         
        return video_total_numbers
    
    def get_student_video_watch_count(self, student_list, student):
        '''
            計算觀看影片數量
        '''
        
        code_mask = student_list[student].code.notnull() == True
        video_watch_count = len(set(student_list[student][code_mask].code))
        
        return video_watch_count
    
    def get_student_video_completion_rate(self, video_total_numbers, video_watch_count):
        '''
            計算學生影片完看率
            需求: 計算影片總數, 學生觀看影片數量
        '''
        
        if video_total_numbers == 0:
            return 0
        else:
            video_complete_rate = video_watch_count / video_total_numbers
            return video_complete_rate
        
    def get_student_video_watch_total_time(self, student_list, student):
        '''
            計算學生影片觀看總時間
            需求: student -> 哪個學生
                  student_list -> 所有學生資料(按照學生劃分好)
        '''
        
        # 利用遮罩過濾 event_type 為 play_video 以及 pause_video 的資料
        play_mask = student_list[student].event_type == "play_video"
        pause_mask = student_list[student].event_type == "pause_video"
        temp_df = student_list[student][play_mask | pause_mask]
        
        # 定義影片總時間
        video_watch_time = 0
        
        count = 0
        for event_type in temp_df.event_type:
            """
            將 puase_video 的 currentTime 減去上一次 play_video 的 currentTime 即為觀看時間，並加總至 video_watch_time
            """
            if event_type == "play_video":
                try:
                    if temp_df.iloc[count+1].event_type == "pause_video":
                        # 暫停的 currentTime 減去 上一次撥放的 currentTime 即為觀看時間
                        video_watch_time += (temp_df.iloc[count+1].currentTime - temp_df.iloc[count].currentTime)
                except:
                    pass
            count += 1
        
        return video_watch_time
    
    def get_video_watch_total_time(self, clean_data, video_id):
        
        # 利用遮罩過濾 event_type 為 play_video 以及 pause_video 的資料
        clean_data =  clean_data[clean_data.code == video_id]
        play_mask = clean_data.event_type == "play_video"
        pause_mask = clean_data.event_type  == "pause_video"
        temp_df = clean_data[play_mask | pause_mask]
        
        # 定義影片總時間
        video_watch_time = 0
        
        count = 0
        for event_type in temp_df.event_type:
            """
            將 puase_video 的 currentTime 減去上一次 play_video 的 currentTime 即為觀看時間，並加總至 video_watch_time
            """
            if event_type == "play_video":
                try:
                    if temp_df.iloc[count+1].event_type == "pause_video":
                        # 暫停的 currentTime 減去 上一次撥放的 currentTime 即為觀看時間
                        video_watch_time += (temp_df.iloc[count+1].currentTime - temp_df.iloc[count].currentTime)
                except:
                    pass
            count += 1
        
        return video_watch_time
        
    def get_student_response_data(self, student_list, student):
        '''
            計算學生影片觀看總時間
            需求: student -> 哪個學生
                  student_list -> 所有學生資料(按照學生劃分好)
            回傳: 總作答次數,總分, 完成題數
        '''
        
        # 利用遮罩挑選 success 為 correct 的資料
        correct_df = student_list[student][student_list[student].success == "correct"]
        
        # 重新設定 index
        correct_df = correct_df.reset_index(drop=True)

        # 宣告作答次數以及總分的變數
        attempts_sum = 0
        problem_grade_sum = 0

        # 宣告完成題數的變數
        success_count = 0
        
        # 當 success 為 correct 時，將作答次數及分數加總，並且完成題數 +1
        for success in correct_df.success:
            attempts_sum += correct_df.iloc[success_count].attempts
            problem_grade_sum += correct_df.iloc[success_count].grade
            success_count += 1
            
        return attempts_sum, problem_grade_sum, success_count
    
    def new_function(func):
        def wrapper(self, *var, **dic):
        
            return func(self, *var, **dic)
        return wrapper


        
        
        
        
    
    
