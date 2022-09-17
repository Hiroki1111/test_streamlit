import streamlit as st
from PIL import Image
import datetime

st.title("ショート")
st.caption("テストアプリです。")
st.subheader("コメント")
st.text("夏休みが終わって大変です。")
st.text("以下はサンプルプログラムです。")
code = '''
import streamlit as st
st.title("ショートアプリ")
'''

st.code(code, language='python')

#画像
image = Image.open("IMG_0560.PNG")
st.image(image, width = 200)

#動画
# video_file = open("v12044gd0000c7e77ijc77u02k5qk2g0.mp4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

#フォームの形成
with st.form(key="profile_form"):
    #テキストボックス
    name = st.text_input('名前')
    #ターミナルに表示
    # print(name)

    # セレクトボックス
    # age_category = st.selectbox("年齢層", ("未成年", "成人"))
    age_category = st.radio("年齢層", ("未成年", "成人"))

    # 複数選択
    hobby = st.multiselect("趣味", ("アニメ", "ゲーム", "プログラミング", "料理"))

    # チェックボックス
    robot = st.checkbox("私はロボットではありません")

    # スライダー
    height = st.slider("プログラミング自信度", min_value = 0, max_value = 100)

    # カラーピッカー
    color = st.color_picker("あなたのイメージカラー", "#00f900")

    # 日付
    start_date = st.date_input("入力日", datetime.date(2022, 9, 17))

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    #↑ボタンが押されている場合はtrue、押されていない場合はfalse
    # print("submit_btn:{}".format(submit_btn))
    # print("cancel_btn:{}".format(cancel_btn))
    if submit_btn == True:
        st.text("ようこそ！{}さん".format(name))
        st.text("年齢層:{}".format(age_category))
        st.text("趣味:{}".format(",".join(hobby)))
