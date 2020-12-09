# -*- coding:utf-8 -*-
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pylab as plt

# loaded_data = datasets.load_boston()
# data_X = loaded_data.data
# data_y = loaded_data.target
#
# model = LinearRegression()
# model.fit(data_X, data_y)
#
# print(model.predict(data_X[:4,:]))
# print(data_y[:4])

X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)
plt.scatter(X, y)
plt.show()

# print(model.coef_) #y = 0.1x + 0.3
# print(model.intercept_)
# print(model.get_params()) #可以取出之前定义的参数
# print(model.score(data_X,data_y)) #R ^2 coefficient of determination