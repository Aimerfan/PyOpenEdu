import pandas as pd
import matplotlib.pyplot as plt

class DataVis():
    
    def __init__(self):
        pass
    
    def show_pie_chart(self, df, y='', figsize=(10, 10)):
        '''
            顯示圓餅圖
        '''
        
        df.plot.pie(y=y, figsize=figsize)
        
    def show_histogram(self, df):
        '''
            顯示直方圖
        '''
        
        df.plot.bar()
        
    def show_scatter_plot(self, df, x='', y='', c='DarkBlue'):
        '''
            顯示散點圖
        '''
        
        df.plot.scatter(x=x, y=y, c=c)
        
    def show_line_chart(self, df):
        '''
            顯示折線圖
        '''
        
        df.plot.line()
        
    def show_box_plot(self, df, x="", y="", figsize=(10, 10)):
        '''
            顯示盒鬚圖
        '''
        if (x=="" and y==""):
            
            df.plot.box(figsize=figsize)
        else:
            fig, ax = plt.subplots(figsize=figsize)
            df.boxplot(x, y, ax=ax, grid=False)