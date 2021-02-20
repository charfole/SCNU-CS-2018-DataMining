## 华南师范大学2018级数据挖掘项目
本仓库是我在上学期与组员完成的数据挖掘课程项目，Project-1为平时项目，Project-2为期末项目，项目结构与具体的使用方法请参照下面的内容。



## 项目结构


SCNU-CS-2018-DataMining
├─ LICENSE		
├─ images
│    ├─ 项目一简介.png
│    ├─ 项目二简介.png
├─ Project-1											 平时项目（用四种方法进行实验）
│    ├─ LogisticRegression.ipynb						 逻辑回归 
│    ├─ MLP.ipynb										 多层感知机
│    ├─ decision_tree.ipynb								 决策树（效果最好）
│    ├─ SVM.py											 SVM	
│    ├─ data
│    │    ├─ churn_training.xlsx						 训练集
│    │    ├─ churn_test.xlsx							 测试集
│    │    ├─ churn_training_scale.csv					 归一化后的训练集（csv）
│    │    └─ churn_training_scale.xlsx					 归一化后的训练集（xlsx）
│    │    ├─ churn_test_scale.csv						 归一化后的测试集（csv）
│    │    ├─ churn_test_scale.xlsx						 归一化后的测试集（xlsx）
│    └─ information
│           ├─ 实验报告.pdf								 实验报告
│           └─ 项目要求.doc								 项目要求
├─ Project-2
│    ├─ Data exploration and preprocessing.ipynb	     数据探索与预处理
│    ├─ FinalProjectFeatureSelection.ipynb				 特征工程			
│    ├─ SupervisedRegression.ipynb						 有监督学习（回归任务）
│    └─ supervised_learning_clf.ipynb					 有监督学习（分类任务）
│    ├─ Semi_supervised_learning.ipynb					 半监督学习
│    ├─ data											
│    │    ├─ data_depression.xlsx						 原始数据集
│    │    ├─ 138rows_before.xlsx						 特征工程前
│    │    ├─ 138rows_after.xlsx							 特征工程后						
│    │    ├─ RandomForestFeatureSelectionOfDatastd.xlsx	 特征选择后的训练集
│    │    ├─ 分类数据集.xlsx							 用于分类任务的数据集
│    │    └─ 回归数据集.xlsx							 用于回归任务的数据集
│    ├─ information
│    │    ├─ 实验报告.pdf								  实验报告
│    │    ├─ 期末汇报.pptx								  期末汇报PPT
│    │    └─ 项目要求.doc								  项目要求
└─ README.md



## 项目一简介

![项目一简介](https://github.com/charfole/SCNU-CS-2018-DataMining/blob/master/images/%E9%A1%B9%E7%9B%AE%E4%B8%80%E7%AE%80%E4%BB%8B.png)



## 项目二简介

![项目二简介](https://github.com/charfole/SCNU-CS-2018-DataMining/blob/master/images/%E9%A1%B9%E7%9B%AE%E4%BA%8C%E7%AE%80%E4%BB%8B.png)



## 开发环境和使用方法

为了能够实时查看到数据，我和项目成员选取了 Jupyter Notebook 的方式在 [Colab](https://colab.research.google.com/notebooks/intro.ipynb) 上进行实验。如果你此前没有配置过相关的环境，在此极力推荐在线的 Jupyter Notebook环境（[Colab](https://colab.research.google.com/notebooks/intro.ipynb) , [Kaggle](https://www.kaggle.com/notebooks?sortBy=dateRun&tab=profile)）进行实验，以免花费太多不必要的精力在配置环境和安装依赖库中。

所有 ipynb 均可在 [Colab](https://colab.research.google.com/notebooks/intro.ipynb) 上直接运行，但不排除会因为没有 pip 安装库等原因导致一些小 bug 出现。



## 写在后面

由于项目以小组单位进行开发，所以各位成员的代码风格有一定的差异，也不排除某些方面的问题有所忽略，如发现有错误或不足，十分欢迎 issue 或 pr。希望能帮助到学习该门课程的同学。