
from icrawler.builtin import GoogleImageCrawler
import os
import random

# Proxy list
proxies = [

    "142.54.239.1:4145", "45.191.12.6:4153", "50.250.205.21:32100", "85.117.69.253:1080",
    "176.118.232.12:5678", "213.184.242.144:1337", "170.233.30.33:4153", "51.15.210.190:16379",
    "192.95.33.162:10974", "51.159.59.154:1080", "36.66.170.25:4153", "193.105.62.11:58973",
    "116.107.184.60:1080", "31.211.142.115:8192", "190.144.224.182:44550", "142.54.226.214:4145",
    "92.255.190.64:4153", "103.148.112.69:8199", "163.172.144.96:16379", "212.50.19.150:4153",
    "209.97.169.41:13108", "185.59.100.55:1080", "198.199.86.11:1080", "8.220.194.115:1080",
    "91.185.236.24:4145", "185.139.56.133:4145", "49.0.156.20:32000", "178.33.164.238:64958",
    "191.37.156.29:5678", "103.141.66.78:2005", "98.175.31.195:4145", "142.54.236.97:4145",
    "72.214.108.67:4145", "51.15.206.101:16379", "103.155.198.109:8199", "85.172.1.30:1080",
    "67.201.58.190:4145", "27.147.221.140:5678", "142.54.228.193:4145", "31.42.185.134:1080",
    "141.105.107.152:5678", "8.218.39.40:10800", "212.47.226.225:16379", "46.146.210.123:1080",
    "8.215.47.191:10080", "212.124.22.245:1080", "68.71.242.118:4145", "51.15.232.175:16379",
    "36.94.100.114:1080", "80.78.78.106:65530", "187.17.201.203:38737", "3.147.60.84:3128",
    "184.149.25.55:5678", "185.14.149.33:4145", "91.221.177.40:80", "93.157.193.139:5678",
    "103.189.218.158:1080", "117.216.46.148:1080", "103.37.82.134:39873", "103.81.194.164:4444",
    "213.250.198.146:7777", "36.93.197.180:5678", "35.152.137.65:26038", "103.160.57.171:10101",
    "109.224.12.170:52015", "138.186.155.1:1085", "54.180.239.137:28136", "122.54.86.40:5678",
    "79.106.170.126:4145", "94.23.222.122:14822", "91.228.245.196:60606", "103.155.167.217:1080",
    "103.191.196.71:8199", "90.182.147.170:4145", "194.164.125.208:57422", "187.63.9.62:63253",
    "103.97.94.22:4153", "82.137.250.156:4145", "91.121.173.38:54233", "89.250.148.158:1080",
    "84.52.123.163:4145", "110.39.40.118:1088", "195.39.233.14:44567", "200.105.252.170:5678",
    "103.81.194.120:8888", "51.158.71.156:16379", "72.37.217.3:4145", "107.152.98.5:4145",
    "103.58.16.106:4145", "69.49.234.59:55804", "24.249.199.12:4145", "116.118.98.25:5678",
    "43.231.78.170:1080", "103.245.205.26:6969", "103.163.244.106:1080", "67.225.137.108:61891",
    "180.94.28.237:999", "103.247.120.51:10800", "8.218.82.179:8888", "85.117.69.251:1080",
    "115.127.124.234:1080", "116.106.108.136:1080", "193.33.153.47:1080", "102.39.157.235:1080",
    "95.164.0.177:36352", "103.154.113.242:4153", "99.56.147.242:53096", "212.220.13.98:4153",
    "8.218.217.168:8888", "176.235.182.84:1080", "139.59.205.148:12040", "3.22.79.220:20919",
    "77.238.245.102:1080", "58.27.203.108:5678", "108.136.220.77:4005", "62.201.233.59:4145",
    "95.182.78.9:5678", "47.254.36.213:104", "185.133.239.244:16299", "188.113.168.37:3629",
    "46.147.65.44:61986", "46.98.200.67:5678", "91.222.173.230:1080", "161.49.176.173:1338",
    "103.247.14.37:8199", "47.74.46.81:9098", "181.204.4.74:5678", "103.18.47.79:4145",
    "103.160.205.38:8080", "50.96.204.252:18351", "186.224.225.82:42648", "81.177.224.173:1337",
    "8.213.129.20:3127", "41.70.106.1:5678", "45.238.57.1:3629", "46.229.66.241:1080",
    "212.31.100.138:4153", "200.81.122.235:4153", "185.43.249.148:39316", "185.151.86.86:3699",
    "24.37.245.42:51056", "138.59.177.117:5678", "50.235.117.234:39593", "23.227.203.202:9150",
    "8.217.241.28:8888", "47.91.121.127:36389", "3.101.76.84:18242", "120.50.1.126:1088",
    "95.163.152.34:1890", "103.55.22.247:8199", "77.46.138.1:33608", "109.69.0.179:5678",
    "195.66.210.177:1080", "45.116.114.37:5678", "103.141.148.62:5678", "91.150.77.57:56921",
    "103.109.2.94:4153", "45.249.78.177:5678", "92.241.92.218:14888", "194.1.188.8:60606",
    "185.128.153.75:33333", "27.123.254.158:6969", "217.219.162.114:5678", "194.150.71.227:4153",
    "198.177.125.181:46549", "52.210.15.148:3128", "108.175.24.1:13135", "15.168.175.83:3128",
    "47.252.11.233:8080", "162.144.33.230:19829", "171.248.221.86:1080", "61.7.147.227:4145",
    "102.64.116.1:4145", "213.147.123.39:1080", "176.236.14.2:4153", "202.131.235.138:4153",
    "185.54.178.193:1080", "3.141.38.145:3128", "93.117.72.27:55770", "80.78.74.66:65530",
    "94.142.136.101:4444", "103.146.185.34:1083", "103.162.50.13:6969", "185.191.165.28:1080",
    "131.161.68.41:35944", "182.253.140.250:5678", "8.220.141.8:8443", "146.196.63.235:4145",
    "79.101.45.94:56921", "201.184.239.75:5678", "185.190.90.2:4145", "82.132.19.108:4153",
    "68.71.245.206:4145", "46.29.116.6:4145", "65.49.67.161:48324", "161.97.163.52:54450",
    "202.166.217.154:48293", "203.150.128.210:5678", "94.159.106.252:1080", "51.158.65.148:16379",
    "202.51.103.154:5678", "49.156.44.130:48293", "143.137.198.204:5678", "103.41.32.250:51951",
    "212.47.251.132:16379", "202.142.178.206:1080", "141.94.195.25:22563", "163.172.185.252:16379",
    "174.75.211.222:4145", "160.19.16.86:1080", "212.47.253.24:16379", "103.81.194.167:4444",
    "192.111.139.162:4145", "95.43.244.15:4153", "36.89.56.127:5678", "98.181.137.83:4145",
    "95.67.72.138:1080", "124.158.149.66:4153", "200.125.40.38:5678", "192.111.137.34:18765",
    "103.172.70.237:12", "160.22.22.85:5678", "163.172.190.59:16379", "212.47.249.156:16379",
    "51.158.125.47:16379", "1.179.151.165:31948", "178.44.118.116:1080", "38.188.52.210:1080",
    "41.186.174.167:1088", "168.228.71.251:4153", "46.175.253.125:1080", "72.205.0.67:4145",
    "72.195.34.58:4145", "184.170.251.30:11288", "116.118.98.21:5678", "185.244.77.62:1080",
    "5.157.64.213:1080", "184.178.172.13:15311", "202.123.183.66:5678", "192.111.138.29:4145",
    "82.130.202.219:43429", "163.53.180.115:60606", "183.80.54.224:1080", "75.41.145.46:5678",
    "184.170.248.5:4145", "115.23.88.118:56452", "183.88.219.206:34676", "13.221.134.55:3128"
]

