from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

class Predictive_Analysis():
    
    def __init__(self):
        pass
    
    def split_training_and_testing(self, x_data, y_data, test_size = 0.10):
        
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_size)
        
        return x_train, x_test, y_train, y_test
    
    def svm(self, x_train, x_test, y_train, y_test, kernel='linear'):
        
        # 建立 SVM 模型
        svclassifier = SVC(kernel=kernel)
       
        # 訓練模型
        svclassifier.fit(x_train, y_train)
       
        # 驗證模型
        y_pred = svclassifier.predict(x_test)
        
        print("============ SVM ============")
        print(classification_report(y_test,y_pred))
        
    def decision_tree(self, x_train, x_test, y_train, y_test):
        
        # 建立決策樹模型
        dclf = tree.DecisionTreeClassifier()
        
        # 訓練模型
        dclf = dclf.fit(x_train, y_train)
        
        # 驗證模型
        y_pred = dclf.predict(x_test)
        
        print("============ decision tree ============")
        print(classification_report(y_test,y_pred))
        
    def random_forest(self, x_train, x_test, y_train, y_test, tree_amount=10, max_depth=2, random_state = 0):
        # 建立隨機森林模型
        clf = RandomForestClassifier(n_estimators=tree_amount, max_depth=max_depth,
                                     random_state=random_state)
        
        # 訓練模型 X[:, np.newaxis]
        clf.fit(x_train, y_train)  
  
        # 驗證模型
        y_pred = clf.predict(x_test)
        
        print("============ random forest ============")
        print(classification_report(y_test,y_pred))
        
    def new_function(func):
        def wrapper(self, *var, **dic):
        
            return func(self, *var, **dic)
        return wrapper
        