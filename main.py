import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("camera.db")

class User(Database):
    def __init__ (self):
        Database.__init__(self)
        self.nama = None
        self.email = None
        self.password = None
        self.alamat = None
        self.telp = None 
    
    def TambahUser(self):
        self.nama = input ("Masukkan nama : ")
        self.email = input ("Masukkan email : ")
        self.password = input ("Masukkan password : ")
        self.alamat = input ("Masukkan alamat : ")
        self.telp = input ("Masukkan no. telp : ")

        query = 'INSERT INTO akun(nama,email,password,Alamat,No_Telp) VALUES (?,?,?,?,?)'
        isi = (self.nama,self.email,self.password,self.alamat,self.telp)
        self.conn.execute(query,isi)
        self.conn.commit()

    def HapusUser(self, hapus):
        for row in self.conn.execute('SELECT * FROM akun'):
            print(row)
        query = 'DELETE FROM akun WHERE email = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    
    def LihatDataAll(self):
        query= 'SELECT * FROM akun'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')

class katalog_camera(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_kamera = None
        self.merk = None
        self.type = None
        self.harga_hari = None
    
    def TambahKamera(self):
        self.id_kamera = input ("Masukkan id camera : ")
        self.merk = input ("Masukkan merk camera : ")
        self.type = input ("Masukkan tipe camera : ")
        self.harga_hari = input ("Masukkan harga per hari : ")
   
        query = 'INSERT INTO katalog_camera(id_kamera,merk,type,harga_perHari) VALUES (?,?,?,?)'
        isi = (self.id_kamera,self.merk,self.type,self.harga_hari)
        self.conn.execute(query,isi)
        self.conn.commit()
    def HapusKamera(self, hapus):
        for row in self.conn.execute('SELECT * FROM katalog_camera'):
            print(row)
        query = 'DELETE FROM katalog_camera WHERE id_kamera = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    def LihatDataAll(self):
        query= 'SELECT * FROM katalog_camera'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
    
class katalog_perlengkapan(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_perlengkapan = None
        self.jenis = None
        self.harga_hari = None
    
    def TambahPerlengkapan(self):
        self.id_perlengkapan = input ("Masukkan id perlegkapan camera : ")
        self.jenis = input ("Masukkan jenis perlengkapan camera : ")
        self.harga_hari = input ("Masukkan harga per hari : ")
   
        query = 'INSERT INTO katalog_perlengkapan(id_perlengkapan,jenis,harga_perHari) VALUES (?,?,?)'
        isi = (self.id_perlengkapan,self.jenis,self.harga_hari)
        self.conn.execute(query,isi)
        self.conn.commit()
    def HapusPerlengkapan(self, hapus):
        for row in self.conn.execute('SELECT * FROM katalog_perlengkapan'):
            print(row)
        query = 'DELETE FROM katalog_perlengkapan WHERE id_perlengkapan = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    def LihatDataAll(self):
        query= 'SELECT * FROM katalog_perlengkapan'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}')

class katalog_audio(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_audio = None
        self.jenis = None
        self.harga_hari = None
    
    def TambahAudio(self):
        self.id_audio = input ("Masukkan id perlegkapan audio : ")
        self.jenis = input ("Masukkan jenis perlengkapan audio : ")
        self.harga_hari = input ("Masukkan harga per hari : ")
   
        query = 'INSERT INTO katalog_audio(id_audio,jenis,harga_perHari) VALUES (?,?,?)'
        isi = (self.id_audio,self.jenis,self.harga_hari)
        self.conn.execute(query,isi)
        self.conn.commit()
    def HapusAudio(self, hapus):
        for row in self.conn.execute('SELECT * FROM katalog_audio'):
            print(row)
        query = 'DELETE FROM katalog_audio WHERE id_audio = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    def LihatDataAll(self):
        query= 'SELECT * FROM katalog_audio'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}')

class katalog_lighting(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_lighting = None
        self.jenis = None
        self.harga_hari = None
    
    def TambahLighting(self):
        self.id_lighting = input ("Masukkan id perlegkapan lighting : ")
        self.jenis = input ("Masukkan jenis perlengkapan lighting : ")
        self.harga_hari = input ("Masukkan harga per hari : ")
   
        query = 'INSERT INTO katalog_lighting(id_lighting,jenis,harga_perHari) VALUES (?,?,?)'
        isi = (self.id_lighting,self.jenis,self.harga_hari)
        self.conn.execute(query,isi)
        self.conn.commit()
    def HapusLighting(self, hapus):
        for row in self.conn.execute('SELECT * FROM katalog_lighting'):
            print(row)
        query = 'DELETE FROM katalog_lighting WHERE id_lighting = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    def LihatDataAll(self):
        query= 'SELECT * FROM katalog_lighting'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}')

class Transaksi(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_transaksi = None
        self.nama = None
        self.id_barang = None
    
    def HasilTransaksi(self):
        self.nama = input ("Masukkan nama anda : ")
        self.id_barang = input ("Masukkan id_barang yang dipesan : ")
   
        query = 'INSERT INTO hasil_transaksi(id_transaksi,nama,id_barang) VALUES (?,?,?)'
        isi = (self.id_transaksi,self.nama,self.id_barang)
        self.conn.execute(query,isi)
        self.conn.commit()
    def HapusTransaksi(self, hapus):
        for row in self.conn.execute('SELECT * FROM hasil_transaksi'):
            print(row)
        query = 'DELETE FROM hasil_transaksi WHERE id_transaksi = ?'
        isi = hapus,
        self.conn.execute(query,isi)
        self.conn.commit()
    def LihatDataAll(self):
        query= 'SELECT * FROM hasil_transaksi'
        cursor = self.conn.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}')

obj = User()
kmr = katalog_camera()
eqp = katalog_perlengkapan()
aud = katalog_audio()
lgh = katalog_lighting()
trn = Transaksi()

def MenuAdmin():
    print("""
    ==Menu Admin== 
    1. Melihat Data User
    2. Menghapus Data User
    3. Menambahkan Data User
    4. Melihat Katalog Kamera
    5. Menghapus Katalog Kamera
    6. Menambahkan Katalog Kamera
    7. Melihat Katalog Perlengkapan Kamera
    8. Menghapus Katalog Perlengkapan Kamera
    9. Menambahkan Katalog Perlengkapan Kamera
    10. Melihat Katalog Perlengkapan Audio
    11. Menghapus Katalog Perlenkapan Audio
    12. Menambahkan Katalog Perlengkapan Audio
    13. Melihat Katalog Perlengkapan Lighting
    14. Mengahapus Katalog Perlenkapan Lighting
    15. Menambahkan Katalog Perlengkapan Lighting
    16. Melihat data transaksi
    17. Menghapus data transaksi
    18. Keluar
    """)

    pilih = input("Pilih Menu : ")
    if pilih == "1":
        obj.LihatDataAll()
    elif pilih == "2":
        hapus = input('Masukkan email dari user yang akan dihapus: ')
        obj.HapusUser(hapus)
    elif pilih == "3":
        obj.TambahUser()
    elif pilih == "4":
        kmr.LihatDataAll()
    elif pilih == "5":
        hapus = input('Masukkan id kamera yang akan dihapus: ')
        kmr.HapusKamera(hapus)
    elif pilih == "6":
        kmr.TambahKamera()
    elif pilih == "7":
        eqp.LihatDataAll()
    elif pilih == "8":
        hapus = input('Masukkan id perlengkapan kamera yang akan dihapus: ')
        eqp.HapusPerlengkapan(hapus)
    elif pilih == "9":
        eqp.TambahPerlengkapan()
    elif pilih == "10":
        aud.LihatDataAll()
    elif pilih == "11":
        hapus = input('Masukkan id audio yang akan dihapus: ')
        aud.HapusAudio(hapus)
    elif pilih == "12":
        aud.TambahAudio()
    elif pilih == "13":
        lgh.LihatDataAll()
    elif pilih == "14":
        hapus = input('Masukkan id lighting yang akan dihapus: ')
        lgh.HapusLighting(hapus)
    elif pilih == "15":
        lgh.TambahLighting()
    elif pilih == "16":
        trn.LihatDataAll()
    elif pilih == "17":
        trn.LihatDataAll()
        hapus = input('Masukkan id transaksi yang akan dihapus: ')
        trn.HapusTransaksi(hapus)
    elif pilih == "18":
        exit()


def MenuUser():
    print("""
    ==Menu==
    1. Katalog Kamera
    2. Katalog Perlengkapan Kamera
    3. Katalog Perlengkapan Audio
    4. Katalog Perlengkapan Lighting
    5. Transaksi Saya
    6. Keluar
    """)

    pilih = input("Pilih Menu : ")
    if pilih == "1":
        kmr.LihatDataAll()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatDataAll()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "2":
        eqp.LihatDataAll()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatDataAll()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "3":
        aud.LihatDataAll()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatDataAll()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "4":
        lgh.LihatDataAll()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatDataAll()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "5":
        trn.LihatDataAll()
        print("""
        Kembali ke menu ?
        1. Ya
        2. Tidak
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            MenuUser()
        elif beli == "2":
            exit() 
    elif pilih == "6":
        exit()

def Main():
    print("====SELAMAT DATANG DI RENTAL CAMERA LA LENS====")
    print("""
    ===Login / Register===
    1. Login
    2. Register
    (input 1 / 2)
    """)
    masuk = input("Masukkan pilihan : ")
    if masuk == "1":
        email_admin = "la.lens@gmail.com"
        print("""
        SIapakah anda ?
        1. Admin
        2. User
        """)
        status = input("Masukkan status anda (1 / 2) : ")
        if status =="1":
            pastikan = input("Jika anda admin, masukkan email admin : ")
            if pastikan == email_admin:

                while True:
                    MenuAdmin()
            else:
                print("Anda bukan admin!! Silahkan restart program!!")
        elif status == "2":
            MenuUser()

    elif masuk == "2":
        obj.TambahUser()
        print("Data Anda telah ditambahkan")
        Main()
Main()

