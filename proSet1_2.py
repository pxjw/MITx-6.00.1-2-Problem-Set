s = raw_input("input a String:")

str1 = "bob"

def searchs(s,str1):
    i = 0
    count = 0
    while(i<len(s)-len(str1)+1):
        if(str1 == s[i:i+3]):
            count = count+1
        i+=1
    return count

print ("Number of times bob occurs is:"+str(searchs(s,str1)))
        
