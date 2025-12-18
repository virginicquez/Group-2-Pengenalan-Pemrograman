def penentu_pemenang(player, computer):
    print(f"Pemain memilih: {player}")
    print(f"Komputer memilih: {computer}")
    
    if player == computer:
        print("Hasil: Seri!")
    elif (player == 'batu' and computer == 'gunting') or \
         (player == 'gunting' and computer == 'kertas') or \
         (player == 'kertas' and computer == 'batu'):
        print("Hasil: Kamu menang!")
    else:
        print("Hasil: Komputer menang!")
