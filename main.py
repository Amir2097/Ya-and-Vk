with open('my_tk.txt', 'r') as file_vk:
    token_vk = file_vk.read().strip()

import requests
from pprint import pprint
import json
import time
from progress.bar import IncrementalBar

def progress_bar(bar_name):
    '''Функция прогресс бар'''
    mylist = [1,2,3,4,5,6,7]
    bar = IncrementalBar(bar_name, max = len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
    bar.finish()

class VK:
    '''Создание класса ВК для инициализации токена и получение фото по id и идентификатора альбома'''

    def __init__(self, token_vk, owner_id, album_id, extended = '1', version='5.131'):
        '''Инициализация'''
        self.token = token_vk
        self.id = owner_id
        self.album_id = album_id
        self.extended = extended
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}


    def photo_info(self):
        '''Использование метода Вк'''
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': self.album_id, 'extended': self.extended}
        response = requests.get(url, params={**self.params, **params})
        progress_bar('Photo info vk')
        return response.json()



size_dict = {}
'''Словарь, в котором ключ количество лайков, а значение размер'''
dict_images = {}
'''Словарь, в котором ключ количество лайков, а значение ссылка на фото для скачивания'''


def receiving_info(vk, dict_images = dict_images, size_dict = size_dict):
    '''Получаем лайки и максимальные размеры фото, в дальнейшем добавляя их в словарь'''
    for vk_name in vk.photo_info()['response']['items']:

        for vk_name_size in vk_name['sizes']:

            if vk_name_size['type'] == 'w':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'z':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'y':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'r':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'q':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'p':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'o':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'x':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 'm':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']

            elif vk_name_size['type'] == 's':
                dict_images[vk_name['likes']['count']] = vk_name_size['url']
                size_dict[vk_name['likes']['count']] = vk_name_size['type']
    progress_bar('Receiving photo')
    return dict_images, size_dict




API_TOKEN = " "

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
        progress_bar('Yandex new folder')
        return response.json()


    def upload_photo(self, path, url_photo = dict_images):
        '''Функция загружает фото по ссылке'''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.path = path
        self.url_photo = url_photo
        headers = self.get_headers()
        params = {'path': self.path, 'url': self.url_photo}
        response = requests.post(upload_url, headers=headers, params=params)
        progress_bar('Upload photo')
        return response.json()

    def resources_photo(self):
        '''Функция для получения информации файлов на диске'''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'
        headers = self.get_headers()
        response = requests.get(upload_url, headers=headers)
        progress_bar('Resources photo')
        return response.json()


def file_recording_json(name_file, object_record, type = 'w'):
    '''Функция для записи данных в файл json, обращаясь к данным, которые имеются'''
    with open(name_file, type) as f:
        list_json_photo = []
        '''Создание циклов для записи данных в файл json'''
        for name_resources_photo in object_record.resources_photo()['items']:

            for name_photo in dict_images.keys():
                new_dict_json = {}
                if str(name_photo) in name_resources_photo['name']:
                    new_dict_json['file name'] = name_resources_photo['name']
                    for likes_name_photo, likes_name_size in size_dict.items():
                        if name_photo == likes_name_photo:
                            new_dict_json['size'] = likes_name_size
                            list_json_photo.append(new_dict_json)
        progress_bar('File recording json')
        return json.dump(list_json_photo, f, indent= 2)

def upload_photos_name(object_upload):
    '''Функция скачивает фото по ссылке в имеющемся словаре,
    прикрепленная к нашей программе, и выводит в название количество лайков'''
    for dict_photo_name, dict_photo_url in dict_images.items():
        object_upload.upload_photo(f'{owner_id}/{dict_photo_name}.jpg', dict_photo_url)
    progress_bar('Upload photos name')



if __name__ == '__main__':
    ya = YaUploader(token=API_TOKEN)
    album_id = 'profile'
    owner_id = '133507957'
    vk = VK(token_vk, owner_id, album_id)
    pprint(receiving_info(vk))
    ya.new_folder(owner_id)
    upload_photos_name(ya)
    file_recording_json('test.json', ya)
































