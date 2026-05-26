import sqlite3
import os

# Simpan database di Desktop biar 100% bisa diakses
db_path = os.path.expanduser("~/Desktop/mahasiswa.db")

# Buat koneksi ke database
conn = sqlite3.connect(db_path)

# Buat tabel
conn.execute("""
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    nim INTEGER NOT NULL,
    prodi TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print(f"✅ Database berhasil dibuat di: {db_path}")
