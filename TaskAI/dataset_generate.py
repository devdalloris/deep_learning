import pandas as pd

# Dataset A: CRM tizimidagi nisbatan toza ma'lumotlar
data_a = {
    'ID_CRM': [i for i in range(1, 51)],
    'Company_Name': [
        "UzAuto Motors", "Artel Electronics", "Akfa Group", "Tashkent IT Park", "Korzinka.uz",
        "Hamkorbank", "Kapitalbank", "SQB Bank", "Ucell", "Beeline Uzbekistan",
        "Apex Insurance", "BMB Holding", "Golden House", "Murad Buildings", "Enter Engineering",
        "Texnomart", "Elmakon", "Ishonch Store", "Havas Food", "Makro Supermarket",
        "Orient Group", "Farg'ona Azot", "Navoiy MMK", "Olmaliq MMK", "Uzbekneftegaz",
        "Uzbekistan Airways", "Uzbekistan Railways", "Agromir Group", "Safi-Pishiriqlari", "G'ofur G'ulom Publishing",
        "Hilol Nashr", "Asaxiy.uz", "Olcha.uz", "Zoodmall", "Uzum Market",
        "Payme", "Click.uz", "Apelsin (Azo)", "Yandex Go Uzbekistan", "Express24",
        "MyTaxi", "Choyxona Navvat", "Les Ailes", "Chopar Pizza", "Bellissimo Pizza",
        "Evos", "Oqtepa Lavash", "FeedUp", "Street 77", "Yapona Mama"
    ],
    'City': ["Andijan", "Tashkent", "Tashkent", "Tashkent", "Tashkent", "Andijan", "Tashkent", "Tashkent", "Tashkent", "Tashkent"] * 5,
    'Industry': ["Manufacturing", "Electronics", "Construction", "IT", "Retail", "Banking", "Banking", "Banking", "Telecom", "Telecom"] * 5
}

# Dataset B: Veb-saytdan olingan (biroz "iflos" yoki boshqacha formatdagi ma'lumotlar)
data_b = {
    'ID_WEB': [i for i in range(1001, 1051)],
    'Org_Name': [
        "Uz-Auto Motors AJ", "Artel Elektroniks", "Akfa Holding", "IT-Park Toshkent", "Korzinka Supermarket",
        "Hamkor Bank", "Kapital Bank ATB", "Sanoat Qurilish Bank", "U-cell (Coscom)", "Bilayn Uzb",
        "Apex Sug'urta", "BMB Trade Group", "Golden-House", "Murad Bldg", "Enter Eng.",
        "Texnomart*", "El-makon", "Ishonch Do'konlari", "Havas Market", "Makro",
        "Orient Group Holding", "Fergana Azot", "NMMC (Navoiy)", "AGMK (Olmaliq)", "UNG - Uzbekneftegaz",
        "Havo Yo'llari", "O'zbekiston Temir Yo'llari", "Agromir", "Safi Bakery", "Gofur Gulom",
        "Hilol Nashriyoti", "Asaxiy Books", "Olcha uz", "Zood mall", "Uzum",
        "Pay-me", "Click", "Azo Bank (Apelsin)", "Yandex Taxi", "Express 24",
        "My Taxi Uz", "Navvat", "LesAiles", "Chopar", "Bellissimo",
        "EVOS Burger", "Oqtepa", "Feed Up", "Street-77", "Yapona-Mama"
    ],
    'Location': ["Andijon vil.", "Toshkent sh.", "Tashkent", "Toshkent, Mirzo Ulugbek", "Toshkent", "Andijon", "Toshkent", "Tashkent", "Toshkent", "Uzb"] * 5,
    'Description': [
        "Avtomobil ishlab chiqarish", "Maishiy texnika", "Qurilish materiallari va derazalar", "IT startaplar markazi", "Oziq-ovqat savdosi",
        "Bank xizmatlari", "Xususiy bank", "Davlat banki", "Mobil aloqa operatori", "Telekommunikatsiya",
        "Sug'urta xizmati", "Investitsion xolding", "Uy-joy qurilishi", "Elita turar joylar", "Sanoat qurilishi",
        "Elektronika do'koni", "Gadjetlar savdosi", "Maishiy texnika kreditga", "Diskaunter supermarket", "Supermarketlar tarmog'i",
        "Ko'p tarmoqli xolding", "Kimyo sanoati", "Oltin qazib olish", "Mis va metallurgiya", "Gaz va neft",
        "Aviatsiya xizmati", "Transport logistikasi", "Sharbatlar ishlab chiqarish", "Kandolat mahsulotlari", "Kitob nashriyoti",
        "Diniy kitoblar", "Onlayn do'kon", "Marketpleys", "To'lov rejasi bilan savdo", "E-commerce",
        "To'lov tizimi", "Fintech xizmati", "Raqamli bank", "Transport xizmati", "Taom yetkazib berish",
        "Taksi xizmati", "Milliy taomlar restorani", "Fast food (tovuq)", "Pitseriya", "Pitsa tarmog'i",
        "Lavash va fastfud", "Tez ovqatlanish", "Fastfud restorani", "Burger va sendvich", "Sushi xizmati"
    ]
}

df_a = pd.DataFrame(data_a)
df_b = pd.DataFrame(data_b)

# Fayllarni saqlash
df_a.to_csv(r'G:\AI\deep_learning\TaskAI\data\dataset_a.csv', index=False)
df_b.to_csv(r'G:\AI\deep_learning\TaskAI\data\dataset_b.csv', index=False)

print("Datasetlar muvaffaqiyatli yaratildi!")