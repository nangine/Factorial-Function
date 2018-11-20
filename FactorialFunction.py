def fact (n) :
    if n == 0 :
        return 1
    else :
        return n*fact(n-1)
        
opt = "y"
while opt == "y":
    n = int(input("Insert n =  "))
    print ("Factorial = ",fact(n))
    print ()
    opt = input ("Continue? y/t ")
    print ()
print ("***Done***")
print ()
