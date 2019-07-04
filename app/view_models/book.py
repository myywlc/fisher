"""
  Created by lin at 2019-06-09
"""


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.publisher = book['publisher']
        self.image = book['images']['large']
        self.price = book['price']
        self.isbn = book['isbn']
        self.summary = book['summary'] or ''
        self.pages = book['pages'] or ''
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intro)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = 1,
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = data['total'],
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'publisher': data['publisher'],
            'image': data['images']['large'],
            'price': data['price'],
            'summary': data['summary'] or '',
            'pages': data['pages'] or ''
        }
        return book
