//     “a project developed by MuratAlpTR”

import requests
import time

def boost_hours(game_id, steam_id, api_key):
    url = f"https://api.steampowered.com/IPlayerService/ReportPlayedGame/v1/?key={api_key}"
    data = {
        "steamid": steam_id,
        "appid": game_id,
        "playtime_2weeks": 60,  # Boost for 1 hour (adjust as needed)
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Hours boosted for game {game_id} on Steam ID {steam_id}")
    else:
        print(f"Error boosting hours: {response.text}")

if __name__ == "__main__":
    # Replace with your own values
    game_id_to_boost = 730  # Example: Counter-Strike: Global Offensive
    your_steam_id = "your_steam_id"
    your_api_key = "your_steam_web_api_key"

    while True:
        boost_hours(game_id_to_boost, your_steam_id, your_api_key)
        time.sleep(3600)  # Boost every hour


//     “a project developed by MuratAlpTR”
