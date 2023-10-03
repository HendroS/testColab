from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
import basicauth
import bcrypt
import os
import datetime
import uuid
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5433/db_perpustakaan'
# data peminjaman {endpoint}
#authentication 
def auth():
    data = request.authorization
    if data != None:
        username = data.parameters['username']
        password = data.parameters['password']

        user = User().query.filter_by(username = username).first()
        if user != None:
            is_match = bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8'))
            if is_match == True:
                return user

db = SQLAlchemy(app)
buku_penulis = db.Table('buku_penulis',
                        db.Column('id_buku',db.Integer, db.ForeignKey('buku.id_buku'), primary_key = True),
                        db.Column('id_penulis',db.Integer, db.ForeignKey('penulis.id_penulis')))

class Book(db.Model):
    __tablename__ = 'buku'
    id_buku:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    id_kategori:Mapped[int] = mapped_column(db.Integer,ForeignKey('kategori.id_kategori'))
    judul:Mapped[str] = mapped_column(db.String)
    tahun:Mapped[int] = mapped_column(db.Integer)
    jumlah_hal:Mapped[int] = mapped_column(db.Integer)
    daftarpenulis = db.relationship('Penulis', secondary = buku_penulis, lazy = 'subquery',
                           backref = db.backref('daftarbuku', lazy = True))
    
class Kategori(db.Model):
    __tablename__ = 'kategori'
    id_kategori:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    nama:Mapped[str] = mapped_column(db.String)
    deskripsi:Mapped[str] = mapped_column(db.String)
    daftarbuku = db.relationship('Book', backref ='kategori', lazy = True)

class Penulis(db.Model):
    __tablename__ = 'penulis'
    id_penulis:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    nama_penulis:Mapped[str] = mapped_column(db.String)
    kewarganegaraan_penulis:Mapped[str] = mapped_column(db.String)
    tahun_kelahiran:Mapped[int] = mapped_column(db.Integer)

class User(db.Model):
    __tablename__ = 'users'
    id_user : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username : Mapped[str] = mapped_column(db.String)
    password : Mapped[str] = mapped_column(db.String)
    isadmin : Mapped[bool] = mapped_column(db.Boolean,default=False)
    # relasi table user dengan peminjaman
    # member_peminjaman = relationship('Peminjaman',back_populates='member',foreign_keys='Peminjaman.id_user')
    # petugas = relationship('Peminjaman',back_populates='petugas',foreign_keys='Peminjaman.id_petugas')
    # pengembalian_petugas = db.relationship('Pengembalian',backref = 'petugas',lazy = True)

class Peminjaman(db.Model):
    __tablename__ = 'peminjaman'
    id_peminjaman : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    id_petugas : Mapped[int] = mapped_column(ForeignKey("users.id_user"),nullable=False)
    id_user : Mapped[int] = mapped_column(ForeignKey("users.id_user"),nullable=False)
    tgl_pinjam : Mapped[datetime.date] = mapped_column(db.Date,default=datetime.date.today(),nullable=False)
    tgl_pengembalian : Mapped[datetime.date] = mapped_column(db.Date,nullable=False)
    dikembalikan : Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    # member = relationship("User",back_populates="member_peminjaman",foreign_keys='Peminjaman.id_user')
    # petugas = relationship("User",back_populates="petugas",foreign_keys='Peminjaman.id_petugas')
    # detail_peminjaman = relationship("Detailpeminjaman",back_populates="peminjaman")
    # pengembalian = relationship("Pengembalian",uselist=False, backref="peminjaman")


class Pengembalian(db.Model):
    __tablename__ = 'pengembalian'
    id_pengembalian : Mapped[int] = mapped_column(db.Integer,primary_key=True)
    id_peminjaman : Mapped[int] = mapped_column(ForeignKey("peminjaman.id_peminjaman"),nullable=False)
    tgl_pengembalian : Mapped[datetime.date] = mapped_column(db.Date,default = datetime.date.today())
    id_petugas : Mapped[int] = mapped_column(ForeignKey("peminjaman.id_petugas"),nullable=False)

