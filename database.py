import sqlite3

databaseName = "camera.db"

conn = sqlite3.connect("camera.db")

tabel = [
    'CREATE TABLE IF NOT EXISTS "akun" ("nama" text NOT NULL,"email" text NOT NULL, "password" text NOT NULL, "Alamat" text NOT NULL, "No_Telp" INTEGER NOT NULL, PRIMARY KEY("email"))',
    'CREATE TABLE IF NOT EXISTS "katalog_camera" ("id_kamera" INTEGER NOT NULL,"merk" text NOT NULL, "type" text NOT NULL, "harga_perHari" INTEGER NOT NULL, PRIMARY KEY("id_kamera"))',
    'CREATE TABLE IF NOT EXISTS "katalog_perlengkapan" ("id_perlengkapan" INTEGER NOT NULL,"jenis" text NOT NULL, "harga_perHari" INTEGER NOT NULL, PRIMARY KEY("id_perlengkapan"))',
    'CREATE TABLE IF NOT EXISTS "katalog_audio" ("id_audio" INTEGER NOT NULL,"jenis" text NOT NULL, "harga_perHari" INTEGER NOT NULL, PRIMARY KEY("id_audio"))',
    'CREATE TABLE IF NOT EXISTS "katalog_lighting" ("id_lighting" INTEGER NOT NULL,"jenis" text NOT NULL, "harga_perHari" INTEGER NOT NULL, PRIMARY KEY("id_lighting"))',
    'CREATE TABLE IF NOT EXISTS "hasil_transaksi" ("id_transaksi" INTEGER NOT NULL, "nama" text NOT NULL, "id_barang" INTEGER NOT NULL, PRIMARY KEY("id_transaksi" AUTOINCREMENT))',
]


def buat():
    for p in range(len(tabel)):
        conn.execute(tabel[p])
        conn.commit

buat()