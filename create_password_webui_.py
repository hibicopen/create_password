import streamlit as st
import string
import secrets
import re


def main():
    # タイトル表示
    st.title('パスワード生成')
    # テキスト表示
    count = st.number_input(label="パスワード文字数（6～24）", value=8, )
    number = st.selectbox("パスワード組合せ",
                          ["１：小文字", "２：小文字＋大文字", "３：小文字＋大文字＋数字", "４：小文字＋大文字＋数字＋記号", "５：数字"])
    buttom1 = st.button('生成')

    if buttom1:
        password = create(count, number)
        if password == 0:
            st.write("６～２４桁で指定してください")
        elif check_password(password, number):
            st.write("パスワード生成に失敗しました。もう一度 生成してください")
        else:
            st.write("パスワードを生成しました")
            st.code(password)


def create(count, number):
    # ユーザーが入力した条件でパスワードを生成する

    if 6 <= count <= 24:
        if number == "１：小文字":
            character = string.ascii_lowercase
            password = ''.join(secrets.choice(character) for _ in range(count))
        elif number == "２：小文字＋大文字":
            character = string.ascii_lowercase + string.ascii_uppercase
            password = ''.join(secrets.choice(character) for _ in range(count))
        elif number == "３：小文字＋大文字＋数字":
            character = string.ascii_lowercase + string.ascii_uppercase + string.digits
            password = ''.join(secrets.choice(character) for _ in range(count))
        elif number == "４：小文字＋大文字＋数字＋記号":
            character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            password = ''.join(secrets.choice(character) for _ in range(count))
        elif number == "５：数字":
            character = string.digits
            password = ''.join(secrets.choice(character) for _ in range(count))
        return password
    else:
        return 0


def check_password(verify_password, verify_number):  # 生成されたパスワードが条件を満たしているかを確認する
    is_match = [0, 0, 0, 0]  # 小文字、大文字、数字、記号があれば各要素に1をセット
    for c in verify_password:
        if re.match(r'[a-z]', c):  # 小文字であれば
            is_match[0] = 1
        elif re.match(r'[A-Z]', c):  # 大文字であれば
            is_match[1] = 1
        elif re.match(r'[0-9]', c):  # 数字であれば
            is_match[2] = 1
        elif re.match(r'[!-/:-~]', c):  # 記号であれば
            is_match[3] = 1
    # 条件満たしていなければTrueを返す
    if verify_number == "２：小文字＋大文字":
        if is_match != [1, 1, 0, 0]:
            return True
    if verify_number == "３：小文字＋大文字＋数字":
        if is_match != [1, 1, 1, 0]:
            return True
    if verify_number == "４：小文字＋大文字＋数字＋記号":
        if is_match != [1, 1, 1, 1]:
            return True
    return False


if __name__ == "__main__":  # よくわからないがおまじない → create_password_gui.pyを直接実行した時と importされたことで動作したものと区別するための記述
    main()  #test
