from flask import Flask

from db import execute_query
from formater import list_rec_html

from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route('/unique_name')
@use_kwargs(
    {
        'first_name': fields.Str(
            required=False,
            missing=None,
        )
    },
    location='query'
)
def get_unique_name(first_name):
    sql = 'select FirstName from customers group by FirstName'
    if first_name:
        sql = f'select FirstName from customers where FirstName="{first_name}"'

    records = execute_query(sql)

    return list_rec_html(records)


if __name__ == '__main__':
    app.run(debug=True, port=8030)
