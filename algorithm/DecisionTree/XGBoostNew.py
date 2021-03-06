from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from xgboost import plot_importance
from matplotlib import pyplot

'''
使用XGBoost提供的二分器作为模型进行预测
用 Xgboost 做一个简单的二分类问题，以下面这个数据为例，
来判断病人是否会在 5 年内患糖尿病，
这个数据前 8 列是变量，最后一列是预测值为 0 或 1
'''




file = '/Users/dzzxjl/Desktop/' + 'pima-indians-diabetes.csv'

dataset = loadtxt(file, delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]


seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


# 使用XGBoost模型，预测准确率，Accuracy: 77.95%
# xgboost 有封装好的分类器和回归器，可以直接用 XGBClassifier 建立模型
# 此处可以进行调参，不调参的话将使用默认的参数
# 2 - 76.77%, 3-77.95, 4- 75.98 5-75.20 6


'''
参数列表Parameters
max_depth : int
Maximum tree depth for base learners.

learning_rate : float #learning_rate ＝ 0.1 或更小，越小就需要多加入弱学习器
Boosting learning rate (xgb’s “eta”)
n_estimators : int
Number of boosted trees to fit.
silent : boolean
Whether to print messages while running boosting.
objective : string or callable
Specify the learning task and the corresponding learning objective or a custom objective function to be used (see note below).
booster: string
Specify which booster to use: gbtree, gblinear or dart.
nthread : int
Number of parallel threads used to run xgboost. (Deprecated, please use n_jobs)
n_jobs : int
Number of parallel threads used to run xgboost. (replaces nthread)
gamma : float
Minimum loss reduction required to make a further partition on a leaf node of the tree.
min_child_weight : int
Minimum sum of instance weight(hessian) needed in a child.
max_delta_step : int
Maximum delta step we allow each tree’s weight estimation to be.
subsample : float
Subsample ratio of the training instance.
colsample_bytree : float
Subsample ratio of columns when constructing each tree.
colsample_bylevel : float
Subsample ratio of columns for each split, in each level.
reg_alpha : float (xgb’s alpha)
L1 regularization term on weights
reg_lambda : float (xgb’s lambda)
L2 regularization term on weights
scale_pos_weight : float
Balancing of positive and negative weights.
base_score:
The initial prediction score of all instances, global bias.
seed : int
Random number seed. (Deprecated, please use random_state)
random_state : int
Random number seed. (replaces seed)
missing : float, optional
Value in the data which needs to be present as a missing value. If None, defaults to np.nan.

'''


def temp_predict(max_depth_num):
    model = XGBClassifier(learning_rate=0.1, max_depth=max_depth_num, booster='gbtree')
    # eval_set = [(X_test, y_test)]
    # model.fit(X_train, y_train, early_stopping_rounds=10, eval_metric="logloss", eval_set=eval_set, verbose=True)

    # plot_importance(model)
    # pyplot.show()

    # 使用XGBoost模型，预测准确率，Accuracy: 71.65%
    # model = tree.DecisionTreeClassifier()


    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)


    predictions = [round(value) for value in y_pred]

    accuracy = accuracy_score(y_test, predictions)
    print("树的高度为", max_depth_num, "  Accuracy: %.2f%%" % (accuracy * 100.0))

'''
树的高度为 2   Accuracy: 76.77%
树的高度为 3   Accuracy: 77.95%
树的高度为 4   Accuracy: 75.98%
树的高度为 5   Accuracy: 75.20%
树的高度为 6   Accuracy: 76.77%
树的高度为 7   Accuracy: 75.20%
树的高度为 8   Accuracy: 75.20%
'''

for i in range(2, 3):
    temp_predict(i)