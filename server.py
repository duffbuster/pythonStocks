from flask import Flask, session, render_template, request, redirect, url_for 

import utils, MySQLdb, ystockquote
app = Flask(__name__)

app.secret_key = 'Zq4oA4Dqq3'

#TODO: variables: username, symbol, price, error
#TODO: get ystockquote working

# Homepage: search for stocks and get current price
@app.route('/', methods=['GET', 'POST'])
def mainIndex():
    if request.method == 'POST':
	ticker = request.form['search']
    	stockPrice = ystockquote.get_price(ticker)
    	return render_template('index.html', selectedMenu='Home', price=stockPrice, symbol=ticker, queryType='stock')
    if 'username' in session:
	return render_template('index.html', selectedMenu='Home', username=session['username'])
    return render_template('index.html', selectedMenu='Home')

#TODO: get table showing on stockReport page (for loop in stockReport.html)

# Stockreport only shows stuff it you're logged in
# If not logged in displays message
@app.route('/stockReport', methods=['GET', 'POST'])
def stockReport():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    # if user is logged in
    if 'username' in session:
        # update stocks then...
            # to update, get array of tickers and use a for loop to iterate through and update the price of each one
        # display stocks
	displayQuery = "SELECT s.symbol symbol, s.name name, s.price price, o.amount amount, (s.price * o.amount) total FROM users u JOIN owners o JOIN stocks s ON u.user_id = o.user_id AND o.stock_id = s.stock_id WHERE u.username = '%s'; " % (session['username'])
	cur.execute(displayQuery)
	print displayQuery
	rows = cur.fetchall()
	print rows
	if request.method == 'POST':
	    print "Adding a new stock to the database..."
	    symbol = request.form['symbol']
	    name = request.form['name']
	    numOwned = request.form['numOwned']
	    #make yql call for price
	    stockPrice = ystockquote.get_price(symbol)
	    
	    query = "SELECT * FROM stocks WHERE symbol = '%s';" % (symbol)
	    cur.execute(query)
	    print query
	    if not cur.fetchone():
		print "Hello World"
	    	queryA = "INSERT INTO stocks (symbol, name, price) VALUES('" + symbol + "', '" + name + "', '" + stockPrice + "');"
		cur.execute(queryA)
		db.commit()
		print queryA
	    
            idquery = "SELECT stock_id FROM stocks WHERE symbol = '%s';" % (symbol)
	    cur.execute(idquery)
	    print idquery
	    data = cur.fetchall()
	    stockid = ''
	    for row in data:
		stockid = row['stock_id']
	    print stockid
	    #queryB = "INSERT INTO owners VALUES((SELECT user_id FROM users WHERE username = '" + session['username'] + "'), " + stockid + ", " + numOwned + ");"
	    queryB = "INSERT INTO owners VALUES((SELECT user_id FROM users WHERE username = '%s'), %s, %s);" % (session['username'], stockid, numOwned)
	    print queryB
	    cur.execute(queryB)
	    db.commit()
	return render_template('stockReport.html', selectedMenu='stockReport', username = session['username'], rows=rows)
    else:
	# return to home
        return redirect(url_for('mainIndex'))
    
    return redirect(url_for('mainIndex'))                                          


@app.route('/login', methods=['GET', 'POST'])
def login():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        print "Logging in..."
        loginUser = request.form['username']
        pw = request.form['password']
        query = "SELECT * FROM users WHERE username = '%s' AND password = SHA2('%s', 0)" % (loginUser, pw)
        print query
	cur.execute(query)
        
        if cur.fetchone():
            session['username'] = loginUser
            pw = ''
            return redirect(url_for('mainIndex'))
        else:
            error = 'Username and password do not match!'
	    print error
	    return render_template('login.html', selectedMenu='Login', error=error)
    if 'username' in session:
	return render_template('login.html', selectedMenu='Login', username=session['username'])
    return render_template('login.html', selectedMenu='Login')

@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        print "Creating new user..."
        session['username'] = request.form['username']
        newPw = request.form['password']
        
        newQuery = "INSERT INTO users (username, password) VALUES('" + session['username'] + "', SHA2('" + newPw + "', 0))"
        query = "SELECT * FROM users WHERE username = '%s' AND password = SHA2('%s', 0)" % (session['username'], newPw)
        print newQuery
        cur.execute(newQuery)
        db.commit()
        cur.execute(query)
        if cur.fetchone():
            return redirect(url_for('mainIndex'))
    
    if 'username' in session:
        return render_template('newUser.html', selectedMenu='New User', username=session['username'])
    return render_template('newUser.html', selectedMenu='New User')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('zip', None)
    print 'You were logged out'
    return redirect(url_for('mainIndex'))

if __name__ == '__main__':
	app.debug==True
	app.run(host='0.0.0.0',port=3000)
