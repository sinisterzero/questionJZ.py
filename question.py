

q1check = False
correct = int(0)

#question one
print("what is 1+1?")
# 4 answers option
print("1) 11")
print("2) 2")
print("3) window")
print("4) 3")

#loop for question 1
while q1check == False:
    try:
        q1answer = int(input("input 1, 2, 3 or 4 as your answer  "))
        #check if answer correct
        if q1answer == 2:
            correct += 1
            q1check = True
        #check if answer is acceatpable
        elif 0 < q1answer < 5:
            q1check = True
        #check if user enter a  unaceatpable number
        else:
            print("you input a unaceaptable option that does not exist as one of the 4 answer listed")

    
    #check if user putted a string or float 
    except ValueError:
        print("you inputted a letter. We do not aceapt letter" )
#print how many question they got correct
print("you got", correct , "correct")
            
        
                   

    
    
    
