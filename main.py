import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("D:/BACKUP/Documents/GitHub/SMT 3/PBO I/Project/camera.db")

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
