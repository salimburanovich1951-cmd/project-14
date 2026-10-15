#phone = {"brand": "Samsung","model": "Galaxy A55","color": "Black","price": 400,"memory": "256GB","ram": "8GB","battery": "5000mAh","year": 2024}
#for key in phone.items():
#    print(key)
#print("Phone haqida ma'lumot:")
#print("Brand -", phone["brand"])
#print("Model -", phone["model"])
#print("Color -", phone["color"])
#print("Price -", phone["price"])
#print("Memory -", phone["memory"])
#print("Year -", phone["year"])
car={"modeli_mashina":'Chevrolet','resumi': 'Diyor','rangi':'oq','probegi':230}
for i in car:
    print(i)
davlatlar = {"AQSH": "Washington ","Italiya": "Rim","Malayziya": "Kuala-Lumpur","O'zbekiston": "Toshkent","Qirg'iziston": "Bishkek","Qozog'iston": "Nursulton","Rossiya": "Moskva","Singapur": "Singapur","Tojikiston": "Dushanbe"}
print("Dunyo davlatlari:")
for davlat in sorted(davlatlar.keys()):
    print(davlat.upper())
print("Davlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)
    taomlar = {"Ali": "osh","Vali": "manti","Gulnoza": "somsa","Hasan": "lag'mon","Husan": "shashlik"}

    for ism, taom in taomlar.items():
        print(ism, "ning sevimli taomi", taom)
phone = {"brand": "Samsung","model": "Galaxy A55","color": "Black","price": 400,"memory": "256GB","ram": "8GB","battery": "5000mAh","year": 2024}
soz=input("So`z kiriting:")
if soz in phone:
    print(phone[soz])
else:
    print("Bunday son mavjud emas")