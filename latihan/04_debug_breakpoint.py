
def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


nilai = [10, 20, 30]
hasil = hitung_total(nilai)

print("Total:", hasil)
