import os
import matplotlib.pyplot as plt 
from prettytable import PrettyTable
os.system("cls")


# ----------------Dictionary-------------------
akun = {"nama":"nora", "PIN": 1234, "saldo" : 1200000, "e-pay":1200000, "member":"VIP"}
akun_admin =  {"nama":"aron", "PIN": 4321}
voucher = { 
    "jkt48": {"nama_voucher": "Diskon 11.11 30%", "persentase_diskon": 0.7, "status": "Aktif"},
    "avenger": {"nama_voucher": "Diskon spesial 50%", "persentase_diskon": 0.5, "status": "Aktif"},
    "2023": {"nama_voucher": "New Year", "persentase_diskon": 0.9, "status": "Tidak aktif"}
}


# --------------List Barang--------------------
barang = {
    1: {"ID": 1, "nama": "Teleskop Galileo Galilei (1609)", "harga": 3000000, "stok": 1},
    2: {"ID": 2, "nama": "Surat cinta era perang dunia ke-II (1914-1918)", "harga": 600000, "stok": 50},
    3: {"ID": 3, "nama": "Cincin emas Mesir kuno (1070-712 SM)", "harga": 2700000, "stok": 10},
    4: {"ID": 4, "nama": "The Da Vinci Globe (1504)", "harga": 2000000, "stok": 5},
    5: {"ID": 5, "nama": "Jam saku era perang dunia ke-II (1817)", "harga": 1200000, "stok": 15},
    6: {"ID": 6, "nama": "Lukisan Monalisa (1503-1506)", "harga": 100000000, "stok": 1},
    7: {"ID": 7, "nama": "Topeng Tutankhamun (1323 M)", "harga": 12000000, "stok": 1}
}


# ----------Variabel Keranjang------------
transaksi_produk =[]


# -------------Banner-----------------
print('''
+===========================================++=================================================+
|    --      -                 --     アンティークアーカイブス     --          -        --     - |
|                                🕰️     Antique Archives    🕰️                                |
|                   Jelajahi Koleksi Unik Kami dan Temukan Sejarah Tersembunyi                 |
+===========================================++=================================================+
    ''')



# ----------Func untuk Registrasi------------
def register():
    while True:
            print("""
            ++================++==================++
            |               REGISTER               |
            ++====================================++
            """)
            username= input("Masukkan username yang anda inginkan: ")
            pin = int(input("Masukkan PIN yang anda inginkan: "))
            
            #Update ke dictionary
            akun_baru = {
                "nama": username,
                "PIN": pin,
                "saldo": 0,
                "e-pay": 0,
                "member": "biasa"
                }
            akun.update(akun_baru)
            
            os.system("cls")
            print(f"\n Selamat, anda berhasil registrasi! Berikut deskripsi akun anda")
            print(f" Username: {username} \n PIN: {pin}")
            login()
            break



# --------------Func untuk Login--------------
def login():  
    while True:
        global username
        print("""
            ++===============++================++
            |               LOGIN               |
            ++=================================++
            """)
        username = input("Masukkan username anda: ")
        pin = int(input("Masukkan PIN anda: "))
        # Untuk mengecek
        if username == akun["nama"] and pin == akun["PIN"]:
            os.system("cls")
            main_program()
            break
        else:
            os.system("cls")
            print("\n!! Mohon masukkan username dan password yang sesuai. !!\n")
            break




# --------------Func Login Admin-----------------
def login_admin(): 
    while True: 
        print("""
            ++===============++================++
            |            LOGIN ADMIN            |
            ++=================================++
            """)
        username_admin = input("Masukkan username anda: ")
        pin_admin = int(input("Masukkan PIN anda: "))
        # Untuk mengecek
        if username_admin == akun_admin["nama"] and pin_admin == akun_admin["PIN"]:
            os.system("cls")
            program_admin()
            break
        else:
            print("\n!! Mohon masukkan username dan password yang sesuai. !!\n")
            os.system("cls")
            break





