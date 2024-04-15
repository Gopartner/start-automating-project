import os
import subprocess
import sys

def clear_screen():
    # Membersihkan layar terminal
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def is_valid_project_name(project_name):
    # Memeriksa apakah nama proyek hanya terdiri dari karakter yang valid
    valid_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,.-')
    return all(char in valid_characters for char in project_name) and ' ' not in project_name

def display_error_message(message):
    # Menampilkan pesan kesalahan dalam format "box"
    clear_screen()
    border = '+' + '-' * (len(message) + 2) + '+'
    print(border)
    print(f'| {message} |')
    print(border)

def choose_option(options, prompt):
    # Menampilkan pilihan dan meminta input nomor pilihan
    while True:
        clear_screen()
        for idx, option in enumerate(options, 1):
            print(f'{idx}. {option}')
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)

def setup_project():
    results_dir = 'results'

    # Membuat folder 'results' jika belum ada
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)
    
    while True:
        clear_screen()
        project_name = input('Masukkan nama proyek: ')

        if not is_valid_project_name(project_name):
            display_error_message('Nama proyek tidak valid. Pastikan hanya menggunakan huruf, angka, _, ,, atau - dan tidak mengandung spasi.')
            input('Tekan Enter untuk melanjutkan...')
            continue
        
        project_dir = os.path.join(results_dir, project_name)
        if os.path.exists(project_dir):
            display_error_message(f'Nama proyek "{project_name}" sudah digunakan. Silakan gunakan nama lain.')
            input('Tekan Enter untuk melanjutkan...')
            continue
        
        break

    os.mkdir(project_dir)
    os.chdir(project_dir)

    # Pilihan frontend
    frontend_options = [
        'React.js (with Create React App)',
        'Vue.js (with Vue CLI)',
        'Angular (with Angular CLI)'
    ]
    frontend_choice = choose_option(frontend_options, 'Pilih Front-end (masukkan nomor pilihan): ')
    frontend_name = frontend_options[frontend_choice - 1]

    # Pilihan build tool
    build_tool_options = [
        'Vite.js',
        'Webpack'
    ]
    build_tool_choice = choose_option(build_tool_options, 'Pilih Build Tool (masukkan nomor pilihan): ')
    build_tool_name = build_tool_options[build_tool_choice - 1]

    # Pilihan backend
    backend_options = [
        'Express.js (for Node.js)',
        'Flask (for Python)',
        'Spring Boot (for Java)'
    ]
    backend_choice = choose_option(backend_options, 'Pilih Back-end (masukkan nomor pilihan): ')
    backend_name = backend_options[backend_choice - 1]

    # Konfirmasi konfigurasi proyek
    clear_screen()
    print('Konfigurasi proyek:')
    print(f'Nama Proyek: {project_name}')
    print(f'Front-end: {frontend_name}')
    print(f'Build Tool: {build_tool_name}')
    print(f'Back-end: {backend_name}')

    confirmation = input('Apakah konfigurasi di atas sudah benar? (y/n): ')
    if confirmation.lower() != 'y':
        clear_screen()
        print('Konfigurasi proyek dibatalkan.')
        return
    
    # Inisialisasi proyek
    if frontend_choice == 1:
        initialize_create_react_app()
    elif frontend_choice == 2:
        initialize_vue_cli()
    elif frontend_choice == 3:
        initialize_angular_cli()

    if backend_choice == 1:
        initialize_express()
    elif backend_choice == 2:
        initialize_flask()
    elif backend_choice == 3:
        initialize_spring_boot()

def initialize_create_react_app():
    # Inisialisasi proyek dengan Create React App
    subprocess.run(['npx', 'create-react-app', '.'])

def initialize_vue_cli():
    # Inisialisasi proyek dengan Vue CLI
    subprocess.run(['npm', 'install', '-g', '@vue/cli'])
    subprocess.run(['vue', 'create', '.'])

def initialize_angular_cli():
    # Inisialisasi proyek dengan Angular CLI
    subprocess.run(['npm', 'install', '-g', '@angular/cli'])
    subprocess.run(['ng', 'new', 'client'])

def initialize_express():
    # Inisialisasi proyek backend Express.js
    subprocess.run(['npm', 'init', '-y'])
    subprocess.run(['npm', 'install', 'express'])

def initialize_flask():
    # Inisialisasi proyek backend Flask
    # Tambahkan logika inisialisasi Flask di sini
    pass

def initialize_spring_boot():
    # Inisialisasi proyek backend Spring Boot
    # Tambahkan logika inisialisasi Spring Boot di sini
    pass

if __name__ == '__main__':
    setup_project()

