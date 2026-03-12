c1,c2,c3,c4,c5,c6,c7=0,0,0,0,0,0,1
s = input("Enter the String: ")
for i in s:
    if i.isalnum():
        if i.isalpha(): 

            if i.isupper(): 
                c1+=1
                if i in "AEIOUaeiou":
                    c3+=1
                   
                else:
                    c4+=1
                    
                
            elif i.islower():
                c2+=1
                if i in "AEIOUaeiou":
                    c3+=1
                   
                else:
                    c4+=1
                    
                

        elif i.isdigit():
             c5+=1
    elif(i==" ") :
        c7+=1        
    else:
         c6+=1

print("No of uppercase:",c1)
print("No of lowercase:",c2)
print("No of vowel:",c3)
print("No of consonant:",c4)
print("No of digit:",c5)
print("No of special character:",c6)
print("No of space:",c7)
print("No of word:",c7+1)