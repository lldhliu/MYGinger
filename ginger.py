"""
 Created by 刘大怪 on 20-1-3
"""
from app.app import create_app

__author__ = "刘大怪"

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
