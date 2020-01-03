"""
 Created by 刘大怪 on 20-1-3
"""
from app.libs.redprint import Redprint

__author__ = "刘大怪"

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    # restful api: route 不能包含动词 比如 /get 就不太好
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'
