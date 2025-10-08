"""3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó."""

szoveg = input('Küldj be egy pythonnal kapcsolatos szöveget. ')

szoszam = szoveg.count('Python')

print(f'A Python szó ennyiszer van benne: {szoszam}')