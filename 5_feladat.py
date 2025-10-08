"""5️⃣ Szó elejének/végének ellenőrzése – email ellenőrzés
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e."""

email = input('Email-cím:\n')

gmail = email.endswith("@gmail.com")

if gmail == True:
    print('Gmail-es az email-cím.')

else:
    print('Nem gmail-es az email-cím.')
