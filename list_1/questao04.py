""" 4) Faca um programa que calcule o aumento de um salario. 
#Ele deve solicitar o valor do salario e a porcentagem do aumento. 
#Exiba o valor do aumento e do novo salario."""


userSalary = input("Insert your salary: ")
salary = float(userSalary)
userPercent = input("Insert percent of Increase ")
percent = float(userPercent)/100 + 1
#print percent
finalSalary = salary * percent
print "Your salary now is $", finalSalary



