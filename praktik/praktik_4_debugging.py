
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

print("\n=== Pengujian Test Case ===")

test_cases = [
    ("T1", "Rata-rata 4 data", hitung_rata_rata([80, 60, 90, 70]), 75.0),
    ("T2", "Rata-rata 2 data", hitung_rata_rata([100, 80]), 90.0),
    ("T3", "Nilai 60", status(60), "Lulus"),
    ("T4", "Nilai 59", status(59), "Tidak lulus"),
    ("T5", "Nilai tertinggi", nilai_tertinggi([80, 60, 90, 70]), 90),
]

for kode, deskripsi, aktual, expected in test_cases:
    hasil = "PASS" if aktual == expected else "FAIL"
    print(f"{kode} - {deskripsi}: {hasil}")
    print(f"    Expected: {expected} | Actual: {aktual}")
