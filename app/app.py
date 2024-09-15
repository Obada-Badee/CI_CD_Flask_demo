#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)


tasks_dict = {
    1:{
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },

    2:   {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
    
}
#Demo data for application
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    """Get requst that retruns all tasks"""
    return jsonify({'All Tasks':tasks_dict})


@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get requst that retruns one task by ID"""
    task = tasks_dict.get(task_id, None)
    if task == None:
        abort(404)
    return jsonify({'The Task': task})


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    """ Post request that adds new task"""
    if not request.json or 'title' not in request.json:
        abort(400)

    # Generate a unique ID using UUID
    task_id = sorted(tasks_dict.items())[-1][0] + 1

    task = {
        'id': task_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks_dict[task_id] = task
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """ A PUT method that updates a present task with its ID number"""
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """ DELETE Method that deletes a task already there """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    """ Function to handle errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
