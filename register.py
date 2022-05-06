import bcrypt      # Para hashear las contraseñas.
import getpass     # Para que no muestre la contraseña por consola.
import os          # Se usa para poder limpiar la terminal.

# Si el archivo existe, simplemente añade una nueva línea.
# De no ser así, crea el archivo y escribe en el.
def userGetReg(userName,userPasswd):
    if len(userName) >= 4 and len(userName) <= 16 and len(userPasswd) >= 8 and len(userPasswd) <= 24:
        password = userPasswd.encode()
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        try:
            with open('userData.dat','a') as userData:
                userData.write(userName + ',' + str(hashedPassword) + '\n')
                userData.close()
        except FileNotFoundError:
            with open('userData.dat','w+') as userData:
                userData.write(userName + ',' + str(hashedPassword) + '\n')
                userData.close()
    else:
        print('\nPuede que el usuario o contraseña esté fuera del rango establecido.\n\nUsuario: Entre 4 y 16 caracteres.\nContraseña: Entre 8 y 24 caracteres.')
    
# Muestra por pantalla el contenido del archivo.
def readData():
    with open('userData.dat','r') as userData:
        print('UserName,Hash:\n\n'+userData.read())

# Llama a las funciones.
if __name__ == "__main__":
    os.system('cls||clear')
    print('\n'+ '='*35 + ' REGISTER ' + '='*35 + '\n')
    userName = input('Introduce nombre de usuario: ')
    userPasswd = getpass.getpass('Introduce una contraseña: ')
    userGetReg(userName,userPasswd)
    os.system('cls||clear')
    print('\n' + '='*34 + ' USERS DATA ' + '='*34 + '\n')
    print(readData())
    input("\nPulsa 'Enter' para continuar...\n")
    os.system('cls||clear')
