from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from model import engine, Base, User, Post

app = Flask(__name__)

# Create the database tables (SERIOUSLY. REMEMBER TO DELETE)
Base.metadata.create_all(bind=engine)

# Create a SQLAlchemy session
db = Session(bind=engine)


# Route to create a new user
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()

    return jsonify({'message': 'User created successfully'}), 201


# Route to get all users
@app.route('/get_users', methods=['GET'])
def get_users():
    users = db.query(User).all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_list)


# Route to create a new post for a user
@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    body = data.get('body')

    user = db.query(User).filter_by(id=user_id).first()
    if user:
        new_post = Post(title=title, body=body, author=user)
        db.add(new_post)
        db.commit()
        return jsonify({'message': 'Post created successfully'}), 201
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
