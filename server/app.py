from flask import Flask, request, jsonify

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_config import Base, User

# Connect to Database and create database session
engine = create_engine('sqlite:///users-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/users', methods=['POST', 'PUT'])
def saveUser():
    post_data = request.get_json()

    if request.method == 'POST':
        newUser = User(name=post_data.get('name'), sectors=post_data.get('sectors'), terms=post_data.get('terms'))

        session.add(newUser)
        session.commit()

        resp = jsonify(message='user created')   
        return resp
    if request.method == 'PUT':
        id=post_data.get('id')
        sectors=post_data.get('sectors')
        terms=post_data.get('terms')

        editedUser = session.query(User).filter_by(id = id).one()
        editedUser.sectors = sectors
        editedUser.terms = terms
        
        session.add(editedUser)
        session.commit()

        resp = jsonify(message='resource updated')   
        return resp

@app.route('/users', methods=['GET'])
def getUser():
    latestSaved = session.query(User).order_by(User.id.desc()).first()
    
    resp = jsonify(success=True, id=latestSaved.id, name=latestSaved.name, sectors=latestSaved.sectors, terms=latestSaved.terms)   
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)