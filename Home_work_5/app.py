from flask import Flask

from db import execute_query
from formater import list_rec2html_br

app = Flask(__name__)


@app.route('/tracks_count')
def get_tracks_count():
    sql = 'select count(*) as count from tracks'
    records = execute_query(sql)
    return list_rec2html_br(records)


if __name__ == '__main__':
    app.run(debug=True, port=8009)
