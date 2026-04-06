# Quiz - Parallel Computing Use Case

## Identitas Mahasiswa
- Nama      : Rifky Zufari
- NRP       : 152024187
- Jurusan   : Informatika

---

## Deskripsi Tugas
Program ini dibuat untuk memenuhi tugas Parallel Computing dengan mengimplementasikan:

1. Data Parallelism (NRP Genap)
2. Task Parallelism (NRP Ganjil)

Program ditulis menggunakan Python dengan memanfaatkan library `concurrent.futures`.

---

## 1. Data Parallelism

### Konsep
Data Parallelism adalah metode di mana:
- Satu fungsi yang sama dijalankan
- Pada data yang berbeda secara paralel

### Implementasi pada Program
- Fungsi: `hitung_kuadrat(x)`
- Data: list angka dari 1 sampai 8
- Setiap proses menghitung kuadrat angka yang berbeda
- Menggunakan `ProcessPoolExecutor`

### Penjelasan Eksekusi
- Setiap data diproses oleh proses yang berbeda (ditandai PID berbeda)
- Semua proses berjalan secara bersamaan
- Output menunjukkan bahwa pekerjaan dilakukan secara paralel

### Alasan Penggunaan
- Cocok untuk pekerjaan CPU-bound
- Memanfaatkan multi-core CPU
- Menghindari keterbatasan Global Interpreter Lock (GIL)

---

## 2. Task Parallelism

### Konsep
Task Parallelism adalah metode di mana:
- Beberapa task berbeda dijalankan secara bersamaan

### Implementasi pada Program
Terdapat 3 task:
1. Task Download
2. Task Proses Data
3. Task Simpan Data

Menggunakan `ThreadPoolExecutor`

### Penjelasan Eksekusi
- Ketiga task berjalan secara paralel
- Tidak saling bergantung
- Waktu eksekusi lebih efisien dibandingkan jika dijalankan secara berurutan

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall