""" 6) Calcule o tempo de uma viagem de carro. 
Pergunte a distancia a percorrer e a velocidade media esperada
 para a viagem."""


userDist = input("Insert travel distance: ")
dist = float(userDist)
userSpeed = input("Average speed? ")
speed = float(userSpeed)
time = dist/speed

print "To arrive in your destine you will take " + str(time) +" hours."




