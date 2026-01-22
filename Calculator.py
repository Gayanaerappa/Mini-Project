while True:
    print("----\n CALCULATOR----")
    print("1. Add")
    print("2. Subtraction")
    print("3.Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter the choice:")
    if choice == "5":
        print("Exit")    
        break
    elif choice not in["1","2","3","4"]:
         print("Invaild Output")
         continue
    a = int(input("Enter the first number:"))    
    b = int(input("Enter the Second  number:")) 
    if choice == "1":
        print( "Result" , a+b)  
    elif choice =="2":
           print( "Result" , a-b)
    elif choice =="3":
           print( "Result" , a*b) 
    elif choice =="4":
        if b ==0 or a==0:
            print("Cannot divide by Zero!")
        else:     
            print( "Result" , a/b)               

      

    
