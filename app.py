from flask import Flask, render_template, request, redirect,Markup
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components, file_html
from bokeh.resources import CDN

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/stock',methods=["post","get"])
def closingprice():
   stockcode = request.args.get("stock")
   df = pd.read_csv('data.csv')
   df = df[df['ticker']==stockcode]
   df.sort_values(by=['date'])

   x = pd.to_datetime(df['date']).dt.day
   y = df['close']

   p = figure(title="closing price", x_axis_label='date',y_axis_label='price')
   p.line(x, y, legend="price", line_width=2)

   script, div = components(p)
   return Markup(file_html(p ,CDN,'my plot'))

if __name__ == '__main__':
  app.run(port=33507)
