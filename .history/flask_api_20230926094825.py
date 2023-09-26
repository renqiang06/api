# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# CHATGPT使用地址 https://c.binjie.fun/
# %% flask api

from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)
db_path = '../Data_backup.db'  # 数据库文件路径

@app.route('/random_poem', methods=['GET'])
def get_random_poem():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT content FROM poems ORDER BY RANDOM() LIMIT 1")
    result = c.fetchone()

    conn.close()

    if result:
        return jsonify({'poem': result[0]})
    else:
        return jsonify({'error': 'No poem found'})

if __name__ == '__main__':
    app.run()
