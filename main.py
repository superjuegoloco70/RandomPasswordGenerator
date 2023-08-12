#RandomPasswordGenerator
import random

chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!#$%&_"
password = ""
a = int(input("Elige la longitud de la contraseña: "))
for i in range (a):
    password = password + random.choice(chars)
print(password)