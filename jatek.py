# Játékos változók
hp = 100
max_hp = 100
gold = 0
days = 0
dmg = 10
pancel = 1
# Ellenség változók
goblin_dmg = 3
sarkany_hp = 1000
sarkany_dmg = 5
# Név
name = input("Adj meg egy karakter nevet: ")
name = name.strip().title()
kisbetus = name.lower()
if kisbetus == "naplopó jános" or kisbetus == "naplopo janos":
    hp = hp + 50
    max_hp = max_hp + 50
    gold = gold + 25
    print("Tetszik a neved, kapsz 50 extra hp-t és 25 aranyat!")
# Tutorial
print("Szia", name)
print("Story: Te vagy", name + ", Dandória lovagja, akinek meg kell védenie Dandória városát a mérges sárkány elől.")
print("Tutorial:")
print("- Minden nap 2 választási lehetőséget kapsz hogy mit csinálhatsz.")
print("- Balra vagy jobbra, melyik lesz?")
print("- Minden 3. napon jön egy kereskedő, akitől vehetsz dolgokat.")
print("- A 10. napon jön a sárkány, neki 1000 hp-ja van.")
print("- Jó játékot!")

# 1. nap: goblin vagy arany
if hp > 0:
    days = days + 1
    print("1. nap")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Elmentél buta goblinokat ölni a dandus folyó mentén.")
        goblin_hp = 30
        utesek = 0
        while goblin_hp > 0:
            goblin_hp = goblin_hp - dmg
            utesek = utesek + 1
        sebzes = round(utesek * goblin_dmg / pancel)
        hp = hp - sebzes
        gold = gold + 25
        print("Legyőzted a goblint", utesek, "ütéssel!")
        print("Kaptál 25 aranyat, de veszítettél", sebzes, "hp-t!")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Találtál 10 aranyat!")
        gold = gold + 10
    else:
        print("Nem követted a szabályokat, egész nap egy helyben álltál.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 2. nap: kard vagy pajzs
if hp > 0:
    days = days + 1
    print("2. nap")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Az utadon találtál egy kardot!")
        print("Felment a dmg-ed 10-zel!")
        dmg = dmg + 10
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Találtál az úton egy pajzsot!")
        print("Ez megvéd a kapott dmg felétől.")
        pancel = 2
    else:
        print("Egy helyben álltál egész nap.")
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 3. nap: kereskedő
if hp > 0:
    days = days + 1
    print("3. nap")
    print("Találkoztál egy kereskedővel.")
    print("Kereskedő: Szia! Mit szeretnél venni?")
    vasarlas = 0
    while vasarlas != 4:
        print("Aranyad:", gold, "| hp:", hp, "/", max_hp, "| dmg:", dmg, "| páncél:", pancel)
        print("1 - Jobb kard (+25 dmg)  30 arany")
        print("2 - Jobb páncél (+0.5 páncél)  30 arany")
        print("3 - Gyógyital (+40 hp)  15 arany")
        print("4 - Továbbállok")
        vasarlas = int(input("Mit szeretnél venni? "))
        if vasarlas == 1:
            if gold >= 30:
                gold = gold - 30
                dmg = dmg + 25
                print("Megvetted a kardot! A dmg-ed most", dmg)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 2:
            if gold >= 30:
                gold = gold - 30
                pancel = pancel + 0.5
                print("Megvetted a páncélt! A páncélod most", pancel)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 3:
            if gold >= 15:
                gold = gold - 15
                hp = hp + 40
                if hp > max_hp:
                    hp = max_hp
                print("Megittad a gyógyitalt! A hp-d most", hp)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 4:
            print("Kereskedő: Szia!")
        else:
            print("Kereskedő: Ilyen nincs.")
    print(days, ". napod ért véget.")
# 4. nap: mocsár vagy forrás
if hp > 0:
    days = days + 1
    print("")
    print("4. nap")
    print("Balra egy mocsár van, lehet hogy van benne kincs.")
    print("Jobbra egy forrás van.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Találtál egy ládát, 40 arany volt benne!")
        print("De megcsípett egy kígyó és megmérgezett!")
        gold = gold + 40
        for kor in range(3, 0, -1):
            mereg = kor * 4
            hp = hp - mereg
            if hp < 0:
                hp = 0
            print("A méreg sebzett:", mereg, "-> hp-d:", hp)
        print("Elmúlt a méreg.")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Ittál a forrásból, kaptál 30 hp-t!")
        hp = hp + 30
        if hp > max_hp:
            hp = max_hp
    else:
        print("Egy helyben álltál egész nap.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")
