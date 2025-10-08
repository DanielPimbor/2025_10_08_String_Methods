"""4️⃣ Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma."""

rendeles = input('Add meg az ételrendelésedet és kicserélem az almákat körtére vagy a körtéket almára.\n')

# if rendeles.count("alma") > 0 or rendeles.count("almás") > 0 or rendeles.count("almával") > 0:
    
#     valtozott = rendeles.replace("alma", "körte").replace( "almás", "körtés").replace("almával", "körtével")

#     print(f'Megváltoztatott ételrendelés:\n {valtozott}')


# elif rendeles.count("körte") > 0 or rendeles.count("körtés") > 0 or rendeles.count("körtével") > 0:
    
#     valtozott = rendeles.replace("körtével", "almával").replace("körtés", "almás").replace("körte", "alma")

#     print(f'Megváltoztatott ételrendelés:\n {valtozott}')


# else:
#     print('Nincs a rendelésedben se alma se körte.')

if "alma" in  rendeles:
    
    valtozott = rendeles.replace("alma", "körte")

    print(f'Megváltoztatott ételrendelés:\n {valtozott}')

elif "körte" in rendeles:
    
    valtozott = rendeles.replace("körte", "alma")

    print(f'Megváltoztatott ételrendelés:\n {valtozott}')