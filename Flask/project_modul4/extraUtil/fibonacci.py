def Funct(n):
    return 1 if n < 3 else Funct(n-1) + Funct(n-3)

if __name__ == '__main__':
    for i in range(0, 16):
        print(Funct(i))