---

# 🎯 Program Otomatisasi Microsoft Bing Rewards

Script Python ini akan membuka situs [Bing Rewards](https://rewards.bing.com), memungkinkan kamu login secara manual, lalu mengotomatiskan pencarian berdasarkan daftar kata kunci, menutup tab setelah selesai, dan membuka tab baru untuk keyword selanjutnya.

---

## 🛠️ Fitur

- Membuka halaman Microsoft Rewards (Bing)
- Menunggu hingga login selesai secara manual
- Melakukan pencarian otomatis dari array data
- Menutup tab setelah pencarian
- Membuka tab baru untuk pencarian berikutnya
- Menggunakan browser **Microsoft Edge** via Selenium

---

## ⚙️ Persyaratan Sistem

- Linux (Ubuntu/Debian direkomendasikan)
- Python 3.10+ (dengan akses ke `venv`)
- Microsoft Edge browser
- Microsoft Edge WebDriver (versi sama dengan browser)

---

## 📦 Instalasi

### 1. Clone Repository (Opsional)

```bash
git clone https://github.com/namauser/Program_Automation_Microsoft_Rewards.git
cd Program_Automation_Microsoft_Rewards
````

### 2. Pastikan Python 3 dan pip terinstal

```bash
python3 --version
pip3 --version
```

Jika tidak ada, install dengan:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

### 3. Install `python3-venv` jika belum ada

```bash
sudo apt install python3.12-venv
```

(Sesuaikan dengan versi Python kamu jika berbeda)

---

### 4. Buat dan Aktifkan Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 5. Install Dependencies

```bash
pip install selenium
```

---

## 🧭 Setup Microsoft Edge WebDriver

1. Cek versi Microsoft Edge kamu:

   ```bash
   microsoft-edge --version
   ```

2. Unduh WebDriver dari:
   [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

   Pastikan versi WebDriver **sesuai dengan versi Edge kamu**.

3. Ekstrak dan letakkan `msedgedriver` ke direktori dalam `PATH`, atau simpan di folder proyek lalu ubah inisialisasi driver:

   ```python
   driver = webdriver.Edge(executable_path="./msedgedriver")
   ```

---

## 🚀 Menjalankan Program

Setelah semua siap dan environment aktif:

```bash
python main.py
```

1. Program akan membuka browser Microsoft Edge.
2. Kamu **login secara manual** ke akun Microsoft Rewards.
3. Setelah login berhasil, program akan:

   * Mencari kata dari daftar (`data_array`)
   * Submit pencarian
   * Tutup tab dan buka tab baru
   * Ulangi proses hingga semua data habis

---

## 🔒 Catatan Penting

* Jangan login lebih dari sekali secara otomatis — gunakan login manual untuk menghindari deteksi bot.
* Jangan mempercepat `sleep()` terlalu banyak — bisa dianggap mencurigakan oleh server.
* Jangan gunakan akun Microsoft utama jika khawatir soal keamanan akun.

---

## 📄 Struktur Proyek

```
Program_Automation_Microsoft_Rewards/
├── main.py
├── venv/               # (virtual environment folder)
├── msedgedriver        # (jika tidak diletakkan di PATH)
└── README.md
```

---

## 🧹 Menonaktifkan Virtual Environment

Setelah selesai:

```bash
deactivate
```

---

## 🆘 Troubleshooting

| Masalah                                   | Solusi                                                |
| ----------------------------------------- | ----------------------------------------------------- |
| `Import "selenium" could not be resolved` | Pastikan venv aktif saat buka VS Code                 |
| `WebDriverException`                      | Pastikan WebDriver sesuai versi browser               |
| `Permission denied saat install pip`      | Aktifkan venv dan jangan install global               |
| Tab tidak tertutup otomatis               | Pastikan `ActionChains` bekerja dan waktu delay cukup |

---

## 🤝 Kontribusi

Pull Request atau masukan sangat diterima. Silakan fork dan submit PR!

---

## 📜 Lisensi

Proyek ini bebas digunakan untuk keperluan pribadi. Jangan digunakan untuk tindakan pelanggaran TOS layanan.

```

---

Jika kamu menggunakan nama repo atau folder tertentu, kamu bisa ganti bagian `git clone` dan struktur file. Kalau kamu ingin saya bantu buatkan file `requirements.txt` atau skrip setup otomatis, tinggal bilang.