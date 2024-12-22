def hitung_faktorial(n):
    faktorial = 1 
    if n < 0:
        return "Faktorial hanya didefinisikan untuk bilangan non-negatif."
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial

bilangan = int(input("Masukkan bilangan bulat non-negatif: "))

hasil_faktorial = hitung_faktorial(bilangan)

if isinstance(hasil_faktorial, int):
    print(f"{bilangan}! = {hasil_faktorial}")
else:
    print(hasil_faktorial)
