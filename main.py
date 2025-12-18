from player_choice import pilihan_pemain
from computer_choice import pilihan_komputer

class batu_gunting_kertas:
    def permainan(self):
        player = pilihan_pemain()
        komputer = pilihan_komputer()
    
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