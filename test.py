import MeCab
f = open('kokoro.txt')
text = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
tagger = MeCab.Tagger("-Odump")
print(tagger.parse(f))