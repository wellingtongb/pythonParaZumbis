"""10) Escreva um programa para calcular a reducao do tempo de vida
de um fumante. Pergunte a quantidade de cigarros fumados por dia 
e quantos anos ele ja fumou. Considere que um fumante perde 
10 minutos de vida a cada cigarro, calcule quantos dias de vida 
um fumante perdera. Exiba o total de dias."""

losing = 10

userCigars = input('how many cigar do you smoke everyday?')
cigars = float(userCigars)
userSmokingTime = input('how many years did you smoke?')
smokingTime = float(userSmokingTime)

daysSmoking = smokingTime * 365
amountSmokedTime = cigars * losing

daysLose = daysSmoking /(amountSmokedTime/1.44)	#was necessary to convert to days

#print amountSmokedTime
#print daysSmoking
print daysLose






