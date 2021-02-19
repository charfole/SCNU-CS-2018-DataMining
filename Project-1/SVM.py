mport matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score,recall_score,precision_score,accuracy_score
from sklearn.metrics import confusion_matrix,plot_confusion_matrix,roc_curve,auc,plot_roc_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn import svm 

def splitData(dataSet):  
    character=[]
    label=[]
    for i in range(len(dataSet)):
        character.append([float(tk) for tk in dataSet[i][:-1]])
        label.append(dataSet[i][-1])
    return np.array(character),np.array(label)
    
# 读数据
WS1 = pd.read_excel('./data/churn_training_scale.xlsx')
data1 = np.array(WS1)
WS2 = pd.read_excel('./data/churn_test_scale.xlsx')
data2 = np.array(WS2)

X_train,y_train = splitData(data1)
X_test,y_test = splitData(data2)

#训练svm分类器  
classifier=svm.SVC(C=10,kernel='rbf',gamma=0.1)   
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

print('准确率:',accuracy_score(y_test,y_pred))
print('精准率:',precision_score(y_test,y_pred))
print('召回率:',recall_score(y_test,y_pred))
print('F1:',f1_score(y_test,y_pred))
#输出混淆矩阵
plot_confusion_matrix(classifier,X_test, y_test)


#-----------------------------------------
#网格搜素寻找最优参数
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import pandas as pd
import numpy as np

def splitData(dataSet):  
    character=[]
    label=[]
    for i in range(len(dataSet)):
        character.append([float(tk) for tk in dataSet[i][:-1]])
        label.append(dataSet[i][-1])
    return np.array(character),np.array(label)
    
# 读数据
WS1 = pd.read_excel('./data/churn_training_scale.xlsx')
data1 = np.array(WS1)
WS2 = pd.read_excel('./data/churn_test_scale.xlsx')
data2 = np.array(WS2)

X_train,y_train = splitData(data1)
X_test,y_test = splitData(data2)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [10,1,1e-1,1e-2,1e-3,1e-4],
                     'C': [0.01,0.1,1, 10, 100]},
                    {'kernel': ['linear'], 'C': [0.01,0.1,1, 10, 100, 1000,10000]}]

print()

  # 调用 GridSearchCV，将 SVC(), tuned_parameters, cv=5, 还有 scoring 传递进去，
clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
                    scoring='f1')
# 用训练集训练这个学习器 clf
clf.fit(X_train, y_train)

#----------------------------------------------
#打印观察各个得分

print("Best parameters set found on development set:")
print()

# 再调用 clf.best_params_ 就能直接得到最好的参数搭配结果
print(clf.best_params_)

print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

# 看一下具体的参数间不同数值的组合后得到的分数是多少
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
  print("%0.3f (+/-%0.03f) for %r"
   % (mean, std * 2, params))
print()

print("Detailed classification report:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
# 打印在测试集上的预测结果与真实值的分数
print(classification_report(y_true, y_pred))

print()


#----------------------------------------------
#训练使用得到的最优参数 训练svm分类器  
classifier=svm.SVC(C=100,kernel='rbf',gamma=0.01) 

classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

print('准确率:',accuracy_score(y_test,y_pred))
print('精准率:',precision_score(y_test,y_pred))
print('召回率:',recall_score(y_test,y_pred))
print('F1:',f1_score(y_test,y_pred))
plot_confusion_matrix(classifier,X_test, y_test)


#-----------------------------------------------
#输入ROC曲线
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
 
fpr, tpr, thersholds = roc_curve(y_test, y_pred)
 
for i, value in enumerate(thersholds):
    print("%f %f %f" % (fpr[i], tpr[i], value))
 
roc_auc = auc(fpr, tpr)
 
plt.plot(fpr, tpr, 'k--', label='ROC (area = {0:.2f})'.format(roc_auc), lw=2)
 
plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')  
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()
