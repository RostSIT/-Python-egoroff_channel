'''
У вас есть N рублей и вы хотите купить
максимальное количество кроссовок по цене R рублей.
Сколько кроссовок Вы можете себе купить?
На вход программе поступают 2 положительных целых числа N, R

Sample Input 1:

150
50
Sample Output 1:

3
Sample Input 2:

120
41
Sample Output 2:

2
'''

N = int(input())
R = int(input())

PairOfSneakers = N // R

print(PairOfSneakers)
