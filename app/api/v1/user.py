"""
 Created by 刘大怪 on 20-1-3
"""
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = "刘大怪"

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'I am ldh'