def download_images(keyword, folder, max_num=100):
    os.makedirs(f'images/{folder}', exist_ok=True)
    
    # Try multiple proxies until successful download
    max_proxy_attempts = 5
    successful_download = False
    
    for attempt in range(max_proxy_attempts):
        # Randomly select a proxy
        proxy = random.choice(proxies)
        print(f"Attempt {attempt + 1}: Using proxy {proxy} for {keyword}")
        
        try:
            # Import required modules
            import requests
            from icrawler.builtin import GoogleImageCrawler
            
            # Create crawler with custom downloader configuration
            crawler = GoogleImageCrawler(
                storage={'root_dir': f'images/{folder}'},
                downloader_cls_config={
                    'session_config': {
                        'proxies': {
                            'http': f'http://{proxy}',
                            'https': f'http://{proxy}'
                        },
                        'timeout': 15
                    }
                }
            )
            
            crawler.crawl(keyword=keyword, max_num=max_num)
            print(f"✓ Successfully downloaded images for {keyword} using proxy {proxy}")
            successful_download = True
            return
            
        except Exception as e:
            print(f"✗ Proxy {proxy} failed for {keyword}: {str(e)[:100]}...")
            
            # If this was the last attempt, try without proxy
            if attempt == max_proxy_attempts - 1:
                print(f"All {max_proxy_attempts} proxy attempts failed for {keyword}. Trying without proxy...")
                try:
                    crawler = GoogleImageCrawler(
                        storage={'root_dir': f'images/{folder}'}
                    )
                    crawler.crawl(keyword=keyword, max_num=max_num)
                    print(f"✓ Successfully downloaded images for {keyword} without proxy")
                    successful_download = True
                    return
                except Exception as final_e:
                    print(f"✗ Failed to download {keyword} even without proxy: {str(final_e)[:100]}...")
                    print(f"Skipping {keyword} and moving to next location")
                    return
            else:
                print(f"Retrying with different proxy...")
                continue

