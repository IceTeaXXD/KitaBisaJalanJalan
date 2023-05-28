import sqlite3

def init_Database():
    conn = sqlite3.connect('kitabisajalan.db')
    c = conn.cursor()

    q1 = """CREATE TABLE IF NOT EXISTS daerah(
        ID_Daerah INTEGER,
        Daerah TEXT,
        Lokasi_Koordinat TEXT,
        PRIMARY KEY(ID_Daerah)
        )"""

    q2 = """
    create table IF NOT EXISTS catatan(
        ID_Catatan INTEGER,
        tgl_mulai TEXT,
        tgl_akhir TEXT,
        isi TEXT,
        PRIMARY KEY(ID_Catatan)
        )
    """

    q3 = """
    create table IF NOT EXISTS lokasiwisata(
        `ID_Wisata` INTEGER,
        `Lokasi_Wisata` TEXT,
        `Lokasi_Koordinat` TEXT,
        `Daerah` INTEGER,
        `Deskripsi` TEXT,
        `Gambar` TEXT,
        PRIMARY KEY(`ID_Wisata`),
        FOREIGN KEY (`Daerah`) REFERENCES daerah(`ID_Daerah`)
        )
    """

    q4 = """
    create table IF NOT EXISTS transportasi(
        `ID_Transportasi` integer,
        `Jenis_Transportasi` text,
        `Harga_Transportasi` integer,
        PRIMARY KEY(`ID_Transportasi`)
    )
    """

    q5 = """
    create table IF NOT EXISTS riwayatperjalanan(
        `ID_riwayat` INTEGER,
        `ID_Perjalanan` INTEGER,
        `tgl_mulai` TEXT,
        `tgl_akhir` TEXT,
        `biaya_perjalanan` INTEGER,
        PRIMARY KEY (`ID_riwayat`),
        FOREIGN KEY (`ID_Perjalanan`) REFERENCES catatan(`ID_Catatan`)
    )
    """

    q6 = """
    create table IF NOT EXISTS destinasiPerjalanan(
    `ID_Perjalanan` INTEGER,
    `ID_Destinasi` INTEGER,
    PRIMARY KEY (`ID_Perjalanan`, `ID_Destinasi`),
    FOREIGN KEY (`ID_Perjalanan`) REFERENCES riwayatperjalanan(`ID_Perjalanan`),
    FOREIGN KEY (`ID_Destinasi`) REFERENCES lokasiwisata(`ID_Wisata`)
    )
    """

    q7 = """
    create table IF NOT EXISTS transportPilihan(
        `ID_Riwayat` INTEGER,
        `ID_Transportasi` INTEGER,
        `Urutan` INTEGER,
        PRIMARY KEY(`ID_Riwayat`, `ID_Transportasi`, `Urutan`),
        FOREIGN KEY (`ID_Riwayat`) REFERENCES riwayatperjalanan(`ID_riwayat`),
        FOREIGN KEY (`ID_Transportasi`) REFERENCES transportasi(`ID_Transportasi`)
    )
    """

    q8 = """
    insert into daerah(ID_Daerah, Daerah, Lokasi_Koordinat) values 
    (1, 'Jakarta', '10'), 
    (2, 'Bandung', '11'), 
    (3, 'Bali', '12')
    """
    
    q9 = """
    insert into lokasiwisata values
    (1, 'Dufan', '10', 1, 'Tempat bermain anak', 'dufan.jpg'),
    (2, 'Pantai Ancol', '10', 1, 'Tempat pantai anak', 'ancol.jpg'),
    (3, 'Grand Indonesia', '10', 1, 'Ini Mall di Jakarta Pusat', 'GI.jpg'),
    (4, 'Museum Bank Indonesia', '10', 1, 'Museum tentang sejarah bank dan uang di Indonesia', 'museumBI.jpeg'),
    (5, 'Katedral Jakarta', '10', 1, 'Tempat Ibadah di Jakarta. Benda historis', 'katedraljkt.jpg'),
    (6, 'PVJ', '10', 2, 'Ini mall gess', 'pvj.jpg'),
    (7, 'Orchid Forest', 15, 2, 'Tempat wisata alam', 'orchid.jpg'),
    (8, 'Paskal 23', 15, 2, 'Macet bet ini tempat','paskal.jpg'),
    (9, 'Cihampelas Walk', 15, 2, 'Tempat wisata mall lagi', 'ciwalk.jpg'),
    (10, 'Lembang Zoo', 15, 2, 'Kebun Binatang di Lembang', 'lembang.jpeg'),
    (11, 'ITB', 15, 2, 'Tempat wisata kuliah', 'itb.jpeg'),
    (12, 'Pantai Kuta', 30, 3, 'Tempat wisata pantai', 'kuta.jpg'),
    (13, 'Pura Ulun Danu Brata', 35, 3, 'Tempat wisata alam', 'pura.jpg'),
    (14, 'Pantai Sanur', 40, 3, 'Tempat wisata pantai', 'sanur.jpg'),
    (15, 'Pantai Lovina', 45, 3, 'Pantai Lovina atau Lovina adalah pesisir pantai yang terletak sekitar 9 km sebelah barat kota Singaraja. Daerah ini merupakan salah satu objek wisata yang ada di Bali Utara', 'lvina.jpg'),
    (16, 'Pantai Tanjung Benoa', 50, 3, 'Tanjung Benoa merupakan sebuah kelurahan di Kecamatan Kuta Selatan, Kabupaten Badung, Bali. Siapa sangka sebelum berkembang menjadi kawasan wisata water sport seperti sekarang ini, Tanjung Benoa adalah kampung nelayan dan tempat pemberhentian para pedagang dari Cina.', 'tanjungbenoa.jpg')
    """

    q10 = """
    insert into transportasi values
    (3, 'Mobil', 10000),
    (4, 'Bus', 5000),
    (1, 'Kereta', 50000),
    (2, 'Pesawat', 1000000)
    """
    with conn:
        c.execute(q1)
        c.execute(q2)
        c.execute(q3)
        c.execute(q4)
        c.execute(q5)
        c.execute(q6)
        c.execute(q7)
        c.execute(q8)
        c.execute(q9)
        c.execute(q10)

    conn.close()

init_Database()
print("Sukses")