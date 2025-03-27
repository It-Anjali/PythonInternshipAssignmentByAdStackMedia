from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define App model
class AppModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Create database and tables
with app.app_context():
    db.create_all()

# Home route (for testing)
@app.route('/')
def home():
    return "✅ Flask API is running!"

# POST /add-app
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    new_app = AppModel(
        app_name=data['app_name'],
        version=data['version'],
        description=data['description']
    )
    db.session.add(new_app)
    db.session.commit()
    return jsonify({'message': 'App added successfully', 'id': new_app.id}), 201

# GET /get-app/<id>
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_data = AppModel.query.get(id)
    if app_data:
        return jsonify({
            'id': app_data.id,
            'app_name': app_data.app_name,
            'version': app_data.version,
            'description': app_data.description
        })
    return jsonify({'error': 'App not found'}), 404

# DELETE /delete-app/<id>
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_data = AppModel.query.get(id)
    if app_data:
        db.session.delete(app_data)
        db.session.commit()
        return jsonify({'message': 'App deleted successfully'})
    return jsonify({'error': 'App not found'}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
