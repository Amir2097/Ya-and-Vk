import requests

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
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Использование метода ВК невозможно, ошибка: {response.status_code}!')