# -*- coding:utf-8 -*-
from sklearn.datasets import load_iris # iris数据集
from sklearn.model_selection import train_test_split # 分割数据模块
from sklearn.neighbors import KNeighborsClassifier # K最近邻(kNN，k-NearestNeighbor)分类算法

#加载iris数据集
iris = load_iris()
X = iris.data
y = iris.target

#分割数据并
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

#建立模型
knn = KNeighborsClassifier(n_neighbors=5)

#训练模型
knn.fit(X_train, y_train)

#将准确率打印出
# print(knn.score(X_test, y_test))

from sklearn.model_selection import cross_val_score # K折交叉验证模块
# scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
# print(scores)
# print(scores.mean())

import matplotlib.pyplot as plt #可视化模块
#建立测试参数集
k_range = range(1, 31)
k_scores = []
#藉由迭代的方式来计算不同参数对模型的影响，并返回交叉验证后的平均准确率
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    loss = -cross_val_score(knn, X, y, cv=10, scoring='neg_mean_squared_error')
    # scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') #for classification
    # k_scores.append(scores.mean())
    k_scores.append(loss.mean())

#可视化数据
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()