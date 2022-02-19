
#夏目漱石「こころ」の取り込み
tytle = "Vtuber 20220214_01"
f = open(tytle + '.csv', encoding="utf-8")
text = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
#単語の分割
import MeCab
import pandas as pd
import numpy as np
 
m = MeCab.Tagger ('-Ochasen')
 
word=""
node = m.parseToNode(text)
while node:
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞","動詞","形容詞"]:
        origin = node.feature.split(",")[6]
        #word = word + " " + origin
        if origin not in ["する","いる","ある","なる"]:
            word = word + " " + origin
    node = node.next
 
 
wordcloud.to_file(tytle + ".png")