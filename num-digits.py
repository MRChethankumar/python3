def count_digits(n):
    count = 0
    while(n>0):
        n = n//10
        count = count+1
    return count
if '__name__' == '__main__':
    num = int(input("Enter number: "))
    c = count_digits(num)
    print("Hello there")
    print(f'Number digits : {c}')