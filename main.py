author = 'Syamsul ANdry'
email = 'syamsulandry@gmail.com'
app_title = 'Menggunakan Python Requests untuk Memanggil Django API'
print(f'{app_title}) oleh {author}')

url = 'http://127.0.0.1:8000'
import requests

response = requests.get(url)
print(response)
if response.status_code == 200:
    print('Koneksi Berhasil!')

    url_api = f'{url}api/v1/stats/'
    response = requests.get(url_api)
    if response.status_code == 200:
        print(response.text)

        import json

        Hasil: [{"id":1,"suhu:10.0"}]

        data =json.lads(response.text)
        data_terakhir = data[len(data) - 1]
        suhu = data_terakhir
        Humidity = data_terakhir['humidity']
        print(f'Hasil pe,bacaan sensor: Suhu={suhu}, humidity = {humidity}')
