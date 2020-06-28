import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.formula.api as smf

class StatisticsAnalyzer():
    
    def __init__(self):
        pass
    
    def pearson(self, data1, data2, output=False):
        '''
            皮爾森相關分析
        '''
        pearson_coef, p_value = stats.pearsonr(data1, data2)
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
        if output == True:
            return pearson_coef, p_value
            
        
        
    def t_test(self, data1, data2):
        '''
            T-檢定
        '''
        
        statistic, pvalue = stats.ttest_ind(data1, data2)
        print("The T-tesr statistic is", statistic, " with a pvalue = ", pvalue)
        
    def ANOVA_one_way(self, data, x, y, typ=2):
        '''
        x : 自變數
        y : 應變數
        data : 資料
        ex : 比較不同 y 之間 x 的差異 
        '''
       
        condition = y + ' ~ C(' + x + ')'
      
        moore_lm = ols(condition, data=data).fit()
        table = sm.stats.anova_lm(moore_lm, typ=typ)
        
        print(table)
        
    def ANOVA_two_way(self, data, x, y, z, typ=2):
        '''
        x : 自變數
        y : 應變數
        z : 自變數
        data : 資料
        ex : 比較不同 y 之間 x 的差異 
        '''
             
        condition = y + ' ~ C(' + x + ')*C(' + z + ')'
                      
        moore_lm = ols(condition, data=data).fit()
        table = sm.stats.anova_lm(moore_lm, typ=typ)
        
        print(table)
        
    def multiple_regression(self, x, y):
        
        mod = sm.OLS(y,x)
        res = mod.fit()
        print(res.summary())
        
    def generalized_linear(self, x, y):
        
        gamma_model = sm.GLM(y, x, family=sm.families.Gamma())
        gamma_results = gamma_model.fit()
        print(gamma_results.summary())
        print(gamma_results.params)
        
    def robust_linear(self, x, y):
        
        rlm_model = sm.RLM(y, x, M=sm.robust.norms.HuberT())
        rlm_results = rlm_model.fit()
        print(rlm_results.summary())
        print(rlm_results.params)
        
    def linear_mixed_effects(self, data, groups, x, y, z):
        '''
            x : 自變數
            y : 應變數
            z : 自變數
            data : 資料
        '''
        condition = y + " ~ " + x + "*" +z
        
        md = smf.mixedlm(condition, data, groups=data[groups])
        mdf = md.fit()
        print(mdf.summary())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        