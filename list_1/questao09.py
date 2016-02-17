"""9) Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado pelo usuario, assim como a quantidade de 
dias pelos quais o carro foi alugado. Calcule o preco a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado."""

diary = 60
travelledKm = 0.15
userKm = input("How many km did youo travelled? ")
km = float(userKm)
userDays = input("How many days did you stay with this car?")
days = float(userDays)
rentaPrice = (days * diary) + (km * travelledKm)
print "the final rental price is $",rentaPrice





