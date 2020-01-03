"""
 Created by 刘大怪 on 20-1-3
"""
from flask import Blueprint
from app.api.v1 import user, book

__author__ = "刘大怪"


# v1 版本蓝图注册
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1
