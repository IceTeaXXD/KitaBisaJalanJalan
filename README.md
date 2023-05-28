# IF2250-2023-K03-01-KitaBisaJalanJalan

## Nama dan Deskripsi Aplikasi
Aplikasi ini diberi nama Kita Bisa Jalan-Jalan, sebuah aplikasi pembuat riwayat perjalanan yang dibuat untuk Gagas P. Bahar dan sebagai tugas di mata kuliah IF2250 Rekayasa Perangkat Lunak pada semester genap di tahun akademik 2022/2023.

## Fitur Aplikasi
Aplikasi yang dibuat memiliki fitur-fitur sebagai berikut
1. Membuat rencana perjalanan, berikut memilih destinasi wisata, memilih metode transportasi, serta memilih tanggal perjalanan. Setelahnya, akan diberikan estimasi biaya perjalanan
2. Melihat perjalanan yang sedang berlangsung. Dari rencana perjalanan yang telah dibuat, diberikan lokasi-lokasi wisata sebagai quick access ke perjalanan yang sedang berlangsung
3. Menambah catatan ke perjalanan yang sudah selesai. Pengguna dapat menambahkan catatan khusus untuk riwayat perjalanannya dari halaman riwayat perjalanan

## Cara Menjalankan Aplikasi
1. Program dijalankan pada sistem operasi Windows. Pastikan sudah memasang compiler Python pada perangkat Anda
2. Pada root folder aplikasi, jalankan file `main.bat`
3. Program sudah dapat dijalankan

## Daftar Modul yang Diimplementasikan dan Pembagian Tugasnya
1. Modul Membuat Rencana Perjalanan: Henry Anand Septian Radityo, Ahmad Nadil, Matthew Mahendra, Jauza Lathifah Annassalafi, Azmi Hasna Zahrani
2. Modul Melihat Riwayat Perjalanan yang Sedang Berlangsung: Henry Anand Septian Radityo, Azmi Hazna Zahrani, Jauza Annassalafi
3. Modul Melihat Riwayat Perjalanan: Ahmad Nadil, Henry Anand Septian Radityo, Azmi Hazna Zahrani
4. Modul Membuat Catatan Perjalanan: Ahmad Nadil, Matthew Mahendra, Henry Anand Septian Radityo
5. Modul Unit Testing: Jauza Lathifah Annassalafi, Azmi Hasna Zahrani

## Daftar Tabel Basis Data dan Atributnya
1. daerah(
        ID_Daerah INTEGER,
        Daerah TEXT,
        Lokasi_Koordinat TEXT,
        PRIMARY KEY(ID_Daerah)
        )

2. catatan(
        ID_Catatan INTEGER,
        tgl_mulai TEXT,
        tgl_akhir TEXT,
        isi TEXT,
        PRIMARY KEY(ID_Catatan))

3. lokasiwisata(
        `ID_Wisata` INTEGER,
        `Lokasi_Wisata` TEXT,
        `Lokasi_Koordinat` TEXT,
        `Daerah` INTEGER,
        `Deskripsi` TEXT,
        `Gambar` TEXT,
        PRIMARY KEY(`ID_Wisata`),
        FOREIGN KEY (`Daerah`) REFERENCES daerah(`ID_Daerah`)
        )

4. transportasi(
        `ID_Transportasi` integer,
        `Jenis_Transportasi` text,
        `Harga_Transportasi` integer,
        PRIMARY KEY(`ID_Transportasi`)
    )

5. riwayatperjalanan(
        `ID_riwayat` INTEGER,
        `ID_Perjalanan` INTEGER,
        `tgl_mulai` TEXT,
        `tgl_akhir` TEXT,
        `biaya_perjalanan` INTEGER,
        PRIMARY KEY (`ID_riwayat`),
        FOREIGN KEY (`ID_Perjalanan`) REFERENCES catatan(`ID_Catatan`)
    )

6. destinasiPerjalanan(
    `ID_Perjalanan` INTEGER,
    `ID_Destinasi` INTEGER,
    PRIMARY KEY (`ID_Perjalanan`, `ID_Destinasi`),
    FOREIGN KEY (`ID_Perjalanan`) REFERENCES riwayatperjalanan(`ID_Perjalanan`),
    FOREIGN KEY (`ID_Destinasi`) REFERENCES lokasiwisata(`ID_Wisata`)
    )

7. transportPilihan(
        `ID_Riwayat` INTEGER,
        `ID_Transportasi` INTEGER,
        `Urutan` INTEGER,
        PRIMARY KEY(`ID_Riwayat`, `ID_Transportasi`, `Urutan`),
        FOREIGN KEY (`ID_Riwayat`) REFERENCES riwayatperjalanan(`ID_riwayat`),
        FOREIGN KEY (`ID_Transportasi`) REFERENCES transportasi(`ID_Transportasi`)
    )

## Pembuat Aplikasi
| NIM | Nama Lengkap |
| ------ | ---------- |
| 13521004 | Henry Anand Septian Radityo |
| 13521006 | Azmi Hasna Zahrani |
| 13521007 | Matthew Mahendra |
| 13521024 | Ahmad Nadil |
| 13521030 | Jauza Lathifah Annassalafi |

## Ucapan Terima kasih
Puji dan syukur kami panjatkan kepada Tuhan Yang Maha Esa, karena tanpa-Nya, tugas ini tidak dapat diselesaikan. Kepada Gagas P. Bahar yang telah mendampingi dalam proses asistensi pembuatan dokumen dari aplikasi ini. Kepada para dosen pengampu IF2250, Wikan Danar Sunindyo dan M. R. Al-ghazali yang telah membagikan ilmu tentang proses perancangan dan pembuatan perangkat lunak.