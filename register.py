import bcrypt      # Para hashear las contraseñas.
import getpass     # Para que no muestre la contraseña por consola.

# Si el archivo existe, simplemente añade una nueva línea.
# De no ser así, crea el archivo y escribe en el.
def userGetReg(userName,userPasswd):
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
            
# Muestra por pantalla el contenido del archivo.
def readData():
    with open('userData.dat','r') as userData:
        print('\nUserName,Hash:\n\n'+userData.read())
        userData.close()

# Llama a las funciones.
if __name__ == "__main__":
    userName = input('Introduce nombre de usuario: ')
    userPasswd = getpass.getpass('Introduce una contraseña: ')
    userGetReg(userName,userPasswd)
    print(readData())
