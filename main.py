import pandas as pd
import streamlit as st
from datetime import datetime
import os
import random

# ----------------------
# CONFIG
# ----------------------
st.set_page_config(page_title="Ruh Hali Önerici", page_icon="🎵", layout="centered")

DATA_FILE = "gecmis_log.xlsx"

# ----------------------
# TEMALAR
# ----------------------
tema = st.sidebar.radio("Tema Seçimi", ["Açık", "Koyu"])
if tema == "Koyu":
    st.markdown(
        """
        <style>
        .css-18e3th9 {background-color: #333333;}
        .css-1d391kg {color: #FFFFFF;}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------
# KULLANICI GİRİŞİ
# ----------------------
st.title("🎵 Ruh Hali Önerici")
username = st.text_input("Kullanıcı Adı:", "")

# ----------------------
# ÖNERİLER
# ----------------------
varsayılan_ruh_halleri = {
    "Mutlu": {"müzik": ["Happy - Pharrell", "Walking on Sunshine - Katrina"], "aktivite": ["Dans etmek", "Arkadaşlarla buluşmak"], "mesaj": "Harika gidiyorsun! 😄"},
    "Üzgün": {"müzik": ["Someone Like You - Adele", "Fix You - Coldplay"], "aktivite": ["Günlük yazmak", "Sessiz bir yürüyüş"], "mesaj": "Her şey geçecek, güç sende! 💛"},
    "Stresli": {"müzik": ["Weightless - Marconi", "Clair de Lune - Debussy"], "aktivite": ["Meditasyon yapmak", "Derin nefes egzersizi"], "mesaj": "Sakin ol ve nefes al 🧘‍♂️"},
    "Yorgun": {"müzik": ["Stay With Me - Sam Smith", "Someone You Loved - Lewis Capaldi"], "aktivite": ["Kısa bir şekerleme", "Bitki çayı içmek"], "mesaj": "Kendine zaman ayır 🌿"},
    "Heyecanlı": {"müzik": ["Can't Stop the Feeling - Justin", "Uptown Funk - Bruno Mars"], "aktivite": ["Yeni bir proje başlat", "Spor yapmak"], "mesaj": "Enerjini iyi kullan! ⚡"},
    "Sakin": {"müzik": ["River Flows In You - Yiruma", "Gymnopédie - Satie"], "aktivite": ["Kitap okumak", "Doğa yürüyüşü"], "mesaj": "Huzurun tadını çıkar 🌸"},
    "Motivasyonlu": {"müzik": ["Eye of the Tiger - Survivor", "Stronger - Kanye"], "aktivite": ["Plan yap", "Hedef belirle"], "mesaj": "Devam et, harika işler başarabilirsin 💪"},
    "Kızgın": {"müzik": ["Break Stuff - Limp Bizkit", "You Oughta Know - Alanis"], "aktivite": ["Spor yapmak", "Sessizce yazmak"], "mesaj": "Sakin ol, nefes al ve devam et 😤"},
    "Endişeli": {"müzik": ["Breathe Me - Sia", "Comfortably Numb - Pink Floyd"], "aktivite": ["Günlük yazmak", "Müzik dinlemek"], "mesaj": "Her şey yoluna girecek, güven 😊"}
}

# ----------------------
# VERİ YÜKLEME
# ----------------------
if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Tarih", "Kullanıcı", "Ruh Hali", "Müzik", "Aktivite", "Mesaj"])
    df.to_excel(DATA_FILE, index=False)

# ----------------------
# YENİ RUH HALİ EKLEME
# ----------------------
st.sidebar.subheader("Yeni Ruh Hali Ekle")
yeni_ruh = st.sidebar.text_input("Ruh Hali İsmi")
yeni_muzik = st.sidebar.text_input("Önerilen Müzik (virgülle ayır)")
yeni_aktivite = st.sidebar.text_input("Önerilen Aktivite (virgülle ayır)")
yeni_mesaj = st.sidebar.text_input("Motivasyon Mesajı")

if st.sidebar.button("Ekle"):
    if yeni_ruh and yeni_muzik and yeni_aktivite and yeni_mesaj:
        varsayılan_ruh_halleri[yeni_ruh] = {
            "müzik": [m.strip() for m in yeni_muzik.split(",")],
            "aktivite": [a.strip() for a in yeni_aktivite.split(",")],
            "mesaj": yeni_mesaj
        }
        st.sidebar.success(f"{yeni_ruh} ruh hali eklendi!")
    else:
        st.sidebar.error("Lütfen tüm alanları doldurunuz!")

# ----------------------
# RUH HALİ SEÇİMİ
# ----------------------
st.subheader("Ruh Halinizi Seçin")
ruh_hali = st.selectbox("Ruh Hali", list(varsayılan_ruh_halleri.keys()))

if st.button("Öneri Getir"):
    secilen = varsayılan_ruh_halleri[ruh_hali]
    muzik = random.choice(secilen["müzik"])
    aktivite = random.choice(secilen["aktivite"])
    mesaj = secilen["mesaj"]

    st.markdown(f"**Ruh Haliniz:** {ruh_hali}")
    st.markdown(f"**Önerilen Müzik:** {muzik}")
    st.markdown(f"**Önerilen Aktivite:** {aktivite}")
    st.markdown(f"**Motivasyon Mesajı:** {mesaj}")

    # ----------------------
    # VERİ KAYDETME
    # ----------------------
    if username:
        yeni_satir = {
            "Tarih": datetime.now(),
            "Kullanıcı": username,
            "Ruh Hali": ruh_hali,
            "Müzik": muzik,
            "Aktivite": aktivite,
            "Mesaj": mesaj
        }
        df = pd.concat([df, pd.DataFrame([yeni_satir])], ignore_index=True)
        df.to_excel(DATA_FILE, index=False)
        st.success("Öneri kaydedildi! ✅")

# ----------------------
# GRAFİKSEL GÖRSELLEŞTİRME
# ----------------------
st.subheader("Ruh Hali Geçmişi Grafiği")
if username:
    user_df = df[df["Kullanıcı"] == username]
    if not user_df.empty:
        grafik = user_df["Ruh Hali"].value_counts()
        st.bar_chart(grafik)
    else:
        st.info("Henüz veri yok, öneri alınca grafik görünecek.")
else:
    st.info("Grafik için kullanıcı adınızı girin.")