import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_name):
    # 検索対象取得
    df=pd.read_csv(f"./{csv_name}")
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません".format(word))
        eel.view_log_js("『{}』を追加します".format(word))

        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(f"./{csv_name}",encoding="utf_8-sig")
    print(source)