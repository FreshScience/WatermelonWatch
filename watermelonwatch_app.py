
import streamlit as st
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="WatermelonWatch", page_icon="🍉")

st.title("🍉 WatermelonWatch")
st.subheader("Prognoza sprzedaży arbuza na podstawie pogody i sezonu truskawkowego")

st.image("https://upload.wikedia.org/wikipedia/commons/3/36/Watermelon_cross_BNC.jpg", use_column_width=True)

# Formularz wejściowy
with st.form("form"):
    start_date = st.date_input("Data od", datetime.today())
    end_date = st.date_input("Data do", datetime.today())
    submit = st.form_submit_button("Analizuj prognozę")

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
        return "❄️ Zbyt zimno – prognozowany spadek sprzedaży arbuza."
    elif strawberry and avg_temp > 22:
        return "🍓 Sezon truskawkowy – możliwa redukcja zatowarowania arbuza."
    elif avg_temp >= 28:
        return "🔥 Wysoka temperatura – rekomendacja zwiększenia zapasów arbuza."
    else:
        return "✅ Warunki umiarkowane – zatowarowanie bez zmian."

# Wynik
if submit:
    forecast = simulate_weather(start_date, end_date)
    st.write("### Prognozowana średnia temperatura i sezonowość:")
    for day, temp, straw in forecast:
        st.write(f"{day}: {temp}°C {'🍓' if straw else ''}")
    st.success(analyze(forecast))
