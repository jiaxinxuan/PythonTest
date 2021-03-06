from wordcloud import WordCloud

f = open(u'/home/jia/jieba.json','r',encoding= 'UTF-8').read()
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2, font_path='/home/jia/bole.ttf').generate(f)

# width,height,margin可以设置图片属性

# generate 可以对全部文本进行自动分词,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
#wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集

#background_color参数为设置背景颜色,默认颜色为黑色

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('test.png')