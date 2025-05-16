
import streamlit as st
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="WatermelonWatch", page_icon="🍉")

st.image("banner.png", use_container_width=True)

# Wybór języka
lang = st.selectbox("🌍 Choose language / Wybierz język", ["English", "Polski"])

# Treści językowe
texts = {
    "English": {
        "title": "🍉 WatermelonWatch",
        "date_prompt": "📅 Select date range:",
        "start_date": "Start date",
        "end_date": "End date",
        "submit": "Analyze forecast",
        "results": "🔍 Forecasted average temperature and seasonality:",
        "too_cold": "❄️ Too cold – expected drop in watermelon sales.",
        "strawberry": "🍓 Strawberry season – possible drop in watermelon demand.",
        "hot_weather": "🔥 Hot weather – increase watermelon stock.",
        "normal": "✅ Moderate conditions – keep current stock level."
    },
    "Polski": {
        "title": "🍉 WatermelonWatch",
        "date_prompt": "📅 Wybierz zakres dat do analizy:",
        "start_date": "Data od",
        "end_date": "Data do",
        "submit": "Analizuj prognozę",
        "results": "🔍 Prognozowana średnia temperatura i sezonowość:",
        "too_cold": "❄️ Zbyt zimno – prognozowany spadek sprzedaży arbuza.",
        "strawberry": "🍓 Sezon truskawkowy – możliwa redukcja zatowarowania arbuza.",
        "hot_weather": "🔥 Wysoka temperatura – rekomendacja zwiększenia zapasów arbuza.",
        "normal": "✅ Warunki umiarkowane – zatowarowanie bez zmian."
    }
}

st.title(texts[lang]["title"])
st.markdown(f"### {texts[lang]['date_prompt']}")

# Formularz wyboru dat
with st.form("date_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(texts[lang]["start_date"], datetime.today())
    with col2:
        end_date = st.date_input(texts[lang]["end_date"], datetime.today())
    submit = st.form_submit_button(texts[lang]["submit"])

# Funkcja symulująca pogodę i sezon truskawkowy
def simulate_weather(start_date, end_date):
    days = (end_date - start_date).days + 1
    forecast = []
    for i in range(days):
        temp = random.randint(14, 34)
        is_strawberry = start_date.month == 6 or start_date.month == 7
        forecast.append((start_date.strftime("%Y-%m-%d"), temp, is_strawberry))
        start_date += timedelta(days=1)
    return forecast

# Logika predykcji
def analyze(forecast):
    avg_temp = sum([t[1] for t in forecast]) / len(forecast)
    strawberry = any([t[2] for t in forecast])
    
    if avg_temp < 18:
        return texts[lang]["too_cold"]
    elif strawberry and avg_temp > 22:
        return texts[lang]["strawberry"]
    elif avg_temp >= 28:
        return texts[lang]["hot_weather"]
    else:
        return texts[lang]["normal"]

# Wynik
if submit:
    forecast = simulate_weather(start_date, end_date)
    st.markdown(f"### {texts[lang]['results']}")
    for day, temp, straw in forecast:
        st.write(f"{day}: {temp}°C {'🍓' if straw else ''}")
    st.success(analyze(forecast))
