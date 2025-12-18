def pilihan_pemain():
    print(f"\n{'='*42}\n|{'Pilih batu, gunting, atau kertas':^40}|\n{'='*42}")
    
    pilihan = input().lower()
    while pilihan not in ['batu', 'gunting', 'kertas']:
        print(f"\n{'='*42}\n|{'input tidak valid':^40}|\n|{'Pilih batu, gunting, atau kertas':^40}|\n{'='*42}")
        pilihan = input().lower()
    return pilihan
