print ("**************************************")
print ("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type \"quit\" **")
print ("**************************************")


print("Appetizers")
print("----------")
print("Wings")
print("Cookies")
print("Spring Rolls")

print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")

print("Desserts")
print("--------")
print("Ice Cream")
print("Cake")
print("Pie")

print("Drinks")
print("------")
print("Coffee")
print("Tea")
print("Unicorn Tears")

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

quit = True
count=0
arr=[] 
while(quit):
 order=input()
 if(order=="quit"):
  quit=False
  break
 #count+=1
 
 arr.append(order)
 if len(arr) > 1 and arr[-1] != arr[-2]:
    count = 1
 else:
    count += 1
 print(f"** {count} order of {order} has been added to your meal **")
 
  
 

 
