def prime_factorize(n):
    prime_numbers = []
    # 2で割り切れるまで割る
    while n % 2 == 0:
        prime_numbers.append(2)
        n //= 2
        
    # 次に奇数で割っていく
    f = 3  # 最初の奇数として3を設定
    while f * f <= n:  # fがnの平方根以下である限り繰り返すことで計算量を削減
        if n % f == 0:
            prime_numbers.append(f)
            n //= f
        else:
            f += 2
            
    # 割り切った数が1でなければその数字も素因数となる
    if n != 1:
        prime_numbers.append(n)
        
    return prime_numbers