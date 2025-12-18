

def penentu_pemenang(player, computer):
    penentu = f"player: {player} VS computer: {computer}"
    print(f"\n{'='*42}\n|{penentu:^40}|")

    if player == computer:
        print(f"|{"Hasil: Seri!":^40}|\n{'*'*42}")
    elif (player == 'batu' and computer == 'gunting') or \
         (player == 'gunting' and computer == 'kertas') or \
         (player == 'kertas' and computer == 'batu'):
        print(f"|{"Hasil: Kamu menang!":^40}|\n{'*'*42}")
    else:
        print(f"|{"Hasil: Komputer menang!":^40}|\n{'*'*42}")
