def pilihan_pemain():
    pilihan = input("Pilih batu, gunting, atau kertas: ").lower()
    while pilihan not in ['batu', 'gunting', 'kertas']:
        pilihan = input("Pilihan tidak valid. Pilih batu, gunting, atau kertas: ").lower()
    return pilihan