# --------------------Func untuk Transaksi-------------------
def beli():
    global transaksi_produk
    while True:
        os.system("cls")
        
        # Menampilkan Barang dalam Prettytable
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama Barang", "Harga", "Stok"]
        for item in barang.values():
            tabel.add_row([item["ID"], item["nama"], item["harga"], item["stok"]])
        print(tabel)

        beli_id = int(input("Silahkan pilih barang yang anda inginkan: "))
        total_dibeli = int(input("Silahkan masukkan jumlah barang yang dibeli: "))

        # Transaksi
        if 0 < beli_id <= len(barang):
            barang_dibeli = barang.get(beli_id)
            nama_barang = barang_dibeli.get("nama")
            harga_barang = barang_dibeli.get("harga")
            stok_barang = barang_dibeli.get("stok")
            
            total_harga = harga_barang*total_dibeli
            
                
            if total_dibeli > stok_barang:
                print("Maaf, stok barang tidak cukup")
                return
        
            # Jika member VIP
            if akun["member"] == "VIP":
                # Pilih metode bayar
                bayar = input(f"Anda akan membeli {nama_barang} dengan total harga IDR {total_harga*0.7} \nIngin bayar lewat apa, {username}? \n1. Saldo \n2. E-pay \n >")
                if bayar == "1" and (akun["member"] == "VIP" and akun["saldo"] >= total_harga):
                    harga_barang = int(total_harga*0.7)
                    akun["saldo"] -= harga_barang
                elif bayar == "2" and  (akun["member"] == "VIP" and akun["e-pay"] >= total_harga):
                    harga_barang = int(total_harga*0.7)
                    akun["e-pay"] -= harga_barang
                else:
                    print("Maaf, e-pay atau saldo tidak mencukupi...")
                    return
                
                
            # Jika member biasa
            elif akun["member"] != "VIP" and  (akun["e-pay"] >= total_harga):
                # Voucher
                pakai_voucher = str(input(f" \n Anda akan membeli {nama_barang} dengan total harga IDR {total_harga}. \nApakah anda ingin menggunakan voucher? (y untuk pakai voucher) \n >"))
                
                # Pakai voucher
                if pakai_voucher.lower() == "y":
                    masukkan_voucher = input("Masukkan Kode Voucher : ")

                    # Untuk mengecek kevalidan voucher
                    voucher_dipakai = voucher.get(masukkan_voucher)
                    if voucher_dipakai and voucher_dipakai.get("status") == "Aktif":
                        nama_voucher = voucher_dipakai["nama_voucher"]
                        diskon = voucher_dipakai["persentase_diskon"]

                        print(f"Anda memakai voucer {nama_voucher}")
                        harga_barang = int(total_harga*diskon)
                        akun["e-pay"] -= harga_barang
                    else:
                        print("Maaf, voucher tidak tersedia")
                        break
                        
                # Ga pake voucher
                else:
                    harga_barang = total_harga  
                    akun["e-pay"] -= harga_barang
                    
            else:
                print("Maaf, e-pay tidak mencukupi...")
                return

            # Update stok barang dan transaksi_produk
            stok_barang -= total_dibeli
            barang[beli_id]["stok"] = stok_barang
            transaksi_produk.append({"Nama Barang": nama_barang, "Jumlah": total_dibeli, "Harga": total_harga})

            os.system("cls")
            print(f"\nTransaksi anda berhasil. Berikut status akun anda\nJumlah saldo: IDR {akun['saldo']}\nE-pay: {akun['e-pay']}")
            
        else:
            print("Produk tidak tersedia")
            break
        
        # Pengecekan jika ingin melakukan transaksi lagi
        ulang = input("Apakah Anda ingin melakukan transaksi lagi? (y/n): ")
        if ulang.lower() != "y":
            os.system("cls")
            break   





# -------------------Func untuk Privillege------------------
def pameran():
    while True:
        os.system("cls")
        print(f"""
            Hai, {username}! Ada event pameran yang sedang berlangsung dan bisa kamu datangi lho!\n
            ++================+[ 📜 Event Pameran 📜 ]+===============++
            |           1. Leonardo da Vinci's Paintings (17/11)        |
            |       2. The Impressionism of Vincent Van Gogh (20/12)    |
            |                        3. Kembali                         |
            ++=========================================================++ 
            """)

        pameran = input("\n Ingin mengeksplor yang mana? : ")
        if pameran == "1" or pameran == "2":
            print(f"Kamu berhasil terdaftar! Kami tunggu kedatanganmu, {username}")
            break
        elif pameran == "3":
            break
        else:
            print("Maaf, event yang kamu maksud tidak ada...")




