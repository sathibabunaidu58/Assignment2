def Increment():
    result = ''
    number = ''
    i = len('ITEMSUB000')-1
    while i>0:
        c= 'ITEMSUB000'[i]
        if not c.isdigit():
            break
        number = c+ number
        i-=1
    number = int(number)
    number+=1
    result += 'ITEMSUB000'[0:i+1]
    if number<10:
        result+='00'
    elif 10<number<100:
        result+='0'
    else:
        result+=''
    result +=str(number)
    yield result



s=Increment()

print(next(s))
print() 

    

    

