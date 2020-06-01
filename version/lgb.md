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

## age
+ train_data = lgb.Dataset('CountVectorizer_train_age.bin')
    lgb_params = {'num_leaves': 2**6-1,
                  'min_data_in_leaf': 25, 
                  'objective':'multiclass',
                  'num_class':10,
                  'max_depth': -1,
                  'learning_rate': 0.1,
                  'boosting': 'gbdt',
                  'feature_fraction': 0.6,
                  'bagging_fraction': 0.9,
                  'bagging_seed': 11,
                  'metric': 'multi_error',
                  'seed':1024,
                  'nthread':12,
                 }
    [10]	cv_agg's multi_error: 0.773837 + 0.00108892
    [20]	cv_agg's multi_error: 0.772143 + 0.00108821
    [30]	cv_agg's multi_error: 0.770558 + 0.00103075
    [40]	cv_agg's multi_error: 0.769079 + 0.00107046
    [50]	cv_agg's multi_error: 0.768085 + 0.00111039
    [60]	cv_agg's multi_error: 0.767147 + 0.00110585
    [70]	cv_agg's multi_error: 0.766379 + 0.00116012
    [80]	cv_agg's multi_error: 0.765656 + 0.00116009
    [90]	cv_agg's multi_error: 0.765029 + 0.00118739
    [100]	cv_agg's multi_error: 0.764253 + 0.00120462
    [110]	cv_agg's multi_error: 0.763796 + 0.00117341
    [120]	cv_agg's multi_error: 0.763329 + 0.00120664
    [130]	cv_agg's multi_error: 0.76284 + 0.0011866
    [140]	cv_agg's multi_error: 0.762506 + 0.00115682
    [150]	cv_agg's multi_error: 0.762025 + 0.00111838
    [160]	cv_agg's multi_error: 0.761746 + 0.00107285
    [170]	cv_agg's multi_error: 0.761478 + 0.000996448
    [180]	cv_agg's multi_error: 0.761132 + 0.00103269
    [190]	cv_agg's multi_error: 0.760799 + 0.000942717
    [200]	cv_agg's multi_error: 0.760576 + 0.000930784
    [210]	cv_agg's multi_error: 0.76024 + 0.0010012
    [220]	cv_agg's multi_error: 0.76005 + 0.000983745
    [230]	cv_agg's multi_error: 0.759897 + 0.00102586
    [240]	cv_agg's multi_error: 0.759728 + 0.000906567
    [250]	cv_agg's multi_error: 0.759594 + 0.000965349
    [260]	cv_agg's multi_error: 0.759431 + 0.00100665
    [270]	cv_agg's multi_error: 0.759253 + 0.000999379
    [280]	cv_agg's multi_error: 0.759036 + 0.00101404
    [290]	cv_agg's multi_error: 0.758921 + 0.000939166
    [300]	cv_agg's multi_error: 0.758868 + 0.00101623
    [310]	cv_agg's multi_error: 0.758743 + 0.00104266
    [320]	cv_agg's multi_error: 0.758628 + 0.000998674
    [330]	cv_agg's multi_error: 0.758501 + 0.000971393
    [340]	cv_agg's multi_error: 0.758433 + 0.000922703
    [350]	cv_agg's multi_error: 0.758311 + 0.000885534
    [360]	cv_agg's multi_error: 0.758235 + 0.000890509
    [370]	cv_agg's multi_error: 0.758157 + 0.000952454
    [380]	cv_agg's multi_error: 0.75806 + 0.000923153
    [390]	cv_agg's multi_error: 0.757906 + 0.000984443
    [400]	cv_agg's multi_error: 0.75781 + 0.00097321
    [410]	cv_agg's multi_error: 0.757786 + 0.00100955
    [420]	cv_agg's multi_error: 0.757758 + 0.00100718
    [430]	cv_agg's multi_error: 0.757575 + 0.000981183
    [440]	cv_agg's multi_error: 0.757525 + 0.000998983
    [450]	cv_agg's multi_error: 0.757463 + 0.000984541
    [460]	cv_agg's multi_error: 0.757358 + 0.000946481
    [470]	cv_agg's multi_error: 0.757313 + 0.000987353
    [480]	cv_agg's multi_error: 0.757219 + 0.000950081
    [490]	cv_agg's multi_error: 0.757157 + 0.000979591
    [500]	cv_agg's multi_error: 0.757051 + 0.000989398
    [510]	cv_agg's multi_error: 0.757035 + 0.00100007
    [520]	cv_agg's multi_error: 0.757 + 0.000991281
    [530]	cv_agg's multi_error: 0.756976 + 0.000995501
    [540]	cv_agg's multi_error: 0.756915 + 0.00097955
    [550]	cv_agg's multi_error: 0.756892 + 0.000976682
    [560]	cv_agg's multi_error: 0.75681 + 0.00100846
    [570]	cv_agg's multi_error: 0.756825 + 0.00099077
    [580]	cv_agg's multi_error: 0.756789 + 0.000969735
    [590]	cv_agg's multi_error: 0.756726 + 0.000942007
    [600]	cv_agg's multi_error: 0.756622 + 0.000963539
    [610]	cv_agg's multi_error: 0.756607 + 0.000938365
    [620]	cv_agg's multi_error: 0.756597 + 0.000928408