# -------------------Func untuk Langganan------------------
def langganan():
    while True:
        os.system("cls")
        print(f"""
        Halo, {username}! Apakah anda tertarik untuk menjelajahi sejarah lebih dalam lagi? \n
        ++========+[ - Paket Langganan Kami - ]+=========++
        |             1. IDR 250.000/bulan                |
        |             2. IDR 700.000/tahun                |
        |                  3. Kembali                     |
        ++===============================================++    
                """)
        
        langganan = input("Silahkan pilih paket langganan anda •ᴗ• : ")
        if langganan == "1" and akun["e-pay"] >= 250000:
            akun["e-pay"] = akun["e-pay"] - 250000
            status = {"member" : "VIP"}
            akun.update(status)
            print("Terima kasih sudah berlangganan!!")
            break
        elif langganan == "2" and akun["e-pay"] >= 700000:
            akun["e-pay"] = akun["e-pay"] - 700000
            status = {"member" : "VIP"}
            akun.update(status)
            print("Terima kasih sudah berlangganan!!")
            break
        elif langganan == "3":
            break 
        else:
            print("\nTolong masukkan input yang sesuai dan perhatikan apakah e-pay anda cukup :(")




# -------------------Func topup Saldo----------------------
def topup_saldo():
    while True:
        os.system("cls")
        print(f"""
        Halo, {username}! Berikut adalah status akun anda! \n Jumlah saldo: IDR {akun['saldo']} \n E-pay: IDR {akun['e-pay']}
        ++============+[ - Top Up Saldo - ]+=============++
        |                1. IDR 1.500.000                 |                
        |                2. IDR 5.000.000                 |
        |                3. IDR 7.500.000                 |
        |                4. Kembali                       |
        ++===============================================++    
                """)
        
        topup = input("Ingin Top Up berapa? (•ᴗ•) : ")
        if topup == "1":
            akun["saldo"] = akun["saldo"] + 1500000
        elif topup == "2":
            akun["saldo"] = akun["saldo"] + 5000000
        elif topup == "3":
            akun["saldo"] = akun["saldo"] + 7500000
        elif topup == "4":
            break
            
        os.system("cls")    
        print(f"Anda berhasil Top Up! Saldo anda IDR {akun['saldo']}")
        break





# --------------------Func topup epay----------------------
def topup_epay():
    while True:
        os.system("cls")
        print(f"""
        Halo, {username}! Berikut adalah status akun anda! \n Jumlah saldo: {akun['saldo']} \n E-pay: {akun['e-pay']}
        ++============+[ - Tukarkan Saldo ke E-pay - ]+=============++
        |                     1. IDR 1.500.000                       |                
        |                     2. IDR 5.000.000                       |
        |                     3. IDR 7.500.000                       |
        |                       4. Kembali                           |
        ++==========================================================++    
                """)
        topup = input("Ingin Top Up E-pay berapa? (•ᴗ•) : ")
            
        if topup == "1" and akun["saldo"] >= 1500000:
            akun["saldo"] -= 1500000
            akun["e-pay"] += 1500000
        elif topup == "2" and akun["saldo"] >= 5000000:
            akun["saldo"] -= 5000000
            akun["e-pay"] += 5000000
        elif topup == "3" and akun["saldo"] >= 7500000:
            akun["saldo"] -= 7500000
            akun["e-pay"] += 7500000
        elif topup == "4":
            break
        else: 
            print("\nTolong masukkan input yang sesuai dan perhatikan apakah saldo anda cukup")
            break      
        
        os.system("cls")
        print(f"Anda berhasil Top Up! E-pay anda IDR {akun['e-pay']}")
        break




