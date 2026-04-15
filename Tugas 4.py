import tkinter as tk
from tkinter import ttk, font as tkFont

# ══════════════════════════════════════════════════════════
#  TEMA WARNA
# ══════════════════════════════════════════════════════════
BG_DARK   = "#0f1117"
BG_CARD   = "#1a1d2e"
BG_PANEL  = "#151726"
ACCENT    = "#3d7eff"
ACCENT2   = "#5c95ff"
SUCCESS   = "#2ecc8a"
WARNING   = "#f0a500"
DANGER    = "#ff4d6d"
TEXT_MAIN = "#dde3f5"
TEXT_DIM  = "#7882a4"
BTN_YES   = "#22c37e"
BTN_NO    = "#e05260"

# ══════════════════════════════════════════════════════════
#  KNOWLEDGE BASE — 7 JENIS KERUSAKAN
# ══════════════════════════════════════════════════════════
database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["blue_screen", "beep", "freeze", "aplikasi_crash", "restart_sendiri"],
        "solusi": (
            "1. Bersihkan pin RAM dengan penghapus karet\n"
            "2. Pasang ulang RAM di slot yang berbeda\n"
            "3. Tes dengan satu keping RAM saja\n"
            "4. Jalankan Windows Memory Diagnostic\n"
            "5. Ganti RAM baru jika tetap bermasalah"
        ),
        "threshold": 2,
        "warna": DANGER,
        "ikon": "💾"
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["tidak_menyala", "mati_mendadak", "restart_sendiri", "tidak_charging", "lampu_berkedip"],
        "solusi": (
            "1. Periksa seluruh kabel power dan konektor\n"
            "2. Ukur voltase output PSU dengan multimeter\n"
            "3. Bersihkan debu pada ventilasi PSU\n"
            "4. Ganti PSU dengan kapasitas daya lebih besar\n"
            "5. Laptop: ganti adaptor / charger baru"
        ),
        "threshold": 2,
        "warna": WARNING,
        "ikon": "⚡"
    },
    "Overheat (Prosesor)": {
        "gejala": ["panas_berlebih", "mati_mendadak", "kipas_berisik", "freeze", "restart_sendiri"],
        "solusi": (
            "1. Bersihkan kipas dan heatsink dari debu\n"
            "2. Ganti thermal paste pada prosesor\n"
            "3. Pastikan ventilasi casing tidak terhalang\n"
            "4. Tambahkan kipas casing tambahan\n"
            "5. Kurangi/nonaktifkan overclock jika ada"
        ),
        "threshold": 2,
        "warna": "#ff7043",
        "ikon": "🌡️"
    },
    "VGA Bermasalah": {
        "gejala": ["layar_artefak", "no_display", "freeze", "aplikasi_crash", "blue_screen"],
        "solusi": (
            "1. Pasang ulang kartu VGA di slot PCIe\n"
            "2. Bersihkan pin VGA dengan penghapus\n"
            "3. Update atau rollback driver VGA ke versi stabil\n"
            "4. Periksa suhu VGA, ganti thermal paste\n"
            "5. Ganti VGA baru jika kerusakan parah"
        ),
        "threshold": 2,
        "warna": "#9c6bff",
        "ikon": "🖥️"
    },
    "Hardisk Corrupt": {
        "gejala": ["boot_lambat", "file_corrupt", "klik_bunyi", "freeze", "aplikasi_crash"],
        "solusi": (
            "1. Jalankan CHKDSK /f /r untuk perbaiki bad sector\n"
            "2. Segera backup data penting sebelum terlambat!\n"
            "3. Defragmentasi hardisk (khusus HDD, bukan SSD)\n"
            "4. Pertimbangkan migrasi ke SSD\n"
            "5. Bunyi klik keras = tanda kritis, segera ganti!"
        ),
        "threshold": 2,
        "warna": "#f0c040",
        "ikon": "💿"
    },
    "Motherboard Rusak": {
        "gejala": ["tidak_menyala", "beep", "no_display", "restart_sendiri", "lampu_berkedip"],
        "solusi": (
            "1. Periksa kapasitor yang menggembung atau bocor\n"
            "2. Reset BIOS: cabut baterai CMOS selama 30 detik\n"
            "3. Periksa semua konektor power pada motherboard\n"
            "4. Bawa ke teknisi berpengalaman untuk diagnosa\n"
            "5. Pertimbangkan penggantian motherboard"
        ),
        "threshold": 2,
        "warna": "#ef5350",
        "ikon": "🔌"
    },
    "OS / Software Corrupt": {
        "gejala": ["boot_lambat", "aplikasi_crash", "blue_screen", "file_corrupt", "freeze"],
        "solusi": (
            "1. Jalankan: sfc /scannow di Command Prompt (Admin)\n"
            "2. Lakukan Startup Repair via Recovery Mode\n"
            "3. Scan malware/virus dengan antivirus terbaru\n"
            "4. Uninstall program yang baru diinstal\n"
            "5. Install ulang OS jika semua cara gagal"
        ),
        "threshold": 2,
        "warna": SUCCESS,
        "ikon": "🗂️"
    }
}

