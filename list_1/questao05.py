""" 5) Solicite o preco de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preco a pagar."""


userPrice = input("Insert product price: ")
price = float(userPrice)
userDescount = input("Insert savings amount ")
descount = float(userDescount)/100
#print descount
descountValue = price * descount
finalPrice = price - descountValue

print "Descount value is $", descountValue
print "Product final price is $", finalPrice



