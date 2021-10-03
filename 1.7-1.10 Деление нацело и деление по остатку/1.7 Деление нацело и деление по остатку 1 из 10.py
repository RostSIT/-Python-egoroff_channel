'''
Дано целое положительное число,
ваша задача вывести его последнюю цифру

Sample Input 1:

123
Sample Output 1:

3
Sample Input 2:

87632
Sample Output 2:

2
'''

a = int(input())
a = a % 10
print(a)
