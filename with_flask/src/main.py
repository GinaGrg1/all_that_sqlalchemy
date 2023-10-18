from flask import Flask

from .entities.entity import session, Exams

app = Flask(__name__)

@app.route('/exams')
def get_exams():
    exams_obj = session.query(Exams).all()
    tmp_dict = dict()

    for exam in exams_obj:
        tmp_dict['id'] = exam.id
        tmp_dict['title'] = exam.title
        tmp_dict['description'] = exam.description

    return tmp_dict
  
