from flask import Flask, session, render_template, request, redirect, url_for 

import utils, stockTickers, ystockquote
app = Flask(__name__)

app.secret_key = 'Zq4oA4Dqq3'

# Homepage: search for stocks and get current price
@app.route('/', methods=['GET', 'POST'])
def mainIndex():
    ticker = request.form['symbol']
    stockPrice = ystockquote.get_price(ticker)
    
    return render_template('index.html', selectedMenu='Home', stockPrice=stockPrice)

# TODO: addStock route

# Stockreport only shows stuff it you're logged in
# If not logged in displays message
@app.route('/stockReport', methods=['GET'])
def stockReport():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    # if user is logged in
    if 'username' in session:
        # update stocks then...
            # to update, get array of tickers and use a for loop to iterate through and update the price of each one
        # display stocks
	print "hello"
    else:
	# return to home
        return redirect(url_for('mainIndex'))
    
    return redirect(url_for('stocklist'))                                          


@app.route('/login', methods=['GET', 'POST'])
def login():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        print "Logging in..."
        loginUser = request.form['username']
        pw = request.form['password']
        query = "SELECT * FROM users WHERE username = '%s' AND password = SHA2('%s', 0)" % (loginUser, pw)
        cur.execute(query)
        
        if cur.fetchone():
            session['username'] = loginUser
            pw = ''
            return redirect(url_for('mainIndex'))
        else:
            error = 'Username and password do not match!'
        
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
        cur.execute(query)
        if cur.fetchone():
            return redirect(url_for('mainIndex'))
    
    if 'username' in session:
        return render_template('newUser.html', selectedMenu='New User', username=session['username'])
    return render_templage('newUser.html', selectedMenu='New User')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('zip', None)
    print 'You were logged out'
    return redirect(url_for('mainIndex'))

if __name__ == '__main__':
	app.debug==True
	app.run(host='0.0.0.0',port=3000)
