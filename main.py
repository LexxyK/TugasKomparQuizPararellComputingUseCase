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
    return hasil


def data_parallelism():
    print("\n=== DATA PARALLELISM DIMULAI ===")

    data = [1, 2, 3, 4, 5, 6, 7, 8]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(hitung_kuadrat, data))

    print("[Data Parallelism] Semua hasil:", results)
    print("=== DATA PARALLELISM SELESAI ===\n")


# =========================================
# TASK PARALLELISM (NRP GANJIL)
# =========================================
def task_download():
    print("[Task Parallelism] Task 1: Download dimulai...")
    time.sleep(2)
    print("[Task Parallelism] Task 1: Download selesai")


def task_proses():
    print("[Task Parallelism] Task 2: Proses data dimulai...")
    time.sleep(3)
    print("[Task Parallelism] Task 2: Proses data selesai")


def task_simpan():
    print("[Task Parallelism] Task 3: Simpan data dimulai...")
    time.sleep(1)
    print("[Task Parallelism] Task 3: Simpan data selesai")


def task_parallelism():
    print("\n=== TASK PARALLELISM DIMULAI ===")

    with ThreadPoolExecutor() as executor:
        executor.submit(task_download)
        executor.submit(task_proses)
        executor.submit(task_simpan)

    print("=== TASK PARALLELISM SELESAI ===\n")


# =========================================
# MAIN
# =========================================
if __name__ == "__main__":
    data_parallelism()
    task_parallelism()