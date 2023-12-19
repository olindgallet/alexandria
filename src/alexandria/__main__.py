#!/usr/bin/env python3

# Author: Olin Gallet
# Date:  18/12/2023
from flask import Flask
from flask import jsonify
from time import gmtime
from time import strftime
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=['GET'])
def server_stats():
    return jsonify({"time": strftime("%H:%M:%S", gmtime()), "date": strftime("%Y-%m-%d")}), 200

@app.route("/listmusic", methods=['GET'])
def list_music():
    return jsonify({"song": "Dab on da Haters", "artist": "Lil og"}), 200

@app.route("/listmovies", methods=['GET'])
def list_movies():
    return jsonify({"title": "Gone with the Wind"}), 200

@app.route("/listanime", methods=['GET'])
def list_anime():
    return jsonify({"title": "Gone with the Wind"}), 200

@app.route("/listbooks", methods=['GET'])
def list_books():
    return jsonify({"title": "Gone with the Wind"}), 200

@app.route("/listmanga", methods=['GET'])
def list_manga():
    return jsonify({"title": "Gone with the Wind"}), 200

def execute():
    serve(app, host='127.0.0.1', port=8080);

if __name__ == "__main__":
    execute()
    