# halaman utama
@app.route('/')
def home():
    return 'Welcom to RestAPI Adi with flask and SQLAlchemy'

# halaman buku
# set data buku dengan penulis {endpoint} {V}   
@app.route('/kategori')
def get_kategori():
    categori = Kategori()
    daftarbuku = categori.query.all()
    arr = []
    for categori in daftarbuku:
        arr.append({'id':categori.id_kategori,
                    'nama':categori.nama,
                    'deskripsi':categori.deskripsi
                    })
    return jsonify([
        {
            'result':arr
        }
    ])

@app.route('/penulis')
def get_penulis():
    author = Penulis()
    authors:[Penulis] = author.query.all()
    arr = []
    for author in authors:
        arr.append({'nama penulis':author.nama_penulis,
                    'kewarganegaraan':author.kewarganegaraan_penulis,
                    'tahun kelahiran':author.tahun_kelahiran,
                    'id':author.id_penulis})
    return jsonify([
        {
            'result':arr
        }
    ])

# crud buku
@app.route('/buku/<int:id>')
def get_buku_by_id(id):
    buku = Book.query.filter_by(id_buku = id).first_or_404()
    return {"buku":{'id_buku': buku.id_buku,
                    'id_kategori':buku.id_kategori,
                    'judul':buku.judul,
                    'tahun':buku.tahun,
                    'jumlah_halaman':buku.jumlah_hal,
                     'daftarpenulis':[
                    x.nama_penulis 
            for x in buku.daftarpenulis]}}

@app.route('/buku/', methods=['GET'])
def get_all_buku():
    # b = auth()
    # if b['isadmin'] == False:
    #     return {'message':'anauthorizes'}
    books = Book() 
    daftarbuku = books.query.all()
    arr = []
    for book in daftarbuku:
        arr.append({'id':book.judul,
                    'daftarpenulis':[b.nama_penulis for b in book.daftarpenulis]})
    return jsonify([
        {
            'result':arr
        }
    ])

@app.route('/buku',methods = ["POST"])
def tambah_buku():
    buku = request.get_json()
    error = []
    if not 'id_kategori'in buku:
        error.append('id kategori buku')
    if not 'judul' in buku:
        error.append('judul buku')
    if not 'tahun' in buku:
        error.append('tahun terbit buku')
    if not 'jumlah_hal' in buku:
        error.append('jumlah halaman buku')
    if len(error)>0:
        return jsonify(
            {
                'error':'Bad Request',
                'message': 'Masukkan '
            }
        )
    b = Book(
        id_kategori = buku['id_kategori'],
        judul = buku['judul'],
        tahun = buku['tahun'],
        jumlah_hal = buku['jumlah_hal']
    )
    Penulis
    for id in buku['daftarpenulis']:
        p = Penulis.query.filter_by(id_penulis = id).first()
        if p == None:
            return {"message":f"penulis dengan id {id} tidak terdapat pada database"}
        b.daftarpenulis.append(p)
    db.session.add(b)
    return {
        'id':b.id_kategori,
        'judul':b.judul,
        'tahun':b.tahun,
        'jumlah halaman':b.jumlah_hal, 
        'daftarpenulis':[
            {'nama_penulis':x.nama_penulis} 
            for x in b.daftarpenulis]
    },201

@app.route('/buku/<id>/', methods =['PUT'])
def update_buku(id):
    data = request.get_json()
    buku = Book.query.filter_by(id_kategori =id).first_or_404()
    buku.judul=data['judul']
    buku.id_kategori = data['id_kategori']
    buku.tahun = data['tahun']
    buku.jumlah_hal = data['jumlah_hal']
    buku.daftarpenulis = []
    for id in buku['daftarpenulis']:
        p = Penulis.query.filter_by(id_penulis = id).first()
        if p == None:
            return {"message":f"penulis dengan id {id} tidak terdapat pada database"}
        buku.daftarpenulis.append(p)
    db.session.commit()
    return jsonify({
        'id':buku.id_kategori,
        'judul':buku.judul,
        'tahun':buku.tahun,
        'jumlah halaman':buku.jumlah_hal,
        'daftarpenulis':[
            x.nama_penulis 
            for x in buku.daftarpenulis]
    })

