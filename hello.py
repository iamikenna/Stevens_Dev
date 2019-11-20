""" 
Testing the flask installation
- Setting up the web server
"""
"""
Author: Ibezim Ikenna
User functions about stevens repository
"""
from flask import Flask, render_template # calling flask libray
import sqlite3

app = Flask(__name__) 
@app.route('/Hello')
def hello():
    """creating the connection and value to be rendered by the browser"""
    return "Hello world! This is flask!"
    
@app.route('/Goodbye')
def see_ya():
    """creating the connection and value to be rendered by the browser"""
    return "See you later!"

@app.route('/instructors')
def instructor():
    db_path = "/Users/ikenna/hw11.db"
    try:
        db = sqlite3.connect(db_path) # making connection to the database 
    except sqlite3.OperationalError: # checking for failed connections to the db
        print(f"Cant open database at path {db.path}")
    else:
        query = """select i.CWID as Cwid, i.Name as Name, i.Dept as Dept, g.Course as Course, count(g.Course) as Course_count 
                from grades g  
                join instructors i on i.CWID = g.InstructorCWID 
                group by Cwid, Name, Dept, Course"""
        # converting the query into a dictionary to enable us use it inside the template
        data = [{'Cwid':Cwid, 'Name':Name, 'Dept':Dept, 'Course':Course, 'Course_count':Course_count} for Cwid, Name, Dept, Course, Course_count in db.execute(query)]
    return render_template('program1.html',
                            title="Instructor Table",
                            my_header="My Stevens Repository",
                            my_header2="Getting the Instructor table from the database ",
                            my_param="My main parameter",
                            instructors=data)

app.run(debug=True) #automatically restarts flask if the file changes 
