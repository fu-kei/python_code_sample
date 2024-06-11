import math

def is_prime_number(n):
    #1,0は素数ではない
    if n == 1 or n == 0:
        return False
    #√nまで2から順に余りを取り、割り切れるなら素数ではない
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#入出力用
#n=int(input())
#print(is_prime_number(n))