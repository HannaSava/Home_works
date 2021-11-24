from flask import Flask

from db import execute_query
from formater import list_rec_html

app = Flask(__name__)


@app.route('/duration_of_tracks')
def get_duration_of_tracks():
    sql = 'select g.Name as "Genre", SUM(t.Milliseconds) / 1000 / 60 as "Duration" \n' \
          'from tracks as t join genres as g on t.GenreId = g.GenreId group by g.GenreId \n' \
          'order by "Duration" desc'

    records = execute_query(sql)

    return list_rec_html(records)


if __name__ == '__main__':
    app.run(debug=True, port=8005)
