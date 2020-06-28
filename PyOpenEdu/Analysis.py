from Descriptive_analysis import GeneralAnalyzer
from Diagnostic_analysis import StatisticsAnalyzer
from Normative_analysis import Normative_Analysis
from Predictive_analysis import Predictive_Analysis


class Analyzer():
    
    def __init__(self):
        
        self.GeneralAnalyzer = GeneralAnalyzer()
        self.StatisticsAnalyzer = StatisticsAnalyzer()
        self.Normative_Analysis = Normative_Analysis()
        self.Predictive_Analysis = Predictive_Analysis()
        
    def pearson(self, data1, data2, output=False):
        
        if output == True:
            pearson_coef, p_value = self.StatisticsAnalyzer.pearson(data1=data1, data2=data2, output=output)
            return pearson_coef, p_value
        else:
            self.StatisticsAnalyzer.pearson(data1=data1, data2=data2, output=output)
        
    def ANOVA_one_way(self, data, x, y, typ=2):
        
        self.StatisticsAnalyzer.ANOVA_one_way(data=data, x=x, y=y, typ=typ)
        
    def ANOVA_two_way(self, data, x, y, z, typ=2):
        
        self.StatisticsAnalyzer.ANOVA_two_way(data=data, x=x, y=y, z=z, typ=typ)
        
    def t_test(self, data1, data2):
        
        self.StatisticsAnalyzer.t_test(data1=data1, data2=data2)
        
    def new_function(func):
        def wrapper(self, *var, **dic):
        
            return func(self, *var, **dic)
        return wrapper