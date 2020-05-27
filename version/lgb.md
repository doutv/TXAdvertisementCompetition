lgb_params = {'num_leaves': 2**5-1,
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