@app.route('/buku/<int:id>/', methods =['DELETE'])
def delete_buku(id):
    buku = Book.query.filter_by(id_buku=id).first_or_404()
    db.session.delete(buku)
    db.session.commit()
    return{
        'success': 'Data Berhasil di Hapus'
    }

#mengambil data user 
@app.route('/user/<int:id>',methods =["PUT"])
def update_user(id):
    data = request.get_json()
    user = User.query.filter_by(id_user=id).first_or_404()
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'),salt= bcrypt.gensalt())

    user.username = data['username']
    # untuk ngencode password
    user.password = hashed.decode('utf-8')
    db.session.commit()
    return {"messege":"Data Berhasil dirubah"},200

@app.route('/user/<int:id>/', methods = ['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id_user = id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return {
        'success' : 'Data Berhasil Dihapus'
    }

@app.route('/user/')
def get_user():
    return jsonify(
        [
            {
                'id_user':user.id_user, 
                'username':user.username,
                'password':user.password,
                'isadmin' : user.isadmin
            }
            for user in User.query.all()
        ]
    )

@app.route('/user',methods =['POST'])
def create_user():
    data = request.get_json()    
    if not 'username' in data or not 'password' in data or 'isadmin' not in data:
        return jsonify(
            {
                'error': 'Bad Request',
                'message' : 'Username dan password atau isadmin tidak ada'
            }
        ),400   
    u = User(
        username =data['username'],
        password =data['password'],
        isadmin =data['isadmin']
    )
    db.session.add(u)
    db.session.commit()
    return {
        'username' : u.username,
        'password' : u.password
    },201

@app.route('/peminjaman/<int:id>')
def get_peminjaman_id(id):
    peminjaman = Peminjaman.query.filter_by(id_peminjaman = id).first()
    return jsonify({'id_petugas': peminjaman.id_petugas,
                         'id_user':peminjaman.id_user,
                         'tgl_pinjam': peminjaman.tgl_pinjaman,
                         'tgl_pengembalian': peminjaman.tgl_pengembalian,
                         'dikembalikan' : peminjaman.dikembalikan})
@app.route('/peminjaman/', methods = ["GET"])
def get_all_peminjaman():
    peminjaman = Peminjaman.query.all()
    # detail_peminjaman = peminjaman.query.all()
    arr = []
    for peminjamans in peminjaman:
        arr.append({'id':peminjamans.id_peminjaman,
                    'id_petugas': peminjamans.id_petugas,
                    'id_user': peminjamans.id_user,
                    'tgl_pinjam': peminjamans.tgl_pinjam,
                    'tgl_pengembalian': peminjamans.tgl_pengembalian,
                    'dikembalikan' : peminjamans.dikembalikan})
    return jsonify([
           {
               'result': arr
           }
       ])

@app.route('/peminjaman/', methods = ["POST"])
def tambah_peminjaman():
    peminjaman = request.get_json()
    pem = Peminjaman(
        id_petugas = peminjaman['id_petugas'],
        id_user = peminjaman['id_user'],
        tgl_pinjam = peminjaman['tgl_pinjam'],
        tgl_pengembalian = peminjaman['tgl_pengembalian']
    )
    db.session.add(pem)
    db.session.commit()
    return {"message":"peminjaman berhasil ditambahkan"}
    # Pengembalian
    # for id in peminjaman['detail_peminjaman']:
    #     pen = Pengembalian.query.filter_by(id_pengembalian = id).first()
    #     if pen == None:
    #         return {"message":f"peminjam buku dengan {id} tidak ada dalam database"} 
    #     pem.detail_peminjaman.append(pen)
    # db.session.add(pem)
    # return {
    #     'id' = 
    # }

@app.route('/pengembalian/<int:id>', methods = ["PUT"])
def update_kembalikan_buku(id):
    peminjamans = Peminjaman.query.filter_by(id_peminjaman = id).first_or_404()
    peminjamans.dikembalikan = True
    db.session.commit()
    return {"message":"buku berhasil dikembalikan"}

if __name__ == "__main__":
    app.run(debug=True)
