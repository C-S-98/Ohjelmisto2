"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
    pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja,
    joka saa parametreinaan nimen,
    kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
Luokassa on seuraavat metodit:
    - tunti_kuluu,
        joka toteuttaa aiemmassa autokilpailutehtävässä
            mainitut tunnin välein tehtävät toimenpiteet
            eli arpoo kunkin auton nopeuden muutoksen
            ja kutsuu kullekin autolle kulje-metodia.
    - tulosta_tilanne,
        joka tulostaa kaikkien autojen sen hetkiset tiedot
            selkeäksi taulukoksi muotoiltuna.
    - kilpailu_ohi,
        joka palauttaa True,
        jos jokin autoista on maalissa
        eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
        Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma,
    joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
    Luotavalle kilpailulle annetaan kymmenen auton
        lista samaan tapaan kuin aiemmassa tehtävässä.
    Pääohjelma simuloi kilpailun etenemistä kutsumalla
        toistorakenteessa tunti_kuluu-metodia,
        jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
        onko kilpailu ohi.
    Ajantasainen tilanne tulostetaan tulosta
        tilanne-metodin avulla kymmenen tunnin välein
        sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
"""

import random

class Auto:
    def __init__(self, nimi, huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

    def muuta_nopeutta(self):
        self.nopeus += random.randint(-10, 50)
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.muuta_nopeutta()
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.nimi}")
        print(f"Pituus: {self.pituus_km} km")
        print("Auto | Matka (km) | Nopeus (km/h)")
        print("-" * 30)
        for auto in self.autot:
            print(f"{auto.nimi} | {auto.matka} km | {auto.nopeus} km/h")
        print("-" * 30)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False

def main():
    # 创建10辆车（假设每辆车的名字和最高速度不同）
    autot = [
        Auto("Auto1", 80),
        Auto("Auto2", 90),
        Auto("Auto3", 100),
        Auto("Auto4", 110),
        Auto("Auto5", 115),
        Auto("Auto6", 120),
        Auto("Auto7", 125),
        Auto("Auto8", 130),
        Auto("Auto9", 135),
        Auto("Auto10", 140)
    ]

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        tunti += 1
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()
