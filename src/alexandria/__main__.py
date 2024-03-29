#!/usr/bin/env python3

# Author: Olin Gallet
# Date:  18/12/2023
from flask import Flask
from flask import jsonify
from flask import Response
from flask_caching import Cache
from time import strftime
from waitress import serve
from plumbum import local
from plumbum import colors
from dotenv import load_dotenv
from dotenv import find_dotenv
import sys
import os
import os.path
import json
from json.decoder import JSONDecodeError

_MOVIE_PATH_KEY   = 'MOVIE_PATH'
_TV_SHOW_PATH_KEY = 'TV_SHOW_PATH'

_NO_MOVIE_DB_RESPONSE = Response("{'message':'No movie db available.'}", status=404, mimetype='application/json')
_NO_TV_SHOW_DB_RESPONSE = Response("{'message':'No TV show db available.'}", status=404, mimetype='application/json')

_ALERT_COLOR = colors.orchid
_MESSAGE_COLOR = colors.blue
_SUCCESS_COLOR = colors.yellow
_ERROR_COLOR = colors.red

_CACHE_TIMEOUT = 43200 # 60 seconds x 60 minutes x 12 hours

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route("/", methods=['GET'])
def server_stats():
    return jsonify({"time": strftime("%H:%M:%S"), "date": strftime("%Y-%m-%d")}), 200

@app.route("/listmusic", methods=['GET'])
def list_music():
    return jsonify({"song": "Dab on da Haters", "artist": "Lil og"}), 200

@app.route("/listmovies", methods=['GET'])
@cache.memoize(_CACHE_TIMEOUT)
def list_movies():
    response = _NO_MOVIE_DB_RESPONSE
    if _MOVIE_PATH_KEY in os.environ and os.path.exists(os.environ[_MOVIE_PATH_KEY]):
        try:
            with open(os.environ[_MOVIE_PATH_KEY], 'r') as movies_file:
                movie_data = json.dumps(json.load(movies_file))
                response = Response(response=movie_data, status=200, mimetype='application/json')
        except IOError:
            pass
        except JSONDecodeError:
            pass
    return response

@app.route("/listtvshows", methods=['GET'])
@cache.memoize(_CACHE_TIMEOUT)
def list_tv_shows():
    response = _NO_TV_SHOW_DB_RESPONSE
    if _MOVIE_PATH_KEY in os.environ and os.path.exists(os.environ[_TV_SHOW_PATH_KEY]):
        try:
            with open(os.environ[_TV_SHOW_PATH_KEY], 'r') as tv_shows_file:
                tv_shows_data = json.dumps(json.load(tv_shows_file))
                response = Response(response=tv_shows_data, status=200, mimetype='application/json')
        except IOError:
            pass
        except JSONDecodeError:
            pass
    return response
    
@app.route("/listanime", methods=['GET'])
def list_anime():
    return jsonify({"title": "Gone with the Wind"}), 200

@app.route("/listbooks", methods=['GET'])
def list_books():
    return jsonify({"title": "Gone with the Wind"}), 200

@app.route("/listmanga", methods=['GET'])
def list_manga():
    return jsonify({"title": "Gone with the Wind"}), 200

def _parse_env(location: str):
    '''
        Parses the environment file at the given location.
        location: the location of the environment file.
    '''
    load_dotenv(find_dotenv(location))
    print(_ALERT_COLOR | '[--LOADING FILE DATA--]')
    if _MOVIE_PATH_KEY in os.environ and os.path.exists(os.environ[_MOVIE_PATH_KEY]):
        print()
        print(_MESSAGE_COLOR | f'Movie DB found: {os.environ[_MOVIE_PATH_KEY]}')
        
    if _TV_SHOW_PATH_KEY in os.environ:
        print()
        print(_MESSAGE_COLOR | f'Searching for: {os.environ[_TV_SHOW_PATH_KEY]}')
        try:
            with open(os.environ[_TV_SHOW_PATH_KEY], 'r') as tv_show_file:
                _tv_show_data = json.load(tv_show_file)
                print(_SUCCESS_COLOR | '[TV SHOW DATA SUCCESSFULLY LOADED]')
        except IOError:
            print(_ERROR_COLOR | f'TV show file not found: {os.environ[_MOVIE_PATH_KEY]}')
            pass
        except JSONDecodeError:
            print(_ERROR_COLOR | 'TV show file not in proper JSON format')

def execute():
    if len(sys.argv) != 3 or 'help' in map(str.lower, sys.argv):
        print()
        print(_ALERT_COLOR | '[Alexandria - Syntax]')
        print()
        print(_MESSAGE_COLOR | 'SYNTAX: python -m alexandria [port 0-65535, inclusive] [path/to/env/]')
        print(_MESSAGE_COLOR | 'EXAMPLE: python -m alexandria 8080 /home/user/alexandria/')
        print()
        print(_MESSAGE_COLOR | 'port - the port on which to start the server')
        print(_MESSAGE_COLOR | 'path/to/env - the path to the .env file with server settings')
    elif not sys.argv[1].isdigit() or int(sys.argv[1]) < 0 or int(sys.argv[1]) > 65535:
        print()
        print(_ALERT_COLOR | '[Alexandria requires a target port]')
        print()
        print(_MESSAGE_COLOR| 'Ensure that port is a valid integer between 0 and 65535, inclusive.')
    elif not os.path.isdir(sys.argv[2]) or not os.path.exists(sys.argv[2] + '.env'):
        print()
        print(_ALERT_COLOR | '[Alexandria requires a valid path]')
        print()
        print(_MESSAGE_COLOR | 'Ensure that path is a valid path and it contains the .env file')
    else:
        _parse_env(sys.argv[2] + '.env')
        port = sys.argv[1]
        print()
        print(_ALERT_COLOR | '[--Syntax correct, attempting startup--]')
        print()
        print(_SUCCESS_COLOR | f'Running on 127.0.0.1:{port}') 
        serve(app, host='127.0.0.1', port=int(port))

if __name__ == "__main__":
    execute()
    