length = int(input('\npanjang fibonacci: '))


def febonacci(length):
    n1, n2 = 0, 1
    result = [n1, n2]

    for i in range(2, length):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        result.append(n3)

    return result


print(febonacci(length))
