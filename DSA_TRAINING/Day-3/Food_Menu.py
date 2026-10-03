pizza = 100 
burger = 50
coldrink = 20
val1 = int(input('Enter the number of pizzas bought :'))
val2 = int(input('Enter the number of burgers bought :'))
val3 = int(input('Enter the number of coldrinks bought :'))
pizza_total = pizza*val1
burger_total = burger*val2
coldrink_total = coldrink*val3
print('------------------------------------------------------')
print('Bill Detais : ')
print('Total Price of Pizza :',pizza_total)
print('Total Price of Burger :',burger_total)
print('Total Price of Coldrink :', coldrink_total)
print('Total Bill Amount :',pizza_total + burger_total + coldrink_total)
print('------------------------------------------------------') 