from flask import Flask

from webargs import fields
from webargs.flaskparser import use_kwargs

from db import execute_query
from formater import list_rec_html

app = Flask(__name__)


@app.route('/sales_tracks')
@use_kwargs(
    {
        'count': fields.Int(
            required=False,
            missing=None,
        )
    },
    location='query'
)
def best_selling_tracks(count):
    sql = 'select t.Name, SUM(ii.Quantity) as "sales", \n' \
          'SUM(ii.UnitPrice * ii.Quantity) as "sales_amount" from tracks as t \n' \
          'join invoice_items as ii on t.TrackId = ii.TrackId group BY ii.TrackId \n' \
          'order by "sales_amount" DESC'
    if count:
        sql = f'select t.Name from tracks as t where row_number() ="{count}"'

    records = execute_query(sql)

    return list_rec_html(records)


if __name__ == '__main__':
    app.run(debug=True)
