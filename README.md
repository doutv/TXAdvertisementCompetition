# 腾讯广告算法大赛2020


# TODO
+ [x] random age and gender (numpy and pandas basic operation)
+ [x] lightgbm for GBDT(Gradient Boosting Decision Tree) 
  + https://lightgbm.readthedocs.io/en/latest/index.html
  + https://blog.csdn.net/u012735708/article/details/83749703
  + https://www.cnblogs.com/bjwu/p/9307344.html
+ [x] Embedding
  + [x] tf-idf
    + https://zhuanlan.zhihu.com/p/31197209
    + https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
    + https://blog.csdn.net/Eastmount/article/details/50323063
  + [ ] Word2vec
    + https://zhuanlan.zhihu.com/p/26306795
    + https://www.tensorflow.org/tutorials/text/word_embeddings
    + https://zhuanlan.zhihu.com/p/53194407
    + https://zhuanlan.zhihu.com/p/46016518
    + https://www.zhihu.com/question/32275069
+ [ ] Transformer
  + https://github.com/huggingface/transformers#installation
  + https://jalammar.github.io/illustrated-transformer/
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
  + creative_id 广告素材id
  + ad_id 素材所属的广告id
  + product_id
  + product_category 产品类别id
  + advertiser_id
  + industry 广告主所属行业的id

+ submission.csv
  + user_id
  + predicted_age [1,10]
  + predicted_gender [1,2]

# 选手思路分享
from:
+ coggle
+ 腾讯广告算法大赛

link:
+ https://mp.weixin.qq.com/s/Spk0qAeg-T2S0cluenMWxA
+ https://mp.weixin.qq.com/s/ZC3V6XZg3xwLUHEXBajt6A
+ https://mp.weixin.qq.com/s?__biz=MzIzMzgzOTUxNA==&mid=2247484348&idx=1&sn=21979700dd0bb650a935f4e4f32e31bd&chksm=e8fecd49df89445f81f78d328282e2259ffa1a195ac3ffff28d07a530cbb0435fc4ef51cc697&mpshare=1&scene=1&srcid=&sharer_sharetime=1589677777078&sharer_shareid=3790971c6b4aa1299e38b0567b32d666&key=826ecc1d344963fbad9b320962d25ef81fc278ca76debfc502be383c22cff7cacfcc4f41711f5131d56dede127d6e8d1df4bb8d5b2fa6b377575fad9f9f853e8851d5d5d0d241e50a3497b0c54d48a37&ascene=1&uin=MTI1MTI1NjQ2MQ%3D%3D&devicetype=Windows+10+x64&version=62090070&lang=zh_CN&exportkey=A1FTXTJLZiMNQozjvUgoub8%3D&pass_ticket=FArSThuR9nKvM4jN2oVyYXyz4XMl481ozDAl72kVU9rveDWLVEO7FAy419Guj3V9
+ https://mp.weixin.qq.com/s/VVGjUxcckWL1oqqBfdGv4Q
+ https://mp.weixin.qq.com/s/q-vK_2e-Uhv6wmClTMvy7Q
+ https://mp.weixin.qq.com/s/ISQjOGcc_spSNVeeg75d8w?tdsourcetag=s_pctim_aiomsg

# Resources
+ 公众号
+ QQ群
+ [智能钛平台文档](https://github.com/tencentyun/qcloud-documents/tree/master/product/%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%B8%8EAI/%E6%99%BA%E8%83%BD%E9%92%9B%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0)
+ [2019冠军代码](https://github.com/guoday/Tencent2019_Preliminary_Rank1st?tdsourcetag=s_pctim_aiomsg)
+ [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
+ [深度学习如何入门](https://www.zhihu.com/question/343407265/answer/830912894)
+ [动手学深度学习](https://zh.gluon.ai/index.html)
+ [Natural Language Processing with PyTorch](https://nlp-pt.apachecn.org/)
+ [NLP代码示例](https://github.com/graykode/nlp-tutorial)