def PowersofTwo(num): 
    num = int(num)
    if num < 0:
        return False

    while num == int(num):
        if num == 1:
            return True
        num /= 2.0
    return False
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PowersofTwo(raw_input())  