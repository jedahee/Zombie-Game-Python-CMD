# python 3.7.1
import random

tipos_enemigos = ["ogro", "zombie", "trasgo"]
lista_mun = [2, 3, 4, 5]
campo_enemigo = []
pos_ene = 70


def menu():
    print(""" 
    ========
      MENU
    ========
    1) JUGAR
    2) REGLAS
    3) SALIR
    """)


class arma():
    nombre = "Pistola"
    dano = 10
    municion = 10
    nivel = 0
    subir_nivel = 35


class me():
    vida = 100
    dinero = 0
    posible = 100
    probabilidad = 50


class ogro():
    nombre = "Ogro"
    vida = 20
    dinero = 35
    dano = 7


class zombie():
    nombre = "Zombie"
    vida = 15
    dinero = 25
    dano = 5


class trasgo():
    nombre = "Trasgo"
    vida = 10
    dinero = 10
    dano = 2


menu()
me = me()
arma = arma()
opc = str(input("--> "))

if opc == "1":
    contador = 0
    while me.vida >= 1:
        if random.randint(0, 100) <= pos_ene:
            generar_enemigo = random.choice(tipos_enemigos)
            if generar_enemigo == "ogro":
                campo_enemigo.append("Ogro")
                campo_enemigo[contador] = ogro()
                contador += 1
                print("HA APARECIDO UN OGRO\n")
            elif generar_enemigo == "zombie":
                campo_enemigo.append("Zombie")
                campo_enemigo[contador] = zombie()
                contador += 1
                print("HA APARECIDO UN ZOMBIE\n")
            elif generar_enemigo == "trasgo":
                campo_enemigo.append("Trasgo")
                campo_enemigo[contador] = trasgo()
                contador += 1
                print("HA APARECIDO UN TRASGO\n")
        print("""Que quieres hacer...
        1) Atacar
        2) Buscar municion
        """)
        opc2 = input(">> ")
        if opc2 == "1":
            if len(campo_enemigo) > 0:

                for i in range(len(campo_enemigo)):
                    print("[", i + 1, "]", campo_enemigo[i].nombre, "(", campo_enemigo[i].vida, ")")

            else:
                print("NO HAY ENEMIGOS")

            if len(campo_enemigo) > 0:
                print("A que enemigo quieres atacar...")
                opc3 = int(input(">> "))
                arma.municion -= 1
                campo_enemigo[opc3 - 1].vida -= arma.dano

                if campo_enemigo[opc3 - 1].vida <= 0:
                    me.dinero += campo_enemigo[opc3 - 1].dinero
                    campo_enemigo.pop(opc3 - 1)
                    contador -= 1

            print(""" 
            ===========================
            |       INFORMACIÓN       |     
            ===========================
            """)
            print("--TU--")
            print("TU VIDA:", me.vida)
            print("TU DINERO:", me.dinero)
            print("\n--TU ARMA--")
            print("TU ARMA:", arma.nombre)
            print("DAÑO DE TU ARMA:", arma.dano)
            print("MUNICIÓN DE TU ARMA:", arma.municion)
            print("TU NIVEL DE ARMA:", arma.nivel)
            print("DINERO NECESARIO PARA SUBIR DE NIVEL:", arma.subir_nivel)
            print("\n")

            if me.dinero >= arma.subir_nivel:
                print("¿Quieres subir el arma de nivel? (s/n)")
                opc4 = str(input(">> "))
                if opc4.lower() == "n" or opc4.lower() == "no":
                    pass
                elif opc4.lower() == "s" or opc4.lower() == "si":
                    me.dinero -= arma.subir_nivel
                    arma.nivel += 1
                    arma.dano += 2
                    arma.subir_nivel += 15

                    if arma.nivel == 3:
                        print("TU ARMA SE HA CONVERTIDO EN UN SUBFUSIL")
                        arma.dano += 5
                        arma.nombre = "Subfusil"
                    elif arma.nivel == 7:
                        print("TU ARMA SE HA CONVERTIDO EN UNA ESCOPETA")
                        arma.dano += 8
                        arma.nombre = "Escopeta"
        elif opc2 == "2":

            if random.randint(0, me.posible) <= me.probabilidad:
                cuanta_mun = random.choice(lista_mun)
                arma.municion += cuanta_mun
                print("HAS ENCONTRADO", cuanta_mun, "BALAS\n")
            else:
                print("NO HAS ENCONTRADO NADA\n")

        print("------------TURNO ENEMIGO------------")
        for i in range(len(campo_enemigo)):
            me.vida -= campo_enemigo[i].dano
            print(campo_enemigo[i].nombre, "te ha atacado\n")
    if me.vida <= 0:
        print("PERDISTE!!")



elif opc == "2":
    print("""
    1) Empiezas con una pistola
    2) Se genera 1 enemigo por ronda
    3) Puedes ganar dinero matando enemigos
    4) Con el dinero puedes subir de nivel tu arma
    5) Cuando tu arma sea nivel 3 se convierte en un subfusil y a nivel 7 tu arma se convierte en una escopeta
    6) Tienes 100 de vida
    7) Existen 3 tipos de enemigos
    8) ogro, zombie, trasgo(ordenado de mayor a menor dificultad)
    9) ogro da 35 monedas, zombie da 25 monedas, trasgo da 10 monedas
    10) ogro tiene 20 de vida, zombie tiene 15 de vida, trasgo tiene 10 de vida
    11) ogro quita 7 de vida, zombie quita 5 de vida, y trasgo quita 2 de vida

    """)