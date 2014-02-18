Stockify
============

A quick and dirty python api for storing stocks.

Created by Colin Mackey, Kevin Murphy, Chad Schmidt, and Peter Moerman
for Computer Science 350 at the University of Mary Washington

Project Description
============

This is a simple web page with a database back end for storing stock info
    * Platforms used: 
        * Python
        * HTML
        * MySQL
        
The website front-end asks for the user to input the symbols of stocks he or she wants to track.
The stocks are stored in the database with their symbol, the name of the company, the current price, and a modified time stamp.
The user's stocks are updated every time he or she presses the "Update" button or every time the site is launched (suj to change).
Live update of the stocks is handled through YQL (Yahoo Query Language) queries to Yahoo finance, which provides a live price.
        
Installation
============

git clone https://github.com/duffbuster/pythonStocks.git