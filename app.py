from flask import Flask, render_template, request, redirect
import pandas as pd
from bokeh.plotting import figure, output_file, show
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/stock',methods=['post','get'])
def closingprice():
   stockcode = request.args.get('id')
   df = pd.read_csv('data.csv')
   df = df[df['ticker']==stockcode]
   df.sort_values(by=['date'])

   x = pd.to_datetime(df['date']).dt.day
   y = df['close']

   p = figure(title="closing price", x_axis_label='date',y_axis_label='price')
   p.line(x, y, legend="price", line_width=2)  
   return show(p)

if __name__ == '__main__':
  app.run(port=33507)
