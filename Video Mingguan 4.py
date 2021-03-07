#Andreas Nugroho
#71200646

# edo bekerja di salah satu kasir minimarket. edo sedang membuat rekap harga, yang meliputi banyak perubahan harga , rata-rata perubahan, harga tertinggi,
# dan terendah dari perubahan harga. bantulah edo membuat program rekap data agar memudahkan edo untuk bekerja. 

#input 
#banyaknya perubahan yang akan di lakukan
#harga yang di inputkan oleh user

#proses
# rata rata = jumlah perubahan harga selurahnya / banyaknya perubahan harga
# max
# min

#ouput
# Banyaknya perubahan harga (kali)
# Harga tertinggi (Rp.)
# Harga terendah (Rp.)
# Rata rata (Rp.)

def hitung():
    updateharga = []
    banyak = int(input("Masukkan Banyaknya Perubahan Harga = "))

    for i in range(banyak):
        harga = int(input("Harga saat ini dalam rupiah = Rp."))
        updateharga.append(harga)

    print("Banyak perubahan harga =",banyak,"kali")
    print("Harga Tertinggi = Rp.",max(updateharga))
    print("Harga Terendah = Rp.",min(updateharga))
    print("Rata - rata Harga = Rp.",sum(updateharga)//banyak)

    lagi = input("Apakah anda akan menggunakan program ini kembali?(yes/no)").lower()
    if lagi == "yes":
        hitung()
    elif lagi == "no":
        exit()
    else:
        print("Inputan Salah!!!")

hitung()