def is_palindrome(n):
    temp = n
    reversed = 0
    while(temp>0):
        rem = temp % 10
        reversed = reversed * 10 + rem
        temp = temp // 10
    
    print(f'Reversed number is {reversed}')

    if(reversed == n):
        print(f'Number is palindrome')
    else:
        print('Not palindrome')

is_palindrome(343)
is_palindrome(433)

