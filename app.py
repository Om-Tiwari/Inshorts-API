from flask import Flask, request, jsonify
from scraper import getNews
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app)


@app.route('/news', methods=['GET'])
def news():
    return jsonify(getNews(request.args.get('category')))


@app.route('/')
def home():
    return ("""<h1>News API</h1>
           <p>Use /news?category=category_name to get news</p>
           <p>Categories: all, national, education,business, sports, world, politics, technology, startup, entertainment, miscellaneous, hatke, science, automobile</p>
           <p>Example: <a href='/news?category=education'>/news?category=education</a></p>
           <p>Source: https://inshorts.com/</p>
           <p>Developed by: <a href="https://www.linkedin.com/in/mrsus/">Om Tiwari</a></p>""")


http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
