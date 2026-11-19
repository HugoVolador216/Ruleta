import random

Rueda = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0]

def girar_rueda(Rueda):
    return random.choice(Rueda)

fichas_mesa = {
    'Jugador' : input('como te llamas?: '),
    'Fichas' : int(input('¿cual es tu stock?: '))
}

while True:
    # 1. Revisando si el jugador tiene fichas
    if fichas_mesa['Fichas'] <= 0:
        print('no te quedan más fichas')
        break
    
    # 2. Resultado de la rueda y su color EN CADA RONDA
    Resultado = 0
    if Resultado == 0:
        Resultado_color = '3'
    elif (Resultado % 2) == 0:
        Resultado_color = '2'
    else:
        Resultado_color = '1'
    
    # 3. Pedimos apuesta
    apuesta_jugador = int(input(f'\n{fichas_mesa["Jugador"]} tiene un stock de {fichas_mesa["Fichas"]}, ¿Cual es tu apuesta? (0 para salir): '))
    
    if apuesta_jugador > fichas_mesa["Fichas"]:
        print("No tienes suficientes fichas para esa apuesta.")
        continue
    
    if apuesta_jugador == 0:
        print(f'Te retiras con {fichas_mesa["Fichas"]} fichas.')
        break
    elif type(apuesta_jugador) == float:
        print('introduce numeros enteros')
    
    mesa_ruleta = input("¿Qué quieres apostar? (1: Número exacto / 2: Color): ")

    # 4. Comprobamos si gana o pierde
    match mesa_ruleta:
        case '1':
            apuesta = int(input(f'selecciona un numero del {min(Rueda)} al {max(Rueda)}: '))
            print('Girando la ruleta...')
            if Resultado == apuesta:
                if Resultado == 0:
                    print(f'ha salido el {Resultado}')
                    ganado = apuesta_jugador * 18
                    print(f'¡Has ganado {ganado} fichas!')
                    fichas_mesa['Fichas'] += ganado
                else:                   
                    print(f'ha salido el {Resultado}')
                    ganado = apuesta_jugador * 9
                    print(f'¡Has ganado {ganado} fichas!')
                    fichas_mesa['Fichas'] += ganado
            else:
                fichas_mesa['Fichas'] -= apuesta_jugador
                print(f'ha salido el {Resultado}')
                print(f'has perdido {apuesta_jugador} fichas')
                
        case '2':
            Apuesta_color = input('elige un color (1: Rojo (impar), 2: Negro(par) o 3: Verde(cero)): ')
            print('Girando la ruleta...')
            if Apuesta_color == Resultado_color:
                print(f'ha salido el {Resultado}')
                if Resultado_color == '3':
                    Ganado_por_color = apuesta_jugador * 10
                else:
                    Ganado_por_color = apuesta_jugador * 2
                print(f'¡Has ganado {Ganado_por_color} fichas!')
                fichas_mesa['Fichas'] += Ganado_por_color
            else:
                fichas_mesa['Fichas'] -= apuesta_jugador
                print(f'ha salido el {Resultado}')
                print(f'has perdido {apuesta_jugador} fichas')
                
        case _:
            print('opción no válida')