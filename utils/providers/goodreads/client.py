from goodreads import client
from django.conf import settings

API_DOCS = 'https://www.goodreads.com/api'
USER_ID = '28892852'
class Client():


    def __init__(self):
        creds = settings.PROVIDER_CREDS 
        self.gc = client.GoodreadsClient(
            creds['goodreads']['key'], creds['goodreads']['secret'])
           
    def books_on_shelf_count(self, shelf_label):
        res = self.gc.request('shelf/list.xml',{'page':'1', 'user_id':USER_ID})
        for shelf in res['shelves']['user_shelf']:
            if shelf['name'] == shelf_label:
                return int(shelf['book_count']['#text'])
        
        return self.no_shelf_code

    @property
    def no_shelf_code(self):
        return '[no shelf]'