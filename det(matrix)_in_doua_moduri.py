def traditional_det(matrice):
    #Verificăm dacă matricea este pătratică
    if len(matrice) != len(matrice[0]):
        raise ValueError("Matricea trebuie să fie pătratică")

    #Cazul pentru matrice de 1x1
    if len(matrice) == 1:
        return matrice[0][0]

    #Cazul pentru matrice de 2x2
    if len(matrice) == 2:
        return matrice[0][0] * matrice[1][1] - matrice[0][1] * matrice[1][0]

    #Cazul recursiv pentru matrici mai mari sau egale de 3x3
    det = 0
    for j in range(len(matrice)):
        semn = (-1) ** j
        sub_matrice = [linie[:j] + linie[j+1:] for linie in matrice[1:]]
        sub_det = traditional_det(sub_matrice)
        det += semn * matrice[0][j] * sub_det

    return det

def gaussian_det(matrice):
    #Verificăm dacă matricea este pătratică
    if len(matrice) != len(matrice[0]):
        raise ValueError("Matricea trebuie să fie pătratică")

    #Cazul pentru matrice de 1x1
    if len(matrice) == 1:
        return matrice[0][0]

    #Copiem matricea inițială pentru a nu o modifica
    A = [linie[:] for linie in matrice]

    #Începem eliminarea prin metoda Gauss
    n = len(A)
    factori_de_esalonare = []
    nr_schimbari_linie = 0  # keep track of number of row swaps
    for i in range(n):
        #Verificăm dacă pivotul este 0
        if A[i][i] == 0:
            #Găsim un pivot diferit de 0 pe aceeași coloană
            for j in range(i+1, n):
                if A[j][i] != 0:
                    #Interschimbăm liniile i și j
                    A[i], A[j] = A[j], A[i]
                    nr_schimbari_linie += 1  #creștem numărul interschimbărilor de linie
                    break
            else:
                #Dacă nu găsim niciun pivot diferit de 0
                return 0

        # Se împarte rândul pivot cu elementul pivot pentru a-l face egal cu 1
        factor = A[i][i]
        factori_de_esalonare.append(factor)
        for k in range(i, n):
            A[i][k] /= factor

        #Se elimină cea de-a i-a coloană de sub cel de-al i-lea rând
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    #Calculați determinantul din factorii de eșalonare utilizați în eliminare
    det = (-1) ** nr_schimbari_linie
    for factor in factori_de_esalonare:
        det *= factor

    return round(det)

#Implementare
'''
print("Matrice:")
for linie in matrice:
    print(*linie)
'''
#Verificarea prin afișarea a 33 de rezultate pentru matrice luate din fișierul date.in
"""
with open("date.in") as fisier:
    for linie in fisier:
        matrice = eval(linie)
        print("Matrice:", matrice)
        print("Determinant calculat prin metoda Tradițională:", traditional_det(matrice))
        print("Determinant calculat prin metoda Gauss:", gaussian_det(matrice))
        print()
"""
import time
import random
T = []
G = []
x = int(input("Dați un număr natural între 1 și 100, inclusiv: "))
for i in range(100):
    n = random.randint(1, x)  #Generează o valoare aleatorie pentru n între 1 și 5
    #Testăm timpul de execuție pentru fiecare funcție
    matrice = [[random.randint(1, 10) for j in range(n)] for k in range(n)]
    print("Matrice:", matrice)
    timp_inceput_t = time.time()
    rez_t = traditional_det(matrice)
    print("Determinant calculat prin metoda Tradițională:", rez_t)
    timp_final_t = time.time()
    timp_traditional = timp_final_t - timp_inceput_t
    timp_inceput_g = time.time()
    rez_g = gaussian_det(matrice)
    print("Determinant calculat prin metoda Gauss:", rez_g)
    timp_final_g = time.time()
    timp_gauss = timp_final_g - timp_inceput_g
    print()

    if timp_traditional!=0: T.append(timp_traditional)
    if timp_gauss!=0: G.append(timp_gauss)

#Calculul procentajelor legate de performanță
import statistics
try: T_T = statistics.mean(T)
except: print("Nu există date suficiente pentru T_T")
try: T_G = statistics.mean(G)
except: print("Nu există date suficiente pentru T_G")
print('\n')
if T_T != 0 and T_T >= T_G:
    P1 = (T_T - T_G) / T_T * 100
    print(f"Funcția gaussian_det este cu {P1:.2f}% mai rapidă decât funcția traditional_det.")
elif T_G != 0:
    P2 = (T_G - T_T) / T_G * 100
    print(f"Funcția traditional_det este cu {P2:.2f}% mai rapidă decât funcția gaussian_det.")
else:
    print("Timpul de execuție e prea mic pentru a deduce un răspuns.")