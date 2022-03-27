
print()
print("\t\t\t\t\t\t\t",32*"=")
print('''
                                                                Program Mengedit List
     ''')
print("\t\t\t\t\t\t\t",32*"=")
print()


dataBarang = []

Command = ''

## Saya akan menggunakan Function

# Batas
def garisBatas():
    print(40*"=")

# Fungsi stop 
def stopProgram():
    stop = input("Apakah ingin input ulang? y/t : ")

    if stop == 't':
        return True
    return False 

# Fungsi tambah data
def addData():
    print()
    while True: 
        data = input("Masukkan data : ")
        dataBarang.append(data)
        garisBatas()
        print(f"\t{data}, di tambahkan")  
        garisBatas()
        if stopProgram() == True:
            break


# Fungsi hapus data
def delData():
    while True:
        print()
        Del = int(input("Masukkan index data yg akan dihapus : "))
    
        if Del > (len(dataBarang) - 1):
            garisBatas()
            print('\tIndex belum ada pada list!')
            garisBatas()
        else:
            garisBatas()
            print('\t',dataBarang.pop(Del),",Terhapus")
            garisBatas()

        if stopProgram() == True:
            break

# Fugnsi mengedit barang
def editData():
    while True:
        # jadi kita akan masukkan index barang yang akan di edit
        edit = int(input("Barang yang akan diedit : "))
        
        if edit > (len(dataBarang) - 1):     
            garisBatas()
            print('\tIndex belum ada pada list!')
            garisBatas()
        else:
            garisBatas()
            dataBarang[edit] = input("\tMasukkan data baru : ")
            garisBatas()

        if stopProgram() == True:
            break


# Fungsi menampilkan semua barang
def echoData():
    print()
    print("\t\t DATA BARANG")
    print("\t",30*'-')
    print("\t   No\t |\t", "Nama Barang")
    print("\t",30*'-')

    for index, barang in enumerate(dataBarang):
        print(f"\t    {index+1}\t |\t {barang}")
        

    print("\t",30*'-')
    print()

# Fungsi untuk mengcek sebuah barang pada list.
def checkData():
    while True:
        cek = input("Masukkan data yang di cek : ")

        if cek in dataBarang:     
            garisBatas()
            print(f"\t{cek}, Ada di dalam list")
            garisBatas()
        else:
            garisBatas()
            print(f"\t{cek}, Belum ada di dalam list")
            garisBatas()

        if stopProgram() == True:
            break            


# Fungsi Mengcek index barang
def checkIndex():
    while True:
        cekIndex = input("Masukkan barang : ")

        if cekIndex in dataBarang:
            cek = dataBarang.index(cekIndex)
            garisBatas()
            print(f"\t{cekIndex}, ada pada index ke {cek}")
            garisBatas()
        else:
            garisBatas()
            print(f"\tIndex '{cekIndex}', Tidak ditemukan! ")
            garisBatas()

        if stopProgram() == True:
            break   

stop = False
while (not True): 
    print('''
                                                                    MENU PILIHAN
                                                        ====================================
                                                        ==   1. Tambahkan sebuah barang   ==
                                                        ==   2. Menghapus barang          ==
                                                        ==   3. Mengedit barang           ==
                                                        ==   4. Menampilkan semua barang  ==
                                                        ==   5. Mengecek sebuah barang    ==
                                                        ==   6. Mengecek index barang     ==
                                                        ==   0. Untuk Keluar.             ==
                                                        ====================================
    ''')


    Command = int(input("Masukkan pilihan diatas : "))

    # Menambah data
    if Command == 1:
        addData()
    
    # Menghapus data
    elif Command == 2:
        delData()
    
    # Mengedit data
    elif Command == 3:
        editData()
    
    # Menampilkan data
    elif Command == 4:
        echoData()

    # Mengcek barang
    elif Command == 5:
        checkData()

    # Mengcek index barang
    elif Command == 6:
        checkIndex()

    elif Command == 0:
        break
        
     else:
      print("Command Not Found !")


print()
print("\t\t\t\t\t\t\t  ",30*"=")
print("\t\t\t\t\t\t\t\t   PROGAM SELESAI")
print("\t\t\t\t\t\t\t  ",30*"=")
print()