# ------------------------Func untuk Melihat Chart-----------------------
def pie_chart(transaksi_produk):
    # Pie chart for total produk yang dibeli
    labels = [transaksi["Nama Barang"] for transaksi in transaksi_produk]
    quantity = [transaksi["Jumlah"] for transaksi in transaksi_produk]
    
    plt.title("Total Produk yang Dibeli")
    plt.pie(quantity, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.show()

def bar_chart(transaksi_produk):
    # Bar chart for uang masuk perusahaan
    nama_produk = [f"{transaksi['Nama Barang']} ({transaksi['Jumlah']})"  for transaksi in transaksi_produk]
    total_uang = [transaksi["Harga"] for transaksi in transaksi_produk]
    
    plt.figure(figsize=(12, 7))
    plt.title("Jumlah Uang Masuk Perusahaan Per Produk")
    plt.bar(nama_produk, total_uang, color="lightcoral")
    plt.ylabel("Total Uang (IDR)")
    plt.xlabel("Nama Produk")
    plt.xticks(size=12)
    plt.yticks(size=12)   
    

    plt.show()






# ------------------------------Program Admin------------------------------------
def program_admin():
    os.system("cls")
    while True:
        print("""
            ++==========+[ ~ Menu Admin ~ ]+==========++
            |        1. Total produk yang dibeli       |
            |         2. Uang masuk perusahaan         |       
            |               3. Kembali                 |
            ++========================================++
                """)
        
        pilih_admin = input(f"Mau ngapain min? \n>")
        if pilih_admin == "1":
            print("\n[INFO] Menampilkan Pie Chart: Total Produk yang Dibeli\n")
            pie_chart(transaksi_produk)
        elif pilih_admin == "2":
            print("\n[INFO] Menampilkan Bar Chart: Jumlah Uang Masuk Perusahaan Per Produk\n")
            bar_chart(transaksi_produk)
        elif pilih_admin =="3":
            os.system("cls")
            menu_akun()
            break
        elif pilih_admin == "4":
            print("""
            ++==========================+[ - Bye - bye - ]+============================++
            | Terima kasih sudah berbelanja, kami tunggu kedatangan anda kembali! (>ᴗ<) |
            ++=========================================================================++
                """)
            quit()




# -------------------------------------Main Program ------------------------------------------
def main_program():
    while True:
        print(f"\n Selamat datang, {username}! Selamat berkelana di dalam sejarah ~ ")

        # Menu VIP
        if akun["member"] == "VIP":
            print("""
            ++=========+[ 👑 Menu VIP 👑 ]+==========++
            |             1. Beli Barang              |
            |             2. Tiket Pameran            |
            |             3. Top Up Saldo             |
            |             4. Tukarkan Saldo           |
            |              5. Kembali                 |
            |               6. Exit                   |
            ++=======================================++
                """)
        # Menu Biasa
        else:
            print("""
            ++=========+[ ~ Menu Pembeli ~ ]+=========++
            |             1. Beli Barang               |
            |             2. Beli Member               |
            |             3. Top Up Saldo              |
            |            4. Tukarkan Saldo             |
            |               5. Kembali                 |
            |                6. Exit                   |
            ++========================================++
                """)

        pilih = input("Anda ingin apa hari ini? \n >")

        # Beli barang
        if pilih == "1":
            beli()

        # Beli member
        elif pilih == "2":
            # Menu pameran jika VIP
            if akun["member"] == "VIP":
                pameran()
            # Menu Langganan VIP
            else:
                langganan()

        # Menu Top Up
        elif pilih == "3":
            topup_saldo()

        # Top Up E-pay
        elif pilih == "4":
            topup_epay()
            
        # Kembali ke menu awal
        elif pilih == "5":
            menu_akun()
            
        # Chart
        elif pilih == "6":
            print("""
            ++==========================+[ - Bye - bye - ]+============================++
            | Terima kasih sudah berbelanja, kami tunggu kedatangan anda kembali! (>ᴗ<) |
            ++=========================================================================++
                """)
            quit()
        else:
            print("Mohon masukkan pilihan yang tersedia")
    




# ----------------------------------------Menu Akun -------------------------------------------------
def menu_akun():
    while True:
        print('''
        ++========+[ ~ Selamat datang ~ ]+========++
        |               1. Register                |
        |                2. Login                  |
        |              3. Login Admin              |
        |                4. Exit                   |
        ++========================================++
            \n''')
        masuk = input("Masukkan pilihan anda: ")

        if masuk == "1":
            register()
        elif masuk == "2":
            login()
            break
        elif masuk == "3":
            login_admin()
        elif masuk == "4":
            print("""
            ++==========================+[ - Bye - bye - ]+============================++
            | Terima kasih sudah berbelanja, kami tunggu kedatangan anda kembali! (>ᴗ<) |
            ++=========================================================================++
                """)
            quit()
        else:
            print("Tolong masukkan 1/2/3/4")
            
# Menjalankan program
menu_akun()






"""
Nama: Naura Syawal Athallah Putri
Kelas: Sistem Informasi A
NIM: 2309116032
"""