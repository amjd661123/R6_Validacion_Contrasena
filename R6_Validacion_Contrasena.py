while True:
    try:
        contraseña = input("Ingrese una contraseña: ")
        int(contraseña[0])
        break
    except ValueError:
        print("La contraseña debe empesar con un número")
      
copia = input("Ingresa la contraseña nuevamente: ")

if copia == contraseña:
        print("Contraseña correcta")
else: 
        errores = 1
        while errores < 3:
            print("Las contraseñas no coinciden")
            copia = input("Ingresa la contraseña nuevamente: ")
            if copia == contraseña:
                print("Contraseña correcta")
                break
            else: 
                errores = errores + 1
                if errores == 3:
                    print("Se ingreso tres veces la contraseña incorrecta.")

print("Fin del programa")


