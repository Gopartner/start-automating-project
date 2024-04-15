import os

def create_termux_package():
    # Tentukan path untuk folder results
    results_dir = 'results'

    # Pastikan folder results ada, jika belum buat
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Meminta input dari pengguna untuk nilai-nilai paket
    package_name = input("Masukkan nama package (Package): ")
    version = input("Masukkan versi package (Version): ")

    # Daftar pilihan arsitektur yang tersedia
    architecture_options = ['all', 'arm', 'aarch64', 'x86', 'x86_64']

    # Meminta pengguna untuk memilih arsitektur dari daftar yang tersedia
    print("Pilih arsitektur package:")
    for i, option in enumerate(architecture_options, start=1):
        print(f"{i}. {option}")

    architecture_choice = None
    while architecture_choice is None:
        try:
            choice_index = int(input("Masukkan nomor pilihan: ")) - 1
            if 0 <= choice_index < len(architecture_options):
                architecture_choice = architecture_options[choice_index]
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor pilihan.")

    maintainer = input("Masukkan informasi maintainer (Maintainer): ")
    description = input("Masukkan deskripsi package (Description): ")
    depends = input("Masukkan dependensi package (Depends): ")
    
    # Meminta input kode aplikasi (Python atau Bash)
    print("\nMasukkan kode aplikasi untuk package:")
    print("Ketik 'DONE' di baris terakhir untuk menyelesaikan input.")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "DONE":
            break
        code_lines.append(line)
    package_code = '\n'.join(code_lines)

    # Path untuk folder utama (mypackage di dalam results)
    package_dir = os.path.join(results_dir, package_name)

    # Membuat struktur folder di dalam mypackage jika belum ada
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)
    else:
        print(f"Struktur folder untuk {package_name} sudah ada.")
        action = input("Apakah Anda ingin menggantinya? (Y/N): ").strip().lower()
        if action != 'y':
            print("Pembuatan package dibatalkan.")
            return

    deb_dir = os.path.join(package_dir, 'DEBIAN')
    bin_dir = os.path.join(package_dir, 'usr', 'local', 'bin')

    # Buat direktori utama mypackage
    os.makedirs(deb_dir, exist_ok=True)
    os.makedirs(bin_dir, exist_ok=True)

    # Buat file control di dalam DEBIAN
    control_file_path = os.path.join(deb_dir, 'control')
    with open(control_file_path, 'w') as control_file:
        control_file.write(f"Package: {package_name}\n")
        control_file.write(f"Version: {version}\n")
        control_file.write(f"Architecture: {architecture_choice}\n")
        control_file.write(f"Maintainer: {maintainer}\n")
        control_file.write(f"Description: {description}\n")
        control_file.write(f"Depends: {depends}\n")

    # Buat file aplikasi di dalam bin (dengan kode yang diberikan)
    app_file_path = os.path.join(bin_dir, package_name)
    with open(app_file_path, 'w') as app_file:
        app_file.write("#!/usr/bin/env python\n")  # Atau ganti dengan shebang Bash jika kode Bash
        app_file.write(package_code)

    # Berikan izin eksekusi pada file aplikasi
    os.chmod(app_file_path, 0o755)  # Permission: -rwxr-xr-x

    print(f"\nStruktur folder dan file untuk {package_name} telah berhasil dibuat di dalam folder 'results'.")

# Panggil fungsi untuk membuat package Termux
create_termux_package()

