from sklearn.model_selection import train_test_split
import lightgbm as lgb
import pandas as pd
import numpy as np
train_ad = pd.read_csv("../train_preliminary/ad.csv")
train_click_log = pd.read_csv("../train_preliminary/click_log.csv")
train_user = pd.read_csv("../train_preliminary/user.csv")
train_merged = pd.merge(train_ad, train_click_log, on='creative_id')
train_merged = pd.merge(train_merged, train_user, on='user_id')
train_merged["product_id"].replace({"\\N": "0"}, inplace=True)
train_merged["industry"].replace({"\\N": "0"}, inplace=True)
train_merged = train_merged.astype(int)
display(train_merged)
del train_ad, train_click_log, train_user
train_merged.to_csv("train_merged.csv")
# %%capture cap --no-stderr
features = ["creative_id", "ad_id", "product_id", "product_category", "advertiser_id", "industry", "time", "click_times"]
df = train_merged.drop(columns=["age", "user_id"])
# convert {1,2} to binary value {0,1}
df["gender"] -= 1
# split train data into 2 parts (cross validation)
train = df.sample(frac=0.8)  # random state is a seed value
test = df.drop(train.index)
y_train = train.pop("gender")
X_train = train
y_test = test.pop("gender")
X_test = test
# display(X_train,y_train)
# display(X_test,y_test)
train_data = lgb.Dataset(X_train, y_train)
train_data.save_binary('gender.bin')

# !pip install lightgbm
features = ["creative_id", "ad_id", "product_id", "product_category", "advertiser_id", "industry", "time", "click_times"]
df = train_merged.drop(columns=["gender", "user_id"])
# split train data into 2 parts (cross validation)
train = df.sample(frac=0.8)  # random state is a seed value
test = df.drop(train.index)
y_train = train.pop("age")
X_train = train
y_test = test.pop("age")
X_test = test
# display(X_train,y_train)
# display(X_test,y_test)
train_data.save_binary('age.bin')

# %%capture cap --no-stderr
# %reset - f
train_data = lgb.Dataset('gender.bin')
lgb_params = {'num_leaves': 2**5-1,
              'min_data_in_leaf': 25,
              'objective': 'binary',
              'max_depth': -1,
              'learning_rate': 0.1,
              'boosting': 'gbdt',
              'feature_fraction': 0.6,
              'bagging_fraction': 0.9,
              'bagging_seed': 11,
              'metric': 'auc',
              #               'seed':1024,
              'nthread': 12,
              }
# with open('lgb.txt', 'a') as f:
#     f.write(str(lgb_params))
print("start training")
cv_results = lgb.cv(
    lgb_params, train_data, num_boost_round=1000, nfold=5, stratified=False, shuffle=True,
    early_stopping_rounds=50, verbose_eval=1, show_stdv=True, seed=0)

# %reset - f
train_data = lgb.Dataset('age.bin')
params = {'num_leaves': 2**6-1,
          'min_data_in_leaf': 25,
          'objective': 'regression_l2',
          'max_depth': -1,
          'learning_rate': 0.1,
          'min_child_samples': 20,
          'boosting': 'gbdt',
          'feature_fraction': 0.6,
          'bagging_fraction': 0.9,
          'bagging_seed': 11,
          'metric': 'mae',
          'seed': 1024,
          'lambda_l1': 0.2,
          'nthread': 12,
          }
print("start training")
cv_results = lgb.cv(
    params, train_data, num_boost_round=1000, nfold=5, stratified=False, shuffle=True,
    early_stopping_rounds=50, verbose_eval=1, show_stdv=True, seed=0)
print('best num_boost_round:', len(cv_results['mae-mean']))
print('best cv score:', cv_results['mae-mean'])