# ══════════════════════════════════════════════════════════
#  DAFTAR GEJALA (kode, teks pertanyaan)
# ══════════════════════════════════════════════════════════
semua_gejala = [
    ("blue_screen",     "Apakah sering muncul layar biru (Blue Screen / BSOD)?"),
    ("tidak_menyala",   "Apakah komputer / laptop tidak mau menyala sama sekali?"),
    ("mati_mendadak",   "Apakah perangkat sering mati mendadak tanpa peringatan?"),
    ("kipas_berisik",   "Apakah kipas pendingin berputar sangat kencang / berisik?"),
    ("panas_berlebih",  "Apakah perangkat terasa sangat panas saat digunakan?"),
    ("layar_artefak",   "Apakah muncul kotak, garis, atau glitch aneh di layar?"),
    ("no_display",      "Apakah layar blank/hitam, tidak ada tampilan sama sekali?"),
    ("boot_lambat",     "Apakah proses booting / startup terasa sangat lambat?"),
    ("file_corrupt",    "Apakah file sering rusak atau tidak bisa dibuka?"),
    ("klik_bunyi",      "Apakah terdengar bunyi klik-klik aneh dari dalam perangkat?"),
    ("restart_sendiri", "Apakah perangkat sering restart sendiri secara tiba-tiba?"),
    ("freeze",          "Apakah perangkat sering hang / freeze (tidak merespons)?"),
    ("beep",            "Apakah terdengar bunyi beep berulang saat perangkat dinyalakan?"),
    ("aplikasi_crash",  "Apakah aplikasi sering tiba-tiba keluar sendiri (crash)?"),
    ("tidak_charging",  "Apakah laptop tidak mau mengisi daya / tidak charging?"),
    ("lampu_berkedip",  "Apakah lampu indikator power berkedip-kedip tidak normal?"),
]


