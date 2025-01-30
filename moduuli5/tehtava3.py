def alkuluku(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Syötä kokonaisluku: "))
if alkuluku(numero):
    print(f"{numero} on alkuluku.")
else:
    print(f"{numero} ei ole alkuluku.")