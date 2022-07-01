import random
def guesser(q):
    a = -1000000
    b =  1000000
    z = random.randint(a,b)
    count = 0
    while z != q:
        if z > q:
            print(str(z) + " = This is too high ")
            b = z
            z = random.randint(a,b)
            count += 1
        elif z < q:
            print(str(z)+ " = This is too low")
            a = z
            z = random.randint(a,b)
            count += 1

    count += 1
    print(str(z) + "= It took" + ' ' + str(count) + ' ' + "attempts")

def main():
     if __name__ == '__main__':
        guesser(242446)

main()
