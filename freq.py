lst=input('Enter a sentence:').split()
over=[]
for i in lst:
    if i not in over:
        over.append(i)
        print(i,':',lst.count(i))
        #continue
    #else:
        
    
