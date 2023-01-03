from ensurepip import version
from os import stat, system
d_nama = []
d_tanggal=[]
d_kategori=[]

def judul():
    print ('=====kredit keaktifan mahasiwa=====')


def menu():
    system('cls')
    judul()
    print('1.menambah kegiatan')
    print('2.menampilkan jumlah poin')
    print('3.Keluar')
    print('=====================================')
    pilih2 = input('Pilihan anda : ')

    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        selesai()
    else:
        tidak = input('pilihan tidak tersedia mas broooo ')
        system('cls')
        menu()

def tambah():
    system('cls')
    judul()
    print('Tambah kegiatan'.center(40))

    kegiatan = input('Nama kegiatan: ')
    d_nama.append(kegiatan)
    tanggal= input('tanggal kegiatan: ')
    d_tanggal.append(tanggal)
    kategori=input('pilhan kategori kegiatan: \n-prestasi \n-organisasi \n-kepanitiaan \n-rekognisi \nmasukan kategori kegiatan : ')
    d_kategori.append(kategori)
    print ('kegiatan berhasil ditambah'.center(40))
    back = input('Kembali ke menu bosss pencet [enter]')
    menu()

def lihat():
    system('cls')
    judul()
    
    for i in range (len(d_nama)):

        print('%d. Nama kegiatan %s'%(i+0, d_nama[i]))
        print('tanggal  %s'%d_tanggal[i])
        print('kategori %s'%d_kategori[i])
        print('-------------------------------------')
    kembali = input('Kembali Tekan [enter]')
    menu()

def selesai():
    exit()

menu()