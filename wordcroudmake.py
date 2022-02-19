import MeCab
import pandas as pd
from datetime import datetime,timezone

def main():
    word = "キムワイプ"
    wordcroudmaker(word)

def wordcroudmaker(treword):        
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
    
    fpath = "meiryo.ttc"
    wordcloud = WordCloud(background_color="white",font_path=fpath,width=600,height=400,min_font_size=15)
    wordcloud.generate(word)
    now = datetime.now()
    filename = "..\..\datastrage\wordcroud\\" + treword + now.strftime('%Y%m%d%H%M') + ".png"
    wordcloud.to_file(filename)
    return filename

if __name__ == "__main__":
    main()