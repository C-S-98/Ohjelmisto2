"""
Jatka edellisen tehtävän ohjelmaa siten,
    että Talo-luokassa on parametriton metodi palohälytys,
    joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""

from Moduuli_10_02_TaloLuokka import Talo

class TaloPalohalytys(Talo):
    def __init__(self, alin_kerros, yli_kerros, hissien_maara):
        super().__init__(alin_kerros, yli_kerros, hissien_maara)

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen!")
        for i, hissi in enumerate(self.hissit):
            print(f"\nHissi {i + 1} palaa pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.alin_kerros)


if __name__ == "__main__":
    talo = TaloPalohalytys(1, 10, 2)
    talo.aja_hissia(0, 5)
    # talo.aja_hissia(1, 8)
    talo.palohalytys()
