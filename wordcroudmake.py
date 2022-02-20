import random
import MeCab
from matplotlib.cbook import flatten
import pandas as pd
from datetime import datetime,timezone

font = ""

def main():
    word = "キムワイプ"
    wordcroudmaker(word)

def wordcroudmaker(treword):
    fontlist = csvcheck("fontlist.csv")
    font = fontlist[random.randint(0,11)]
    text = ""
    df = pd.read_csv("..\..\datastrage\RawData\\" + treword + ".csv")
    textarray = df["ツイート内容"]
    for t in textarray:
        text = text + t + "\n"

    m = MeCab.Tagger ('-Ochasen')
    
    word=""
    node = m.parseToNode(text)

    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in ["名詞","動詞","形容詞"]:
            origin = node.feature.split(",")[6]
            #word = word + " " + origin
            if origin not in ["する","いる","ある","なる",treword]:
                word = word + " " + origin
        node = node.next

        from wordcloud import WordCloud
    
    fpath = "C:\Windows\\fonts\\" + font
    print(fpath)
    wordcloud = WordCloud(background_color="white",font_path=fpath,width=600,height=400,min_font_size=15)
    wordcloud.generate(word)
    now = datetime.now()
    filename = "..\..\datastrage\wordcroud\\" + treword + now.strftime('%Y%m%d%H%M') + ".png"
    wordcloud.to_file(filename)
    return filename

def csvcheck(passcsv):
    csvdata = []
    df = pd.read_table(passcsv)
    csvdata = df["name"]
    return csvdata

if __name__ == "__main__":
    main()