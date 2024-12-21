#ある商品のN日間の売上が整数列A1,A2,…,ANとして与えられる。
#Ai(1≦i≦N) がi日目の売上を表す。
#あなたは、2日目以降の各日について、
#その日の売上が前日の売上よりどれだけ高かったか (あるいは低かったか)
#を出力するプログラムを作成することにした。
#より具体的には、プログラムは 
#N−1行を出力し、i行目(1≦i≦N−1) の内容は次の通りである。
#Ai+1がAiと等しい場合: stay
#Ai+1がAiより小さい場合: down [減少量]、ここで [減少量] は整数値 
#Ai−Ai+1 Ai+1がAiより大きい場合: up [増加量]、
#ここで [増加量] は整数値 Ai+1 − Ai 
#このプログラムを作成せよ。
#制約
#2≦N≦100,000
#0≦A 
#i ≦1,000,000,000
#入力中の値はすべて整数である。

# メイン関数
def main() -> None:
    input_data = create_input_data()

    for idx in range(len(input_data) - 1):
        if input_data[idx] == input_data[idx + 1]:
            print('stay')
        elif input_data[idx] > input_data[idx + 1]:
            print(f'down {input_data[idx] - input_data[idx + 1]}')
        else:
            print(f'up {input_data[idx + 1] - input_data[idx]}')


def create_input_data() -> None:
    input_data = []

    while True:
        data = str(input())

        if data.isnumeric():
            input_data.append(int(data))
        else:
            break
    return input_data


if __name__ == '__main__':
    main()
