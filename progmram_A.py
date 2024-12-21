#あなたは、
#3 桁の整数を入力として受け取り、それを 
#2 倍して出力するプログラムの作成を頼まれた。
#ところが、どうやらプログラムに入力される文字列 
#S に英小文字が紛れ込むことがあるようだ。そこで、その場合はエラーを出力することにした。
#S が 
#3 桁の整数である場合 (0 で始まる場合を含む) はその 
#2 倍の値を出力し、そうでなければ error と出力するプログラムを作成せよ。

# メイン関数
def main() -> None:
    # 文字列で数字を受け取る
    input_data = str(input('3桁の数字：'))

    # 文字列が数値かを判定
    if input_data.isnumeric():
        print(f'{input_data}×2={int(input_data) * 2}')
    else:
        print('error')

if __name__ == '__main__':
    main()