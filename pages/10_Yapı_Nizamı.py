import streamlit as st
from PIL import Image

st.title("Yapı Nizamı/Bitişik Binalarla Döşeme Seviyeleri")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.subheader("Açıklama")
    st.write("Bitişik binaların konumları deprem \
            performansını çarpışma nedeniyle etkileyebilmektedir. Kenarda yer alan binalar bu durumdan \
            en olumsuz etkilenmekte, bitişik bina ile kat seviyeleri farklıysa bu olumsuzluk daha da \
            artmaktadır. Çarpışma etkisinin söz konusu olduğu durumlar dışarıdan yapılacak gözlemler ile \
            belirlenecektir. Yapı nizam durumu ve bitişik binalarla döşeme seviyesi durumu birlikte \
            değerlendirilecektir."
            )

    image = Image.open("./figures/nizam_durumu.jpg")
    st.image(image, width = 280)

    nizam_durumu = st.radio(
        "Yapının nizam durumunu seçiniz.",
        ("Ayrık", "Bitişik"))

    st.session_state["nizam_durumu"] = nizam_durumu


    if "nizam_konumu" not in st.session_state:
        st.session_state["nizam_konumu"] = ""

    if "doseme_seviyesi" not in st.session_state:
        st.session_state["doseme_seviyesi"] = ""



    if st.session_state["nizam_durumu"] == "Bitişik":
        nizam_konumu = st.radio(
            "Bitişik yapının konumunu seçiniz.",
            ("Ortada", "Köşede"))

        st.session_state["nizam_konumu"] = nizam_konumu

        image = Image.open("./figures/doseme_seviyesi.jpg")
        st.image(image, width = 540)

        doseme_seviyesi = st.radio(
            "Bitişik yapının döşeme seviyesi durumunu seçiniz.",
            ("Aynı", "Farklı"))

        st.session_state["doseme_seviyesi"] = doseme_seviyesi
    


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")