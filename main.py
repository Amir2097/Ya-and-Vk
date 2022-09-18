import requests
from Ya import YaUploader
from vk import VK
from pprint import pprint
import json
import time
from progress.bar import IncrementalBar



API_TOKEN = " "

vk_token = " "

size_dict = {}
'''Словарь, в котором ключ количество лайков, а значение размер'''
dict_images = {}
'''Словарь, в котором ключ количество лайков, а значение ссылка на фото для скачивания'''

def receiving_info(vk, dict_images = dict_images, size_dict = size_dict):
    '''Получаем лайки и максимальные размеры фото, в дальнейшем добавляя их в словари'''
    for vk_name in vk.photo_info()['response']['items']:

        for vk_name_size in vk_name['sizes']:
            dict_images[vk_name['likes']['count']] = vk_name_size['url']
            size_dict[vk_name['likes']['count']] = vk_name_size['type']
    return dict_images, size_dict


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
        return json.dump(list_json_photo, f, indent=2)



def progress_bar(bar_name):
    '''Функция прогресс бар'''
    mylist = [1,2,3,4,5,6,7]
    bar = IncrementalBar(bar_name, max = len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
    bar.finish()

def upload_photos_name(object_upload, path_name):
    '''Функция скачивает фото по ссылке в имеющемся словаре,
    прикрепленная к нашей программе, и выводит в название количество лайков'''
    for dict_photo_name, dict_photo_url in dict_images.items():
        object_upload.upload_photo(f'{path_name}/{dict_photo_name}.jpg', dict_photo_url)
        progress_bar('Upload photos name')



if __name__ == '__main__':
    ya = YaUploader(token=API_TOKEN)
    album_id = 'profile'
    owner_id = '133507957'
    vk = VK(vk_token, owner_id, album_id)
    receiving_info(vk)
    ya.new_folder(owner_id)
    upload_photos_name(ya, owner_id)
    file_recording_json('test.json', ya)
































