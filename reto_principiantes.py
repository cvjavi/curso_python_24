# Estructuras de control
menu = """
        ***********************************
        * MENU PRINCIPAL DE LA APLICACION *  
        ***********************************
        
        Elija la opción del reto que desea ejecutar:
        1000 :  Hello World
        1001 :  Suma Simple
        1002 :  Área Círculo
        1003 :  Suma 2 números
        1004 :  Multiplicación 2 números
        1005 :  Promedio 1
        1006 :  Promedio 2
        1007 :  Diferencia
        1008 :  Salario
        1009 :  Salario con Bonus
        1010 :  Cálculo Simple
        1011 :  Esfera
        1012 :  Área
        1013 :  El Mayor
        1014 :  Consumo
        1015 :  Distancia Entre Dos Puntos
        1016 :  Distancia
        1017 :  Combustible Gastado
        1018 :  Billetes
        1019 :  Conversión del Tiempo
        1020 :  Edad en Días
        1021 :  Billetes y Monedas
        1035 :  Prueba de Selección
        1036 :  Fórmula de Bashkara
        1037 :  Intervalo
        0 :  Salir del programa
"""

bandera = True


while bandera:
    print(menu)
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!")
        break
    
    elif opcion == 1000:
        
        # Ejercicio 1000
        print('Hola Mundo')
        
    elif opcion == 1001:
        
        # Ejercicio 1001
        A = int(input("Ingrese #1 de la suma : \n"))
        B = int(input("Ingrese #2 de la suma : \n"))
        X = A + B
        print(f"X = {X}")
        
    elif opcion == 1002:
        
        # Ejercicio 1002
        pi = 3.14159
        radio = float(input("Ingrese el radio de la circunferencia: \n"))
        area = pi*radio**2
        print(f"A={area:.4f}")
        
    elif opcion == 1003:
        
        # Ejercicio 1003
        A = int(input())
        B = int(input())
        SOMA = A + B
        print(f"SOMA = {SOMA}")
        
    elif opcion == 1004:
        
        # Ejercicio 1004
        A = int(input())
        B = int(input())
        PROD = A*B
        print(f"PROD = {PROD}")
        
    elif opcion == 1005:
        
        # Ejercicio 1005
        A = float(input("Ingrese nota A : \n"))
        B = float(input("Ingrese nota B : \n"))
        peso_A = 3.5
        peso_B = 7.5
        MEDIA =  (A*peso_A + B*peso_B)/(peso_A + peso_B)
        print(f"MEDIA = {MEDIA:.5f}")
        
    elif opcion == 1006:
        
        # Ejercicio 1006
        A = float(input("Ingrese nota A : \n"))
        B = float(input("Ingrese nota B : \n"))
        C = float(input("Ingrese nota C : \n"))
        w_A = 2
        w_B = 3
        w_C = 5
        MEDIA = (A*w_A + B*w_B + C*w_C)/(w_A + w_B + w_C)
        print(f"MEDIA = {MEDIA:.1f}")
        
    elif opcion == 1007:
        
        # Ejercicio 1007
        A = int(input("Ingrese un valor entero A : \n"))
        B = int(input("Ingrese un valor entero B : \n"))
        C = int(input("Ingrese un valor entero C : \n"))
        D = int(input("Ingrese un valor entero D : \n"))
        DIFERENCA = (A * B - C * D)
        print(f"DIFERENCA = {DIFERENCA}")
        
    elif opcion == 1008:
        
        # Ejercicio 1008
        numero = int(input("Ingrese el número del empleado : \n"))
        horas = int(input("Ingrese el número de horas trabajadas en el mes: \n"))
        monto = float(input("Ingrese el monto recibido por hora: \n"))
        salario = horas * monto
        print(f"NUMBER = {numero}")
        print(f"SALARY = U$ {salario:.2f}")
        
    elif opcion == 1009:
        
        # Ejercicio 1009
        nombre_vendedor = str(input("Ingrese el nombre del vendedor : \n"))
        salario_fijo = float(input("Ingrese el salario fijo : \n"))
        ventas_mes = float(input("Ingrese el número total de ventas realizadas en el mes : \n"))
        porcentaje = 0.15
        salario_final = salario_fijo + porcentaje * ventas_mes
        print(f"TOTAL = R$ {salario_final:.2f}")
        
    elif opcion == 1010:
        
        # Ejercicio 1010
        producto_1 = input("Ingrese el código, número de unidades, y precio del producto 1 en el orden correspondiente y separado por un espacio : \n")
        producto_2 = input("Ingrese el código, número de unidades, y precio del producto 2 en el orden correspondiente y separado por un espacio : \n")
        valores_1 = producto_1.split(" ")
        valores_2 = producto_2.split(" ")
        suma_total_p1 = float(valores_1[1]) * float(valores_1[2])
        suma_total_p2 = float(valores_2[1]) * float(valores_2[2])
        suma_final = suma_total_p1 + suma_total_p2
        print(f"VALOR A PAGAR: R$ {suma_final:.2f}") 
        
    elif opcion == 1011:
        
        # Ejercicio 1011
        pi = 3.14159
        R = float(input("Ingrese el radio de la esfera : \n"))
        VOLUME = (4.0 / 3) * pi * R ** 3
        print(f"VOLUME = {VOLUME:.3f}")
        
    elif opcion == 1012:
        
        # Ejercicio 1012
        A, B, C = map(float, input("Ingrese 3 valores A, B, C en el orden correspodiente y separado por un espacio : \n").split())
        area_triangulo = (A * C) / 2
        area_circulo = 3.14159 * C**2
        area_trapecio = ((A + B) * C) / 2
        area_cuadrado = B**2
        area_rectangulo = A * B
        print(f"TRIANGULO: {area_triangulo:.3f}")
        print(f"CIRCULO: {area_circulo:.3f}")
        print(f"TRAPEZIO: {area_trapecio:.3f}")
        print(f"QUADRADO: {area_cuadrado:.3f}")
        print(f"RETANGULO: {area_rectangulo:.3f}")
        
    elif opcion == 1013:
        
        # Ejercicio 1013
        valores = input("Ingrese 3 valores enteros : \n").split()
        a, b, c = map(int, valores)
        MaiorAB = (a + b + abs(a - b)) // 2
        maior = (MaiorAB + c + abs(MaiorAB - c)) // 2
        print(f"{maior} eh o maior")
        
    elif opcion == 1014:
        
        # Ejercicio 1014
        X = int(input("Ingrese la distancia total recorrida en km/h : \n"))
        Y = float(input("Ingrese el total de combustible gastado en litros : \n"))
        consumo = X / Y
        print(f"{consumo:.3f} km/l")
        
    elif opcion == 1015:
        
        # Ejercicio 1015
        x1, y1 = map(float, input("Ingrese las coordenadas del primero punto en formato x y : \n").split())
        x2, y2 = map(float, input("Ingrese las coordenadas del segundo punto en formato x y : \n").split())
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        print(f"{distancia:.4f}")
        
    elif opcion == 1016:    
        
        # Ejercicio 1016
        distancia = int(input("Ingrese la distancia entre los dos autos : \n"))
        tiempo = distancia * 2
        print(f"{tiempo} minutos")
        
    elif opcion == 1017:
        
        # Ejercicio 1017   
        tiempo = int(input("Ingrese el tiempo en horas que duró el viaje : \n"))
        velocidad_media = int(input("Ingrese la velocidad media del viaje en km/h : \n"))
        consumo = 12.0 #km/L
        litros = velocidad_media * tiempo / consumo
        print(f"{litros:.3f}")
        
    elif opcion == 1018:
        
        # Ejercicio 1018
        valor = int(input("Ingrese la cantidad total de dinero : \n"))
        billetes = [100, 50, 20, 10, 5, 2, 1]
        desglose = {}
        for billete in billetes:
            desglose[billete], valor = divmod(valor, billete)
        print(f"{sum(desglose[b] * b for b in billetes)}")
        for billete, cantidad in desglose.items():
            print(f"{cantidad} nota(s) de R$ {billete},00") 
        
    elif opcion == 1019:
        
        # Ejercicio 1019   
        N = int(input("Ingrese la duración del evento en segundos : \n"))
        horas = N // 3600
        minutos = (N % 3600) // 60
        segundos = (N % 3600) % 60
        print(f"{horas}:{minutos}:{segundos}") 
        
    elif opcion == 1020:
        
        # Ejercicio 1020
        N = int(input("Ingrese la edad de la persona en días : \n"))
        anos = N // 365
        meses = (N % 365) // 30
        dias = (N % 365) % 30
        print(f"{anos} ano(s)")
        print(f"{meses} mes(es)")
        print(f"{dias} dia(s)")
        
    elif opcion == 1021:
        
        # Ejercicio 1021
        valor = float(input("Ingrese la cantidad de dinero : \n"))
        valores = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
        centavos = round(valor * 100)
        desglose = {}
        for valor in valores:
            valor_centavos = round(valor * 100)
            desglose[valor], centavos = divmod(centavos, valor_centavos)
        print("NOTAS:")
        for valor in valores[:6]:  
            print(f"{int(desglose[valor])} nota(s) de R$ {valor:.2f}")
        print("MOEDAS:")
        for valor in valores[6:]:  
            print(f"{int(desglose[valor])} moeda(s) de R$ {valor:.2f}")
            
    elif opcion == 1035:
        
        # Ejercicio 1035
        A, B, C, D = map(int, input("Ingrese 4 valores enteros A,B,C,D en el orden correspondiente y separado por un espacio : \n").split())
        if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
            
    elif opcion == 1036:
        
        # Ejercicio 1036
        A, B, C = map(float, input("Ingrese 3 valores separados por un espacio : \n").split())
        discriminante = B**2 - 4*A*C
        if discriminante < 0 or A == 0:
            print("Impossivel calcular")
        else:
            R1 = (-B + discriminante**0.5) / (2*A)
            R2 = (-B - discriminante**0.5) / (2*A)
            print(f"R1 = {R1:.5f}")
            print(f"R2 = {R2:.5f}")  
            
    elif opcion == 1037:   
        
        # Ejercicio 1037  
        numero = float(input("Ingrese un número : \n"))
        if 0 <= numero <= 25:
            intervalo = "Intervalo [0,25]"
        elif 25 < numero <= 50:
            intervalo = "Intervalo (25,50]"
        elif 50 < numero <= 75:
            intervalo = "Intervalo (50,75]"
        elif 75 < numero <= 100:
            intervalo = "Intervalo (75,100]"
        else:
            intervalo = "Fora de intervalo"
        print(intervalo) 
            
    
    else:
        print("La opción seleccionada no es correcta")
        
        




