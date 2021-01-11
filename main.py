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
    1. Data User
    2. Katalog Kamera
    3. Katalog Perlengkapan Kamera
    4. Katalog Audio
    5. Katalog Lighting
    6. Melihat data transaksi
    7. Menghapus data transaksi
    8. Keluar
    """)

    pilihmenu = input("Pilih Menu : ")
    if pilihmenu == "1":
        print("""
        1. Melihat Data User
        2. Menghapus Data User
        3. Menambahkan Data User
        4. Kembali ke Menu Utama
        """)
        menu_user = input("Pilihan : ")
        if menu_user == "1":
            obj.LihatDataAll()
        elif menu_user == "2":
            hapus = input('Masukkan email dari user yang akan dihapus: ')
            obj.HapusUser(hapus)
        elif menu_user == "3":
            obj.TambahUser()
        elif menu_user == "4":
            MenuAdmin()
    elif pilihmenu == "2":
        print("""
        1. Melihat Katalog Kamera
        2. Menghapus Katalog Kamera
        3. Menambahkan Katalog Kamera
        4. Kembali ke Menu Utama
        """)
        menu_kamera = input("Pilihan : ")
        if menu_kamera == "1":
            kmr.LihatDataAll()
        elif menu_kamera == "2":
            hapus = input('Masukkan id kamera yang akan dihapus: ')
            kmr.HapusKamera(hapus)
        elif menu_kamera == "3":
            kmr.TambahKamera()
        elif menu_kamera == "4":
            MenuAdmin()
    if pilihmenu == "3":
        print("""
        1. Melihat Katalog Perlengkapan Kamera
        2. Menghapus Katalog Perlengkapan Kamera
        3. Menambahkan Katalog Perlengkapan Kamera
        4. Kembali ke Menu Utama
        """)
        menu_perlengkapan = input("Pilihan : ")
        if menu_perlengkapan == "1":
            eqp.LihatDataAll()
        elif menu_perlengkapan == "2":
            hapus = input('Masukkan id perlengkapan kamera yang akan dihapus: ')
            eqp.HapusPerlengkapan(hapus)
        elif menu_perlengkapan == "3":
            eqp.TambahPerlengkapan()
        elif menu_perlengkapan == "4":
            MenuAdmin()
    elif pilihmenu == "4":
        print("""
        1. Melihat Katalog Audio
        2. Menghapus Katalog Audio
        3. Menambahkan Katalog Audio
        4. Kembali ke Menu Utama
        """)
        menu_audio = input("Pilihan : ")
        if menu_audio == "1":
            aud.LihatDataAll()
        elif menu_audio == "2":
            hapus = input('Masukkan id audio yang akan dihapus: ')
            aud.HapusAudio(hapus)
        elif menu_audio == "3":
            aud.TambahAudio()
        elif menu_audio == "4":
            MenuAdmin()
    elif pilihmenu == "5":
        print("""
        1. Melihat Katalog Lighting
        2. Menghapus Katalog Lighting
        3. Menambahkan Katalog Lighting
        4. Kembali ke Menu Utama
        """)
        menu_lighting = input("Pilihan : ")
        if menu_lighting == "1":
            lgh.LihatDataAll()
        elif menu_lighting == "2":
            hapus = input('Masukkan id lighting yang akan dihapus: ')
            lgh.HapusLighting(hapus)
        elif menu_lighting == "3":
            lgh.TambahLighting()
        elif menu_lighting == "4":
            MenuAdmin()
    elif pilihmenu == "6":
        trn.LihatDataAll()
    elif pilihmenu == "7":
        trn.LihatDataAll()
        hapus = input('Masukkan id transaksi yang akan dihapus: ')
        trn.HapusTransaksi(hapus)
    elif pilihmenu == "8":
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
    ===Masuk / Daftar===
    1. Masuk
    2. Daftar
    (input 1 / 2)
    """)
    masuk = input("Masukkan pilihan : ")
    if masuk == "1":
        kode_admin = "lalens123"
        print("""
        SIapakah anda ?
        1. Admin
        2. User
        """)
        status = input("Masukkan status anda (1 / 2) : ")
        if status =="1":
            pastikan = input("Jika anda admin, masukkan kode admin : ")
            if pastikan == kode_admin:
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

