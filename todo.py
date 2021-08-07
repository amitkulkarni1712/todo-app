# Commands to run - 
#     1. python -m venv venv
#     2. /venv/Scripts/activate
#     3. pip install -r /requirements.txt
#     4. python todo.py
#     5. hit on browser http://127.0.0.1:5000/health
import datetime
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'task_name': 'Buy groceries',
        'description': 'Chitale_Milk, Amul_Cheese, Pizza_base, apple_Fruit',
        'done': False,
        'created_date': "",
        'updated_date': ""
    },
    {
        'id': 2,
        'task_name': 'Learn golang',
        'description': 'Need to find a good golang tutorial on the web',
        'done': False,
        'created_date': "",
        'updated_date': "" 
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Up'})


@app.route('/task', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/task/<int:task_id>', methods=['PUT'])

def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'task_name' in request.json and type(request.json['task_name']) is not str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['task_name'] = request.json.get('task_name', task[0]['task_name'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    task[0]["updated_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'task': task[0]}), 201

@app.route('/task', methods=['POST'])
def create_task():
    if not request.json or not 'task_name' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'task_name': request.json['task_name'],
        'description': request.json.get('description', ""),
        'done': False,
        'created_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


def create_app():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    create_app()


