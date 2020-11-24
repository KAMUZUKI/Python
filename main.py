import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator
text = open(r'D:\ciyuntu\wz.txt', "r",encoding='utf-8').read()
cut_text = jieba.cut(text)
result = " ".join(cut_text)
wc = WordCloud(
        width=3840,height=62160,
        max_font_size=25,min_font_size=7,
        mode='RGBA',font_path='D:/ciyuntu/wenben.ttc',
        repeat=True,max_words=200000,scale=8,
        )
image = Image.open(r'D:\ciyuntu\image8.jpg')
graph = np.array(image)
wc.generate(result)
plt.figure("词云图")
image_color = ImageColorGenerator(graph)#从背景图片生成颜色值
wc.recolor(color_func=image_color)
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
wc.to_file('C:/Users/MUZUKI/Desktop/photo/wordcloud2.png')
plt.axis("off")
plt.show()

