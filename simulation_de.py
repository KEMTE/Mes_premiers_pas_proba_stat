import random

lancers = [random.randint(1,6) for _ in range(10000)]
moyenne = sum(lancers) / len(lancers)

print(f"Moyenne sur 10000 lancers : {moyenne}")
