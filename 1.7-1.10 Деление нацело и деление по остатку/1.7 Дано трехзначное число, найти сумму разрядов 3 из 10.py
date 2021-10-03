'''
Дано целое положительное трехзначное число,
ваша задача найти сумму разрядов этого числа

Sample Input 1:

123
Sample Output 1:

6
Sample Input 2:

109
Sample Output 2:

10
'''

a = int(input())
a1 = a // 100
a3 = a % 10
a2 = a // 10 % 10

print(a1 + a2 + a3)
