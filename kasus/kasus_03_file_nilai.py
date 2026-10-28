
def baca_nilai(nama_file):
    nilai = []

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            nilai.append(float(baris.strip()))

    return nilai


print("Data nilai:", baca_nilai("data/nilai.txt"))
