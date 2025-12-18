from player_choice import pilihan_pemain
from computer_choice import pilihan_komputer
from winner import penentu_pemenang

print(f"{'='*42}\n|{'Selamat datang di permainan':^40}|\n|{'Batu Gunting Kertas':^40}|\n{'='*42}\n")
print("Aturan permainan:\n- Batu mengalahkan Gunting\n- Gunting mengalahkan Kertas\n- Kertas mengalahkan Batu\n")
print(f"{'='*42}\n|{'mau main? (ya/tidak)':^40}|\n{'='*42}")

mulai_permainan = input().lower()
if mulai_permainan != 'ya':
    print(f"\n{'='*42}\n|{'Baik, terima kasih! Sampai jumpa lagi.':^40}|\n{'='*42}")
    exit()

class batu_gunting_kertas:
    def permainan(self):
        player = pilihan_pemain()
        komputer = pilihan_komputer()
        penentu_pemenang(player, komputer)
    
    def play_game(self):
        while True:
            self.permainan()
            play_again = input("next round? (ya/tidak): ").lower()
            if play_again != 'ya':
                break

# Jalankan permainan
if __name__ == "__main__":
    game = batu_gunting_kertas()
    game.play_game()
