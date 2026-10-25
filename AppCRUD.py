from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('students_new.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    
    # Handle Form Submission (Add or Update)
    if request.method == 'POST':
        action = request.form.get('action')
        db_id = request.form.get('db_id')  # Hidden field for primary key 'Id'  db_id = request.form['db_id']
        student_id = request.form['Student_Id']
        student_name = request.form['Student_Name']
        major = request.form['Major']
        score = request.form['Score']
        grade = request.form['Grade']
        
        if action == 'update' and db_id:
            # UPDATE Query
            conn.execute('''
                UPDATE student_table 
                SET Student_Id = ?, Student_Name = ?, Major = ?, Score = ?, Grade = ? 
                WHERE Id = ?
            ''', (student_id, student_name, major, score, grade, db_id))
        else:
            # INSERT Query
            conn.execute('''
                INSERT INTO student_table (Student_Id, Student_Name, Major, Score, Grade) 
                VALUES (?, ?, ?, ?, ?)
            ''', (student_id, student_name, major, score, grade))
            
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    # Check if user clicked 'Edit' on a row (Passes edit_id via GET query parameter)
    edit_id = request.args.get('edit_id')
    student_to_edit = None
    if edit_id:
        student_to_edit = conn.execute('SELECT * FROM student_table WHERE Id = ?', (edit_id,)).fetchone()

    # Fetch all students for the table view
    students = conn.execute('SELECT * FROM student_table').fetchall()
    conn.close()
    
    return render_template('index_SQLiteCRUD.html', student_list=students, student_to_edit=student_to_edit)

# Route to handle DELETE action
@app.route('/delete/<int:db_id>', methods=['POST'])
def delete_student(db_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM student_table WHERE Id = ?', (db_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


