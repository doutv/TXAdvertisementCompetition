# lgb parameters
## IO
+ zero_as_missing=True set this to true to treat all zero as missing values 我将`product_id`和`industry`里面的缺失值`\N`替换成了`0`，所以`0`在处理后的数据中视为缺失值
## Objective
+ lgb_params = {'num_leaves': 2**5-1,
              'min_data_in_leaf': 25, 
              'objective':'binary',
              'max_depth': -1,
              'learning_rate': 0.1,
              'boosting': 'gbdt',
              'feature_fraction': 0.6,
              'bagging_fraction': 0.9,
              'bagging_seed': 11,
              'metric': 'auc',
              'nthread':12,
             }
    [400]	cv_agg's auc: 0.720976 + 0.00047492
    {'num_leaves': 63, 'min_data_in_leaf': 25, 'objective': 'binary', 'max_depth': -1, 'learning_rate': 0.1, 'boosting': 'gbdt', 'feature_fraction': 0.6, 'bagging_fraction': 0.9, 'bagging_seed': 11, 'metric': 'auc', 'nthread': 12}

+ lgb_params = {'num_leaves': 2**7-1,
              'min_data_in_leaf': 25, 
              'objective':'binary',
              'max_depth': -1,
              'learning_rate': 0.1,
              'boosting': 'gbdt',
              'feature_fraction': 0.6,
              'bagging_fraction': 0.9,
              'bagging_seed': 11,
              'metric': 'auc',
              'seed':1024,
              'nthread':12,
             }
             [487]	cv_agg's auc: 0.675685 + 0.00098973