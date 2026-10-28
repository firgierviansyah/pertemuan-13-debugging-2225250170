# Pertemuan 13 — Debugging dan Testing

**Nama:** Firgi Erviansyah  
**NIM:** 2225250170  
**Kelas:** 3B

## Kasus

Praktik ini dilakukan untuk mengidentifikasi dan memperbaiki tiga bug pada program pengolahan nilai mahasiswa, yaitu kesalahan perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

Debugging dilakukan dengan membandingkan hasil aktual dengan hasil yang diharapkan. Setelah penyebab bug ditemukan, kode diperbaiki dan diuji kembali menggunakan beberapa test case.

## Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| T2 | `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | Nilai `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | Nilai `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `[80, 60, 90, 70]` | `90` | `0` | FAIL |

## Bug Report

### B01 — Kesalahan Perhitungan Rata-rata

- **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program selalu membagi jumlah nilai dengan angka `5`.
- **Perbaikan:** Mengganti pembagi dengan `len(nilai)` dan menambahkan pemeriksaan untuk list kosong.

### B02 — Kesalahan Status Kelulusan

- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Program menggunakan operator `>` sehingga nilai 60 tidak memenuhi kondisi kelulusan.
- **Perbaikan:** Mengganti operator `>` menjadi `>=`.

### B03 — Kesalahan Pencarian Nilai Tertinggi

- **Gejala:** Program menghasilkan nilai tertinggi `0`.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Variabel pembanding dimulai dari `0` dan kondisi menggunakan operator `<`, sehingga pencarian nilai tertinggi tidak berjalan dengan benar.
- **Perbaikan:** Menggunakan elemen pertama sebagai nilai awal, membandingkan menggunakan operator `>`, dan menangani list kosong.

## Retest

Setelah perbaikan, kelima test case dijalankan kembali.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | `75.0` | `75.0` | PASS |
| T2 | `90.0` | `90.0` | PASS |
| T3 | `Lulus` | `Lulus` | PASS |
| T4 | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `90` | `90` | PASS |

Seluruh lima test case berhasil setelah perbaikan. Hasil pengujian menunjukkan bahwa ketiga bug telah diperbaiki sesuai hasil yang diharapkan.

## Cara Menjalankan

Pastikan terminal berada di folder utama proyek Pertemuan 13. Jalankan perintah berikut:

```bash
python praktik/praktik_4_debugging.py
```

Program akan menampilkan hasil perhitungan rata-rata, status kelulusan, nilai tertinggi, serta hasil pengujian test case.

## Refleksi

Teknik debugging yang paling membantu adalah menggunakan test case dan menelusuri logika program. Dengan membandingkan hasil aktual dan hasil yang diharapkan, penyebab kesalahan lebih mudah ditemukan. Setelah kode diperbaiki, pengujian ulang diperlukan untuk memastikan hasil sudah benar dan tidak menimbulkan kesalahan pada bagian lain.