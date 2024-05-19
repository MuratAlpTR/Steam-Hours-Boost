//     “a project developed by MuratAlpTR”

import time
from steam.client import SteamClient
from steam.enums import EResult

# Steam oturumu oluştur
client = SteamClient()

# Giriş bilgilerinizi ve shared secret'ınızı buraya girin
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
shared_secret = 'YOUR_SHARED_SECRET'

# Giriş fonksiyonu
def steam_login():
    result = client.login(username, password, two_factor_code=shared_secret)
    if result != EResult.OK:
        print(f'Giriş başarısız: {result}')
        return False
    print('Giriş başarılı')
    return True

# Oyun saatlerini artırma fonksiyonu
def boost_hours(app_id):
    print(f'{app_id} kimlikli oyunda saat artırma başlıyor...')
    while True:
        client.games_played([app_id])
        time.sleep(60)  # 1 dakika bekle (60 saniye)
        print(f'{app_id} kimlikli oyun için 1 saat eklendi')

# Ana fonksiyon
if __name__ == '__main__':
    if steam_login():
        app_id = 440  # Saat artırmak istediğiniz oyunun app_id'sini girin
        boost_hours(app_id)



//     “a project developed by MuratAlpTR”
