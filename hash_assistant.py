#!python3
"""
任意のファイルのハッシュ値(SHA1, SHA256, SHA512, MD5)を求め、一致しているかを確認します。
"""
import hashlib
import unicodedata

#指定のハッシュ関数確認用
userhs = 0

#公式サイト等に記載してある正しいハッシュ値を入力し、[correcths]に代入する
while True:
    print()                                                                 #改行
    print("[A]：正しいハッシュ値を以下に入力してください。")
    correcths = input()
    
    #半角英数判定用フラグ
    flag = 0

    #一文字ごとに半角英数を判定し、半角英数以外が含まれていた時、ハッシュ値入力に戻る
    for i in correcths:
        if unicodedata.east_asian_width(i) != "Na":
            print()                                                         #改行
            print("ハッシュ値が適切ではありません。半角英数で入力してください。")
            flag = 1
            break
    if flag == 1:
        continue

    break
print()                                                                     #改行

#ダウンロードしたファイルなどの絶対パスを入力し、[userobject]に代入する
while True:
    print("[B]：ハッシュ値を確認したいファイルの絶対パスを以下に入力してください。")
    userobject = input()

    if "/" in userobject or "\\" in userobject:
        break

    print()                                                                 #改行
    print("パスが誤っています。正しいパスを入力してください。") 
print()                                                                     #改行

#適用するハッシュ関数を選択し、[userhs]に代入する
#誤った数字の場合、ループする
while True:
    print("[対応ハッシュ関数]\n" + 
    "SHA1・・・1\n" + 
    "SHA256・・・2\n" + 
    "SHA512・・・3\n" + 
    "MD5・・・4")
    userhs = int(input("使用するハッシュ関数の番号を選択してください。："))
    
    if 1 <= userhs <= 4:
        break

    print("番号が違います。1～4の数字のいずれかを入力してください。")
    print()                                                                 #改行

#[userobject]のファイルを開き、指定のハッシュ関数でハッシュ値を求める
#求めたハッシュ値を[objecths]に、使用したハッシュ関数を[selecthash]に代入する
with open(userobject, "rb") as fileoj:
    readdata = fileoj.read()
    if userhs == 1:
        objecths = hashlib.sha1(readdata).hexdigest()
        selecthash = "SHA1"
    elif userhs == 2:
        objecths = hashlib.sha256(readdata).hexdigest()
        selecthash = "SHA256"
    elif userhs == 3:
        objecths = hashlib.sha512(readdata).hexdigest()
        selecthash = "SHA512"
    elif userhs == 4:
        objecths = hashlib.md5(readdata).hexdigest()
        selecthash = "MD5"

print()                                                                     #改行
#元のハッシュ値と求めたハッシュ値を表示する
print(f"[A]　{selecthash}: {correcths.upper()}")
print(f"[B]　{selecthash}: {objecths.upper()}")
print()                                                                     #改行

print("-----------------------------------------")
#2つのハッシュ値が一致しているか否かを確認する
if correcths.upper() == objecths.upper():
    print("ハッシュ値が一致しています。")
else:
    print("*ハッシュ値が異なります。*")
print("-----------------------------------------")

print()                                                                     #改行
input("Press any key to exit")