"""2️⃣ Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll. Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez."""

uzenet = input('Írj egy üzenetet. ')

karakterszam = uzenet.__len__()

print(f'Az üzenet hossza {karakterszam}.')