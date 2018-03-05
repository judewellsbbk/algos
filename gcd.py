def gdc(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return gdc(b, a_prime)

print(gdc(357,234))