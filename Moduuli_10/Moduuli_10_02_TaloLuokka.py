"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman
    ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä,
    joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""

from Moduuli_10_01_HissiLuokka import Hissi

class Talo:
    def __init__(self, alin_kerros, yli_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.yli_kerros = yli_kerros
        self.hissit = [Hissi(alin_kerros, yli_kerros) for _ in range(hissien_maara)]

    def aja_hissia(self, hissi_num, kohdekerros):
        if 0 <= hissi_num < len(self.hissit):
            print(f"Ajetaan hissi {hissi_num + 1} kohdekerrokseen {kohdekerros}.")
            self.hissit[hissi_num].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissin numero!")


if __name__ == "__main__":
    talo = Talo(1, 10, 2)
    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 8)
    talo.aja_hissia(0, 1)