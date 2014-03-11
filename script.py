from flask import Flask, render_template

<<<<<<< HEAD
mport utils, stockdb
app = Flask(__name__)

@app.route('/')
=======
import utils, stockTickers
app = Flask(__name__)

@app.route('/stocks')
>>>>>>> master
def mainIndex():
    return render_template('stockhomepage.html', selectedMenu='Home')

@app.route('/stockreport', methods=['POST'])
def report2():
  date = '%s-%02i-%02i' % (request.form['year'], int(request.form['month']),
                           int(request.form['day']))
  
  db = utils.db_connect()
<<<<<<< HEAD
  cur = db.cursor(cursorclass=stockdb.cursors.DictCursor)
  query = "INSERT INTO stockdb (firstname, lastname, stockname,stockinfo)"
=======
  cur = db.cursor(cursorclass=stockTickers.cursors.DictCursor)
  query = "INSERT INTO users (firstname, lastname, username,password)"
>>>>>>> master
  cur.execute(query)
  db.commit()
  
  return redirect(url_for('stocklist'))                                          


<<<<<<< HEAD
@app.route('/stocklist')
def stocklist():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    query = 'SELECT * from stockdb'
=======
@app.route('/stockslist')
def stocklist():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    query = 'SELECT * from users'
>>>>>>> master
    cur.execute(query)
    rows = cur.fetchall()
    return render_template('stocklist.html', abductions=rows, selectedMenu='StockList')





if __name__ == '__main__':
	app.debug==True
	app.run(host='0.0.0.0',port=3000)









