from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time

# =========================================
# DATA PARALLELISM (NRP GENAP)
# =========================================
def hitung_kuadrat(x):
    print(f"[Data Parallelism] Process {os.getpid()} memproses data: {x}")
    hasil = x * x
    print(f"[Data Parallelism] Hasil dari {x} = {hasil}")
    return x, hasil


def data_parallelism():
    print("\n=== DATA PARALLELISM DIMULAI ===")

    data = [1, 2, 3, 4, 5, 6, 7, 8]
    mulai = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(hitung_kuadrat, data))

    durasi = time.perf_counter() - mulai
    print("\n[Data Parallelism] Ringkasan hasil:")
    for angka, kuadrat in results:
        print(f"- {angka}^2 = {kuadrat}")
    print(f"[Data Parallelism] Total data diproses: {len(results)}")
    print(f"[Data Parallelism] Waktu eksekusi: {durasi:.2f} detik")
    print("=== DATA PARALLELISM SELESAI ===\n")


# =========================================
# TASK PARALLELISM (NRP GANJIL)
# =========================================
def task_download():
    print("[Task Parallelism] Task 1: Download dimulai...")
    mulai = time.perf_counter()
    time.sleep(2)
    print("[Task Parallelism] Task 1: Download selesai")
    return "Download", time.perf_counter() - mulai


def task_proses():
    print("[Task Parallelism] Task 2: Proses data dimulai...")
    mulai = time.perf_counter()
    time.sleep(3)
    print("[Task Parallelism] Task 2: Proses data selesai")
    return "Proses Data", time.perf_counter() - mulai


def task_simpan():
    print("[Task Parallelism] Task 3: Simpan data dimulai...")
    mulai = time.perf_counter()
    time.sleep(1)
    print("[Task Parallelism] Task 3: Simpan data selesai")
    return "Simpan Data", time.perf_counter() - mulai


def task_parallelism():
    print("\n=== TASK PARALLELISM DIMULAI ===")
    mulai = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(task_download),
            executor.submit(task_proses),
            executor.submit(task_simpan),
        ]

    hasil_task = [future.result() for future in futures]
    durasi_total = time.perf_counter() - mulai

    print("\n[Task Parallelism] Ringkasan task:")
    for nama_task, durasi_task in hasil_task:
        print(f"- {nama_task}: {durasi_task:.2f} detik")
    print(f"[Task Parallelism] Total waktu paralel: {durasi_total:.2f} detik")

    print("=== TASK PARALLELISM SELESAI ===\n")


# =========================================
# MAIN
# =========================================
if __name__ == "__main__":
    data_parallelism()
    task_parallelism()