import pandas as pd
import MeCab

def main():
    filename1 = "#にゃんにゃんにゃんの日"
    filename2 = "#ねこの日"

    analize(filename1,filename2)



#ツイートの内容で単語を抜き出し、その出現回数上位5つを抽出
#その5つの中で重複がどの程度あるかを返す
def analize(filename1,filename2):  
    search = 10     #10この上位ワードから
    border = 0.4    #3つの重複があればFalseを返すように設定
    answer = True

    ana1 = textanalize(filename1)
    ana2 = textanalize(filename2)
    a1 = ana1.value_counts().head(search).index
    a2 = ana2.value_counts().head(search).index
    count = 0
    for i in a1:
        for j in a2:
            if i == j:
                count += 1
                break
    
    if count/search >= border:
        answer = False
    return answer

def textanalize(filename):
    csvdata = csvcheck("..\..\datastrage\RawData\\" + filename + ".csv")
    text = ""
    for t in csvdata:
        text = text + t + "\n"
    m = MeCab.Tagger ('-Ochasen')
    word=""
    node = m.parseToNode(text)
    hairetu = []
    inhairetu = []
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in ["名詞"]:
            origin = node.feature.split(",")[6]
            #word = word + " " + origin
            if origin not in ["する","いる","ある","なる","*"]:
                # word = word + " " + origin
                inhairetu = [origin,hinshi]
                hairetu.append(inhairetu)
        node = node.next
    df = pd.Series(hairetu)
    return df

def csvcheck(passcsv):
    csvdata = []
    df = pd.read_csv(passcsv)
    csvdata = df["ツイート内容"]
    return csvdata

if __name__ == "__main__":
        main()