inventory = []

def create_item(kode, nama, kategori, stok, harga, status="Aktif", histori=None):
    if histori is None:
        histori = []
    for item in inventory:
        if item[0] == kode:
            return "Duplikasi kode_barang"
    new_item = [kode, nama, kategori, stok, harga, status, histori]
    inventory.append(new_item)
    return "Berhasil ditambah"

def read_items(filter_kategori=None):
    filtered = []
    for item in inventory:
        if item[5] == "Aktif" and (filter_kategori is None or item[2] == filter_kategori):
            filtered.append(item)
    if not filtered:
        print("Tidak ada barang yang sesuai.")
        return
    print("Daftar Barang:")
    print(f"{'Kode':<10} {'Nama':<20} {'Kategori':<15} {'Stok':<5} {'Harga':<10} {'Status':<10}")
    for item in filtered:
        print(f"{item[0]:<10} {item[1]:<20} {item[2]:<15} {item[3]:<5} {item[4]:<10} {item[5]:<10}")

def update_item(kode, new_nama=None, new_kategori=None, new_stok=None, new_harga=None):
    for item in inventory:
        if item[0] == kode:
            if new_nama: item[1] = new_nama
            if new_kategori: item[2] = new_kategori
            if new_stok: item[3] = new_stok
            if new_harga: item[4] = new_harga
            return "Berhasil diupdate"
    return "Barang tidak ditemukan"

def delete_item(kode):
    for item in inventory:
        if item[0] == kode:
            item[5] = "Tidak Aktif"
            return "Berhasil dihapus (soft delete)"
    return "Barang tidak ditemukan"

def sort_items(by="nama"):
    if by == "nama":
        inventory.sort(key=lambda x: x[1])
    elif by == "stok":
        inventory.sort(key=lambda x: x[3])
    print("Barang telah diurutkan.")

def search_items(keyword, by="kode"):
    results = []
    for item in inventory:
        if item[5] == "Aktif":
            if by == "kode" and keyword.lower() in item[0].lower():
                results.append(item)
            elif by == "nama" and keyword.lower() in item[1].lower():
                results.append(item)
    if not results:
        print("Tidak ada hasil pencarian.")
        return
    print("Hasil Pencarian:")
    print(f"{'Kode':<10} {'Nama':<20} {'Kategori':<15} {'Stok':<5} {'Harga':<10} {'Status':<10}")
    for item in results:
        print(f"{item[0]:<10} {item[1]:<20} {item[2]:<15} {item[3]:<5} {item[4]:<10} {item[5]:<10}")

def generate_report():
    total_nilai = 0
    low_stock = []
    for item in inventory:
        if item[5] == "Aktif":
            total_nilai += item[3] * item[4]
            if item[3] < 5:
                low_stock.append(item)
    print(f"Total Nilai Stok: {total_nilai}")
    if low_stock:
        print("Barang dengan stok < 5:")
        for item in low_stock:
            print(f"{item[0]} - {item[1]}: {item[3]}")
    else:
        print("Tidak ada barang dengan stok < 5.")

def restock_item(kode, jumlah):
    for item in inventory:
        if item[0] == kode and item[5] == "Aktif":
            item[3] += jumlah
            tanggal = datetime.date.today().isoformat()
            item[6].append([tanggal, jumlah])
            return "Berhasil direstock"
    return "Barang tidak ditemukan atau tidak aktif"


while True:
    print("\nMenu Sistem Manajemen Inventaris Coffee Shop:")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Sorting Barang")
    print("6. Searching Barang")
    print("7. Laporan")
    print("8. Restock Barang")
    print("9. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        kode = input("Kode Barang: ")
        nama = input("Nama Barang: ")
        kategori = input("Kategori: ")
        stok = int(input("Stok: "))
        harga = float(input("Harga Satuan: "))
        print(create_item(kode, nama, kategori, stok, harga))
    elif pilihan == "2":
        filter_kat = input("Filter kategori (kosongkan jika tidak): ")
        read_items(filter_kat if filter_kat else None)
    elif pilihan == "3":
        kode = input("Kode Barang: ")
        new_nama = input("Nama Baru (kosongkan jika tidak): ") or None
        new_kat = input("Kategori Baru (kosongkan jika tidak): ") or None
        new_stok = input("Stok Baru (kosongkan jika tidak): ")
        new_stok = int(new_stok) if new_stok else None
        new_harga = input("Harga Baru (kosongkan jika tidak): ")
        new_harga = float(new_harga) if new_harga else None
        print(update_item(kode, new_nama, new_kat, new_stok, new_harga))
    elif pilihan == "4":
        kode = input("Kode Barang: ")
        print(delete_item(kode))
    elif pilihan == "5":
        by = input("Sort by (nama/stok): ")
        sort_items(by)
    elif pilihan == "6":
        keyword = input("Kata kunci: ")
        by = input("Cari by (kode/nama): ")
        search_items(keyword, by)
    elif pilihan == "7":
        generate_report()
    elif pilihan == "8":
        kode = input("Kode Barang: ")
        jumlah = int(input("Jumlah Restock: "))
        print(restock_item(kode, jumlah))
    elif pilihan == "9":
        break
    else:
        print("Pilihan tidak valid.")
