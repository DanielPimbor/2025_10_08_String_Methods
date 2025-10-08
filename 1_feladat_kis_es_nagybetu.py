"""1️⃣ Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).
"""

felhasznalonev = input(str('Adj meg egy felhasználónevet.'))

nagybetus = felhasznalonev.upper()

print(f'Nagybetűs verzió:{nagybetus}')

kisbetus = felhasznalonev.lower()

print(f'Kisbetűs verzió:{kisbetus}')

elsonagy = felhasznalonev.capitalize()

print(f'"Első betű nagy" verzió:{elsonagy}')