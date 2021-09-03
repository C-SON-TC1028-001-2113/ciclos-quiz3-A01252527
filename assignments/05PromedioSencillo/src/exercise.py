def main():
    #escribe tu código abajo de esta línea
    suma = 0
    numero = int(input(""))
    for cont in range(1,numero+1):
        nn = float(input(""))
        
        suma += nn 
    promedio = suma / numero
    print(promedio)
if __name__=='__main__':
    main()
