import requests

class YaUploader:
    '''Класс для загрузки фото на Яндекс диск с помощью токена'''
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def new_folder(self, path):
        '''Функция создает папку в Яндекс диске'''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.path = path
        params = {'path': self.path}
        headers = self.get_headers()
        response = requests.put(upload_url, headers=headers, params=params)
        if response.status_code == 201:
            return response.json()
        else:
            print(f'Добавление новой папки невозможно, ошибка: {response.status_code}!')


    def upload_photo(self, path, url_photo):
        '''Функция загружает фото по ссылке'''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.path = path
        self.url_photo = url_photo
        headers = self.get_headers()
        params = {'path': self.path, 'url': self.url_photo}
        response = requests.post(upload_url, headers=headers, params=params)
        if response.status_code == 202:
            return response.json()
        else:
            print(f'Скачивание фото невозможно, ошибка: {response.status_code}!')


    def resources_photo(self):
        '''Функция для получения информации файлов на диске'''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'
        headers = self.get_headers()
        response = requests.get(upload_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Получение информации невозможно, ошибка: {response.status_code}!')