download_images("Sigiriya, Sri Lanka", "sigiriya", max_num=150)
download_images("Anuradhapura, Sri Lanka", "anuradhapura", max_num=150)
download_images("Polonnaruwa, Sri Lanka", "polonnaruwa", max_num=150)
download_images("Dambulla Cave Temple, Sri Lanka", "dambulla_cave_temple", max_num=150)
download_images("Kandy Temple of Tooth, Sri Lanka", "kandy_temple_of_tooth", max_num=150)
download_images("Galle Fort, Sri Lanka", "galle_fort", max_num=150)
download_images("Ritigala, Sri Lanka", "ritigala", max_num=150)
download_images("Mihintale, Sri Lanka", "mihintale", max_num=150)
download_images("Medirigiriya Vatadage, Sri Lanka", "medirigiriya_vatadage", max_num=150)
download_images("Buduruwagala, Sri Lanka", "buduruwagala", max_num=150)
download_images("Yapahuwa, Sri Lanka", "yapahuwa", max_num=150)
download_images("Kadurugoda Temple, Sri Lanka", "kadurugoda_temple", max_num=150)
download_images("Batticaloa Dutch Fort, Sri Lanka", "batticaloa_dutch_fort", max_num=150)
download_images("Ella Nine Arches Bridge, Sri Lanka", "ella_nine_arches_bridge", max_num=150)
download_images("Nuwara Eliya, Sri Lanka", "nuwara_eliya", max_num=150)
download_images("Horton Plains, Sri Lanka", "horton_plains", max_num=150)
download_images("World's End, Sri Lanka", "world's_end", max_num=150)
download_images("Adams Peak, Sri Lanka", "adams_peak", max_num=150)
download_images("Knuckles Mountain Range, Sri Lanka", "knuckles_mountain_range", max_num=150)
download_images("Yala National Park, Sri Lanka", "yala_national_park", max_num=150)
download_images("Udawalawe National Park, Sri Lanka", "udawalawe_national_park", max_num=150)
download_images("Sinharaja Forest, Sri Lanka", "sinharaja_forest", max_num=150)
download_images("Bambarakanda Falls, Sri Lanka", "bambarakanda_falls", max_num=150)
download_images("Ravana Falls, Sri Lanka", "ravana_falls", max_num=150)
download_images("Kalpitiya Lagoon, Sri Lanka", "kalpitiya_lagoon", max_num=150)
download_images("Mannar Island, Sri Lanka", "mannar_island", max_num=150)
download_images("Pigeon Island, Sri Lanka", "pigeon_island", max_num=150)
download_images("Gal Oya National Park, Sri Lanka", "gal_oya_national_park", max_num=150)
download_images("Belihuloya, Sri Lanka", "belihuloya", max_num=150)
download_images("Meemure, Sri Lanka", "meemure", max_num=150)
download_images("Kanneliya Rainforest, Sri Lanka", "kanneliya_rainforest", max_num=150)
download_images("Ruwanwelisaya Stupa, Sri Lanka", "ruwanwelisaya_stupa", max_num=150)
download_images("Kelaniya Raja Maha Vihara, Sri Lanka", "kelaniya_raja_maha_vihara", max_num=150)
download_images("Sri Maha Bodhi Tree, Sri Lanka", "sri_maha_bodhi_tree", max_num=150)
download_images("Kataragama Temple, Sri Lanka", "kataragama_temple", max_num=150)
download_images("Nagadeepa Viharaya, Sri Lanka", "nagadeepa_viharaya", max_num=150)
download_images("Muthiyangana Raja Maha Viharaya, Sri Lanka", "muthiyangana_raja_maha_viharaya", max_num=150)
download_images("Munneswaram Temple, Sri Lanka", "munneswaram_temple", max_num=150)
download_images("St. Anne’s Church Talawila, Sri Lanka", "st._annes_church_talawila", max_num=150)
download_images("Dewatagaha Mosque, Sri Lanka", "dewatagaha_mosque", max_num=150)
download_images("Unawatuna Beach, Sri Lanka", "unawatuna_beach", max_num=150)
download_images("Mirissa Beach, Sri Lanka", "mirissa_beach", max_num=150)
download_images("Tangalle Beach, Sri Lanka", "tangalle_beach", max_num=150)
download_images("Trincomalee Beach, Sri Lanka", "trincomalee_beach", max_num=150)
download_images("Pasikudah Beach, Sri Lanka", "pasikudah_beach", max_num=150)
download_images("Arugam Bay, Sri Lanka", "arugam_bay", max_num=150)
download_images("Kalutara Beach, Sri Lanka", "kalutara_beach", max_num=150)
download_images("Bentota Beach, Sri Lanka", "bentota_beach", max_num=150)
download_images("Mount Lavinia Beach, Sri Lanka", "mount_lavinia_beach", max_num=150)
download_images("Hikkaduwa Beach, Sri Lanka", "hikkaduwa_beach", max_num=150)
download_images("Delft Island, Sri Lanka", "delft_island", max_num=150)
download_images("Colombo Lotus Tower, Sri Lanka", "colombo_lotus_tower", max_num=150)
download_images("Independence Square Colombo, Sri Lanka", "independence_square_colombo", max_num=150)
download_images("Gangaramaya Temple, Sri Lanka", "gangaramaya_temple", max_num=150)
