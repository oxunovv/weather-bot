import requests
from bs4 import BeautifulSoup

# Viloyat nomlari uchun mapping
city = {
    "Toshkent": "tashkent",
    "Andijon": "andyzhan",
    "Farg'ona": "ferhana",
    "Namangan": "namanhan",
    "Samarqand": "samarkand",
    "Buxoro": "bukhara",
    "Navoiy": "navoi",
    "Qashqadaryo": "karshi",  # Qarshi shahri
    "Surxondaryo": "termez",  # Termiz shahri
    "Xorazm": "urhench",      # Urganch shahri
    "Qoraqalpog‘iston": "nukus",
    "Jizzax": "dzhyzak",
    "Sirdaryo": "hulistan",
}

#Uzbekistan uchun
uzbekistan = [
    'tashkent', 'samarkand', 'namanhan', 'andyzhan', 'ferhana', 'nukus', 'bukhara',
    'karshi', 'navoi', 'marhilan', 'kokand', 'urhench', 'dzhyzak', 'chyrchyk', 'termez',
    'anhren', 'almalyk', 'denau', 'bekabad', 'shakhrisabz', 'hulistan', 'kattakurhan',
    'kuvasai', 'kunhrad', 'zarafshan', 'namanhanska-oblast-chust', 'kasan', 'kahan',
    'asaka', 'chartak', 'urhut', 'khiva', 'turtkul', 'beruni', 'manhit'
]

def ob_havo_qidir(nomi: str) -> str:
    # Nomi shahar ro‘yxatida bo‘lsa to‘g‘ridan-to‘g‘ri
    if nomi.lower() in uzbekistan:
        slug = nomi.lower()
    # Aks holda city lug‘atidan viloyat markaziga mapping
    elif nomi in city:
        slug = city[nomi]
    else:
        return f"❗️ '{nomi}' bo‘yicha ob-havo topilmadi."

    url = f"https://sinoptik.ua/pohoda/{slug}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "❌ Sahifani yuklab bo‘lmadi."

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temp_now = soup.select_one("p.R1ENpvZz")
        current_temp = temp_now.text.strip() if temp_now else "Noma’lum"

        img_tag = soup.find("img",attrs={'class' :"iXU+aDg2"})
        weather_status = img_tag["alt"] if img_tag and "alt" in img_tag.attrs else "Noma’lum"

        sun_times = soup.find_all("span",attrs={'class': 'WJJwi+RN'})
        # print(sun_times)
        sunrise = sun_times[0].text if len(sun_times) > 0 else "Noma’lum"
        sunset = sun_times[1].text if len(sun_times) > 1 else "Noma’lum"

        min_temp_tag = soup.find("div", class_="+Ncy59Ya")
        min_temp = min_temp_tag.find_all("p")[1].text if min_temp_tag else "Noma’lum"
        max_temp_tag = min_temp_tag.find_next_sibling("div") if min_temp_tag else None
        max_temp = max_temp_tag.find_all("p")[1].text if max_temp_tag else "Noma’lum"

        return (
            f"📍 {nomi} ob-havo:\n"
            f"🌡 Hozirgi harorat: {current_temp}\n"
            f"☀️ Holat: {weather_status}\n"
            f"🔻 Minimum: {min_temp}, 🔺 Maksimum: {max_temp}\n"
            f"🌅 Quyosh chiqishi: {sunrise}, 🌇 Botishi: {sunset}"
        )

    except Exception as e:
        return f"⚠️ Xatolik yuz berdi: {e}"

# Foydalanish:

# Misollar
# ob_havo_qidir("Andijon")      # viloyat nomi
# print(ob_havo_qidir("ferhana"))      # shahar nomi (ingliz translit)
# print(ob_havo_qidir("Samarqand"))    # viloyat nomi
# print(ob_havo_qidir("Qashqadaryo"))        # shahar nomi