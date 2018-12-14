

q1check = False
correct = int(0)


print("what is 1+1?")
print("1) 11")
print("2) 2")
print("3) window")
print("4) 3")


while q1check == False:
    try:
        q1answer = int(input("input 1, 2, 3 or 4 as your answer  "))
        if q1answer == 2:
            correct += 1
            q1check = True
        elif 0 < q1answer < 5:
            q1check = True
        else:
            print("you input a unaceaptable option that does not exist as one of the 4 answer listed")

    except ValueError:
        print("you inputted a letter. We do not aceapt letter" )
            
        
                   

    
    
    
