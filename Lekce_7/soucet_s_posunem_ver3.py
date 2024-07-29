### Lekce 7 - Domácí úkol-1
###
### Autor: Marcel Breda
"""
   Zadání : Soucet s posunem
      dostanu dve pole
      jsou stejne delky?
      dostanu posun
      ke kazdemu elementu z prvniho pole s indexem i, prictu element z druheho pole s indexem i + posun
      vratim sumu vysledku.
   Ukazka: 
      s_1=[1, 2, 3, 4, 5, 6, 7, 8], 
      s_2=[-1, -2, -3, -4, -5, -6, -7, -8], 
      posun=3
      s_2_posunuty=[-4, -5, -6, -7, -8, -1, -2, -3]
      Sumy paru: [-3, -3, -3, -3, -3, 5, 5, 5]
      suma=0
"""
### Obsluzne funkce ###

def zkrat_seznam(seznam, delka):
     """
     Zkrátí seznam na vstupu o danou délku.

     Parametry:
        seznam: vstupní seznam
        delka: délka zkrácení

     Returns:
        vystupni_seznam: zkracena podoba seznamu
     """
     vystupni_seznam = seznam[:(delka)]
     return vystupni_seznam

def posun_seznam(seznam, posun):
     """
     Posune seznam na vstupu o daný počet kroků.

     Parametry:
        seznam: vstupní seznam
        posun: počet kroků

     Returns:
        posunuty_seznam: posunutá podoba seznamu
     """
     posunuty_seznam = seznam[posun:] + seznam[:posun]
     return posunuty_seznam

def uprav_seznamy(seznam1, seznam2,p):
     """
     Upraví seznamy na vstupu na stejnou délku a druhý seznam posune o daný počet kroků.

     Parametry:
        seznam1: vstupní seznam 1
        seznam2: vstupní seznam 2
        p: počet kroků posunu

     Returns:
        s_1_kor
        , s_2_posun: srovnané a posunuté podoby seznamu
     """     
     d_1 = len(seznam1)
     d_2 = len(seznam2)
     if d_1>d_2:
          s_1_kor = zkrat_seznam(seznam1, d_2)
          s_2_kor = seznam2
     elif d_2>d_1:
          s_2_kor = zkrat_seznam(seznam2, d_1)
          s_1_kor = seznam1
     else:
          s_1_kor = seznam1
          s_2_kor = seznam2
     s_2_posun = posun_seznam(s_2_kor, p)
     return s_1_kor,s_2_posun

def secti_seznam(seznam):
     """
     Sečte všechny prvky vstupního seznamu a vrací hodnotu součtu.

     Parametry:
        seznam: vstupní seznam 

     Returns:
        s_soucet: Hodnota součtu všech prvků seznamu
     """     
     s_soucet = 0
     for a in seznam:
          s_soucet += a
     return s_soucet

### MAIN ###
if __name__ == "__main__":
   # Zadani, Seznamy s hodnotami
   s_1=[1, 2, 3, 4, 5, 6, 7, 8]
   s_2=[-1, -2, -3, -4, -5, -6, -7, -8, 1, 2, 3, 4, 5] 
   posun=3
   print(f"\nSeznamy \n  {s_1=} \n  {s_2=}")
   print(f"  {posun=}")

   # 240728-MX: Následující dva kroky, tj. volání uprav_seznamy a sečtení prvků se dají vytahnout mimo __main__

   # upravy a posuny
   s_1_k, s_2_k = uprav_seznamy(s_1,s_2,posun)
   print(f"\nSeznamy po uprave \n  {s_1_k=} \n  {s_2_k=}")

   # Sečtení prvků
   s_soucet = [a + b for a, b in zip(s_1_k, s_2_k)]
   print(f"Součet prvků seznamů: \n  {s_soucet=}")

   s_soucet_seznamu = secti_seznam(s_soucet)
   print(f"Součet souctu prvků: \n  {s_soucet_seznamu=}")
else:
    print("Nahrávání modulu...")