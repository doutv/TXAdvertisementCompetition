# 腾讯广告算法大赛2020

# TODO
+ random age and gender
# 赛题
具体而言，在比赛期间，我们将为参赛者提供一组用户在长度为 91 天（3 个月）的时间窗
口内的广告点击历史记录作为训练数据集。每条记录中包含了日期（从 1 到 91）、用户信息
（年龄，性别），被点击的广告的信息（素材 id、广告 id、产品 id、产品类目 id、广告主
id、广告主行业 id 等），以及该用户当天点击该广告的次数。测试数据集将会是另一组用户
的广告点击历史记录。提供给参赛者的测试数据集中不会包含这些用户的年龄和性别信息。
本赛题要求参赛者预测测试数据集中出现的用户的年龄和性别，并以约定的格式提交预测结
果。

+ click_log.csv
  + time
  + user_id
  + creative_id
  + click_times
+ user.csv
  + user_id
  + age [1,10]
  + gender [1,2]
+ ad.csv
  + creative_id
  + ad_id
  + product_id
  + product_category
  + advertiser_id
  + industry

+ submission.csv
  + user_id
  + predicted_age [1,10]
  + predicted_gender [1,2]

# Analyse data

# Resources
+ 公众号
+ QQ群
+ [智能钛平台文档](https://github.com/tencentyun/qcloud-documents/tree/master/product/%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%B8%8EAI/%E6%99%BA%E8%83%BD%E9%92%9B%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0)
+ [2019冠军代码](https://github.com/guoday/Tencent2019_Preliminary_Rank1st?tdsourcetag=s_pctim_aiomsg)
+ [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)