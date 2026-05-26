from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

#database
DB_PATH = os.path.expanduser("~/Desktop/mahasiswa.db")

#con database
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Halaman utama
@app.route("/dashboard")
def index():
    conn = get_db_connection()
    mahasiswa = conn.execute("SELECT * FROM mahasiswa").fetchall()
    conn.close()
    return render_template("index.html", mahasiswa=mahasiswa)

# Tambah data mhs
@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        prodi = request.form["prodi"]

        #simpan ke database
        conn = get_db_connection()
        conn.execute("INSERT INTO mahasiswa (nama, nim, prodi) VALUES (?, ?, ?)",
                     (nama, nim, prodi))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("tambah.html")

# Edit data mhs
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM mahasiswa WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        prodi = request.form["prodi"]
        conn.execute("UPDATE mahasiswa SET nama=?, nim=?, prodi=? WHERE id=?",
                     (nama, nim, prodi, id))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn.close()
    return render_template("edit.html", mahasiswa=data)

# Hapus data nhs
@app.route("/hapus/<int:id>")
def hapus(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM mahasiswa WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

#route melihat db
@app.route("/db")
def lihat_db():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM mahasiswa").fetchall()
    conn.close()
    return "<br>".join([str(dict(row)) for row in data])


if __name__ == "__main__":
    app.run(debug=True)
