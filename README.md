### Penjelasan singkat per fungsi

### ⚙️ Manajemen Antarmuka (Front-end)
1.  **`__init__`**: Inisialisasi window utama Tkinter dan konfigurasi dasar.
2.  **`_setup_fonts`**: Pengaturan tipografi aplikasi menggunakan font monospaced.
3.  **`_build_frame`**: Pembuatan layout utama (Header dan Body container).
4.  **`_clear`**: Fungsi utilitas untuk membersihkan layar saat transisi antar halaman.
5.  **`_show_welcome`**: Rendering tampilan halaman awal/splash screen.
6.  **`_show_question`**: Komponen UI untuk menampilkan pertanyaan dan progress bar.
7.  **`_show_result`**: Komponen UI untuk menampilkan kartu hasil diagnosa dan solusi.
8.  **`_btn`**: Factory method untuk menciptakan tombol kustom dengan efek hover.

### 🧠 Logika & Inferensi (Back-end)
9.  **`_start_diagnosis`**: Inisialisasi ulang state aplikasi (reset variabel) saat mulai.
10. **`_jawab`**: Handler untuk memproses input jawaban dan menyimpan state gejala.
11. **`_back`**: Logika navigasi mundur untuk memperbaiki jawaban sebelumnya.
12. **`_proses_hasil`**: Mesin inferensi yang melakukan pencocokan pola (*pattern matching*) antara input pengguna dengan knowledge base.

### Program tersebut juga terdapat "database" yang berisi gejala laptop, warna, dan font