# ══════════════════════════════════════════════════════════
#  KELAS UTAMA APLIKASI
# ══════════════════════════════════════════════════════════
class SistemPakarKomputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas 4 KB — H1D024023")
        self.root.geometry("640x520")
        self.root.configure(bg=BG_DARK)
        self.root.resizable(False, False)

        self.gejala_terpilih = []
        self.index_q = 0

        self._setup_fonts()
        self._build_frame()
        self._show_welcome()

    # ─── Setup Font ────────────────────────────────────────
    def _setup_fonts(self):
        fam = "Consolas" 
        self.f_title    = tkFont.Font(family=fam, size=13, weight="bold")
        self.f_sub      = tkFont.Font(family=fam, size=9)
        self.f_question = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_btn      = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_small    = tkFont.Font(family=fam, size=8)
        self.f_result   = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_sol      = tkFont.Font(family=fam, size=8)
        self.f_big      = tkFont.Font(family=fam, size=36, weight="bold")

    # ─── Kerangka utama ────────────────────────────────────
    def _build_frame(self):
        # ── Header ──
        hdr = tk.Frame(self.root, bg=BG_PANEL, pady=10)
        hdr.pack(fill=tk.X)

        tk.Label(hdr, text="█ SISTEM PAKAR DIAGNOSA KOMPUTER", font=self.f_title, bg=BG_PANEL, fg=ACCENT).pack()
        tk.Label(hdr, text="Identifikasi kerusakan hardware & software secara otomatis", font=self.f_small, bg=BG_PANEL, fg=TEXT_DIM).pack(pady=(1,0))

        # garis aksen
        tk.Frame(self.root, bg=ACCENT, height=2).pack(fill=tk.X)

        # ── Kontainer konten ──
        self.frame_body = tk.Frame(self.root, bg=BG_DARK)
        self.frame_body.pack(fill=tk.BOTH, expand=True, padx=28, pady=18)

    # ─── Bersihkan frame body ───────────────────────────────
    def _clear(self):
        for w in self.frame_body.winfo_children():
            w.destroy()

    # ════════════════════════════════════════════════════════
    #  HALAMAN 1 — SELAMAT DATANG
    # ════════════════════════════════════════════════════════
    def _show_welcome(self):
        self._clear()

        tk.Label(self.frame_body, text="?>_", font=self.f_big, bg=BG_DARK, fg=ACCENT).pack(pady=(8, 4))

        tk.Label(self.frame_body, text="Selamat Datang!", font=self.f_result, bg=BG_DARK, fg=TEXT_MAIN).pack()

        tk.Label(self.frame_body,
                 text="Jawab pertanyaan berikut dengan YA atau TIDAK.\n"
                      "Sistem akan mendiagnosa kerusakan perangkat Anda.",
                 font=self.f_sub, bg=BG_DARK, fg=TEXT_DIM, justify=tk.CENTER).pack(pady=(6, 14))

        # kotak info statistik
        info = tk.Frame(self.frame_body, bg=BG_CARD, padx=14, pady=10)
        info.pack(fill=tk.X, pady=(0, 18))

        stats = [
            ("16", "Gejala Dianalisis"),
            ("7",  "Jenis Kerusakan"),
            ("AI", "Inferensi Cerdas"),
        ]
        for val, lbl in stats:
            col = tk.Frame(info, bg=BG_CARD)
            col.pack(side=tk.LEFT, expand=True)
            tk.Label(col, text=val, font=tkFont.Font(family="Consolas", size=16, weight="bold"), bg=BG_CARD, fg=ACCENT).pack()
            tk.Label(col, text=lbl, font=self.f_small, bg=BG_CARD, fg=TEXT_DIM).pack()

        self._btn(self.frame_body, "▶  MULAI DIAGNOSA", ACCENT, ACCENT2, self._start_diagnosis)

    # ════════════════════════════════════════════════════════
    #  HALAMAN 2 — PERTANYAAN
    # ════════════════════════════════════════════════════════
    def _start_diagnosis(self):
        self.gejala_terpilih = []
        self.index_q = 0
        self._show_question()

    def _show_question(self):
        self._clear()

        if self.index_q >= len(semua_gejala):
            self._proses_hasil()
            return

        kode, teks = semua_gejala[self.index_q]
        no   = self.index_q + 1
        tot  = len(semua_gejala)
        pct  = no / tot

        # ── Progress bar ──
        tk.Label(self.frame_body, text=f"Pertanyaan {no} / {tot}",
                 font=self.f_small, bg=BG_DARK, fg=TEXT_DIM).pack(anchor=tk.W)

        bar_bg = tk.Frame(self.frame_body, bg=BG_CARD, height=5)
        bar_bg.pack(fill=tk.X, pady=(2, 10))
        bar_bg.pack_propagate(False)
        tk.Frame(bar_bg, bg=ACCENT, height=5).place(
            relx=0, rely=0, relwidth=pct, relheight=1)

        # ── Kartu pertanyaan ──
        card = tk.Frame(self.frame_body, bg=BG_CARD, padx=20, pady=20)
        card.pack(fill=tk.X, pady=(0, 6))

        tk.Label(card, text="[ ? ]", font=tkFont.Font(family="Consolas", size=18, weight="bold"),
                 bg=BG_CARD, fg=ACCENT).pack()

        tk.Label(card, text=teks,
                 font=self.f_question, bg=BG_CARD, fg=TEXT_MAIN,
                 wraplength=480, justify=tk.CENTER).pack(pady=(8, 4))

        if self.gejala_terpilih:
            tk.Label(card,
                     text=f"✓  {len(self.gejala_terpilih)} gejala telah dicatat",
                     font=self.f_small, bg=BG_CARD, fg=SUCCESS).pack()

        # ── Tombol YA / TIDAK ──
        row = tk.Frame(self.frame_body, bg=BG_DARK)
        row.pack(pady=10)

        self._btn(row, "✓   YA",    BTN_YES, "#28d98c",
                  lambda: self._jawab(True),  side=tk.LEFT, px=14)
        self._btn(row, "✗   TIDAK", BTN_NO,  "#f05870",
                  lambda: self._jawab(False), side=tk.LEFT, px=14)

        # ── Tombol kembali ──
        if self.index_q > 0:
            self._btn(self.frame_body, "← Kembali", BG_CARD, BG_PANEL, self._back, fg=TEXT_DIM)

    def _jawab(self, ya: bool):
        if ya:
            self.gejala_terpilih.append(semua_gejala[self.index_q][0])
        self.index_q += 1
        self._show_question()

    def _back(self):
        if self.index_q > 0:
            kode_prev = semua_gejala[self.index_q - 1][0]
            if kode_prev in self.gejala_terpilih:
                self.gejala_terpilih.remove(kode_prev)
            self.index_q -= 1
            self._show_question()

    # ════════════════════════════════════════════════════════
    #  MESIN INFERENSI
    # ════════════════════════════════════════════════════════
    def _proses_hasil(self):
        """
        Mesin Inferensi berbasis Dictionary.
        Hitung jumlah kecocokan gejala tiap kerusakan,
        tampilkan jika >= threshold.
        """
        hasil = []
        for nama, data in database_kerusakan.items():
            cocok = [g for g in data["gejala"] if g in self.gejala_terpilih]
            skor  = len(cocok)
            if skor >= data["threshold"]:
                hasil.append({
                    "nama":   nama,
                    "skor":   skor,
                    "total":  len(data["gejala"]),
                    "solusi": data["solusi"],
                    "warna":  data["warna"],
                    "ikon":   data["ikon"],
                })

        # Urutkan: skor tertinggi di atas
        hasil.sort(key=lambda x: x["skor"], reverse=True)
        self._show_result(hasil)

    # ════════════════════════════════════════════════════════
    #  HALAMAN 3 — HASIL DIAGNOSA
    # ════════════════════════════════════════════════════════
    def _show_result(self, hasil):
        self._clear()

        # scrollable area
        canvas = tk.Canvas(self.frame_body, bg=BG_DARK, highlightthickness=0)
        sb = ttk.Scrollbar(self.frame_body, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=BG_DARK)

        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        # ── Judul hasil ──
        if not hasil:
            tk.Label(inner, text="[ OK ]", font=tkFont.Font(family="Consolas", size=28, weight="bold"), bg=BG_DARK, fg=SUCCESS).pack(pady=(6, 2))
            tk.Label(inner, text="Tidak Ada Kerusakan Terdeteksi", font=self.f_result, bg=BG_DARK, fg=SUCCESS).pack()
            tk.Label(inner,
                     text=f"Dari {len(self.gejala_terpilih)} gejala yang Anda laporkan,\n"
                          "tidak ditemukan pola kerusakan yang signifikan.\n\n"
                          "Saran: Lakukan pemeliharaan rutin atau konsultasi\n"
                          "ke teknisi komputer terdekat.",
                     font=self.f_sub, bg=BG_DARK, fg=TEXT_DIM, justify=tk.CENTER).pack(pady=12)
        else:
            tk.Label(inner, text=f"⚠  {len(hasil)} Kemungkinan Kerusakan Ditemukan", font=self.f_result, bg=BG_DARK, fg=WARNING).pack(pady=(4, 10))

            for item in hasil:
                pct_val = int(item["skor"] / item["total"] * 100)

                card = tk.Frame(inner, bg=BG_CARD, padx=14, pady=12)
                card.pack(fill=tk.X, pady=4, padx=2)

                # header kartu
                hdr_c = tk.Frame(card, bg=BG_CARD)
                hdr_c.pack(fill=tk.X)

                tk.Label(hdr_c, text=f"{item['ikon']}  {item['nama']}", font=self.f_result, bg=BG_CARD, fg=item["warna"]).pack(side=tk.LEFT)

                tk.Label(hdr_c, text=f"Cocok: {item['skor']}/{item['total']} ({pct_val}%)", font=self.f_small, bg=BG_CARD, fg=TEXT_DIM).pack(side=tk.RIGHT)

                # progress mini kecocokan
                pb_bg = tk.Frame(card, bg=BG_PANEL, height=4)
                pb_bg.pack(fill=tk.X, pady=(4, 8))
                pb_bg.pack_propagate(False)
                tk.Frame(pb_bg, bg=item["warna"], height=4).place(relx=0, rely=0, relwidth=item["skor"]/item["total"], relheight=1)

                # solusi
                tk.Label(card, text="💡 SOLUSI:", font=tkFont.Font(family="Consolas", size=8, weight="bold"), bg=BG_CARD, fg=TEXT_MAIN, anchor=tk.W).pack(fill=tk.X)
                tk.Label(card, text=item["solusi"], font=self.f_sol, bg=BG_CARD, fg=TEXT_DIM, justify=tk.LEFT, anchor=tk.W).pack(fill=tk.X, pady=(2,0))

        # ── Tombol Ulangi ──
        tk.Frame(inner, bg=BG_DARK, height=6).pack()
        self._btn(inner, "↺  DIAGNOSA ULANG", ACCENT, ACCENT2, self._show_welcome)
        tk.Frame(inner, bg=BG_DARK, height=14).pack()

    # ────────────────────────────────────────────────────────
    #  HELPER: buat tombol seragam
    # ────────────────────────────────────────────────────────
    def _btn(self, parent, text, bg, hover_bg, cmd,
             fg="white", side=None, px=0):
        b = tk.Button(parent, text=text, font=self.f_btn, bg=bg, fg=fg, relief=tk.FLAT, padx=22, pady=7, cursor="hand2", activebackground=hover_bg, activeforeground=fg, command=cmd, bd=0)
        b.bind("<Enter>", lambda e: b.config(bg=hover_bg))
        b.bind("<Leave>", lambda e: b.config(bg=bg))
        if side:
            b.pack(side=side, padx=px)
        else:
            b.pack(pady=4)
        return b


# ══════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    app  = SistemPakarKomputer(root)
    root.mainloop()