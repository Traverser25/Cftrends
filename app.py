from flask import Flask, jsonify,render_template
from flask_cors import CORS
import sqlite3
dbpath="CFproblems.db"
app = Flask(__name__)
CORS(app)
def updateVisit():
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("SELECT visitcount FROM visits")
    cnt = cursor.fetchone()[0]
    cnt += 1
    cursor.execute("UPDATE visits SET visitcount = ?", (cnt,))
    conn.commit() 
    conn.close()

def getVisitCount():
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("SELECT visitcount FROM visits")
    cnt = cursor.fetchone()[0]
    conn.close()
    return cnt


@app.route('/')
def index():
    updateVisit()
    return render_template("spawnhome.html")

@app.route('/getVisit', methods=['GET'])
def getVisit():
    cnt=getVisitCount()
    return jsonify({"count":cnt})

@app.route('/problems/<int:rating>', methods=['GET'])
def get_problems_by_rating(rating):
    try:
        rating=str(rating)
        conn = sqlite3.connect("CFproblems.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM problem_table WHERE rating=?"
        cursor.execute(query, (rating,))
        problems = cursor.fetchall()
        conn.close()

        problem_list = []
        for prob in problems:
            problem_dict = {
                'probName': prob[0],
                'link': prob[1],
                'rating': prob[2]
            }
            problem_list.append(problem_dict)

        return jsonify(problem_list)
    
    except sqlite3.Error as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
