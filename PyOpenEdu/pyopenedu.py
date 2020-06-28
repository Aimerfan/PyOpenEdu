"""
    DataProcess for processing data
"""
from data_process import DataProcess
from loader import Loader
from export import Export
from Course import Course
from Analysis import Analyzer

class OpenEdu():
    """
        software start
    """
    def __init__(self):
        self.analyzer = Analyzer()

    @classmethod
    def import_course(cls, dic_path):
        """
            new a course from openedu
        """

        course = Course(dic_path)

        return course

    # Loader ------------------------------------------------------------

    @classmethod
    def load_csv(cls, path):
        """
            get data from csv files
        """

        loader = Loader()

        csv_data = loader.load_csv(path)

        return csv_data

    @classmethod
    def load_all_log(cls, log_dic_path):
        """
            get all of log files data
        """

        loader = Loader()

        log_data = loader.load_all_log(log_dic_path)

        return log_data

    @classmethod
    def unzip(cls, path):
        """
            unzip the zip file
        """

        loader = Loader()

        loader.unzip(path)

    @classmethod
    def load_log(cls, path):
        """
            get a log data from log file
        """

        loader = Loader()

        log_data = loader.load_log(path)

        return log_data

    # Data_Processing ------------------------------------------------------------

    @classmethod
    def new_table(cls, data_table, columns):
        """
            to get a new  table from another table
        """

        data_process = DataProcess()

        data_table = data_process.new_table(data_table, columns)

        return data_table

    @classmethod
    def remove_columns(cls, data_table, columns, axis=1):
        """
            remove a columns from table
        """

        data_process = DataProcess()

        data_table = data_process.remove_columns(data_table=data_table, columns=columns, axis=axis)

        return data_table

    @classmethod
    def rename_columns(cls, data, re_columns, inplase=True):
        """
            rename the colums name
        """

        data_process = DataProcess()

        data = data_process.rename_columns(data=data, re_columns=re_columns, inplase=inplase)

        return data

    @classmethod
    def filter_data(cls, origin_log_data, field, field_value=''):
        """
            filter value for a columns
        """

        data_process = DataProcess()

        filter_data_done = data_process.filter_data(origin_log_data=origin_log_data,
                                                    field=field, field_value=field_value)

        return filter_data_done

    @classmethod
    def classify_data(cls, data, _type=""):
        """
            classify the  data
        """

        data_process = DataProcess()

        data = data_process.classification_data(data=data, _type=_type)

        return data

    @classmethod
    def get_student_data(cls, clean_data):
        """
            let data classify by student
        """

        data_process = DataProcess()

        student_list = data_process.get_student_data(clean_data)

        return student_list

    @classmethod
    def merge(cls, df1, df2, on, how="left"):
        """
            make two table merge to one table
        """

        data_process = DataProcess()

        data = data_process.merge(df1, df2, on=on, how=how)

        return data

    # Export ------------------------------------------------------------

    @classmethod
    def export_to_csv(cls, export_data, file_name_path):
        """
            let data to a csv file
        """

        export = Export()

        export.export_data_to_csv(export_data, file_name_path)
