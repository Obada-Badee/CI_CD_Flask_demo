#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)
app.url_map.strict_slashes = False

tasks_dict = {
    1:{
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },

    2:   {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
    
}


@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    """Get requst that retruns all tasks"""
    return jsonify(tasks_dict)


# @app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     """Get requst that retruns one task by ID"""
#     task = tasks_dict.get(task_id, None)
#     if task == None:
#         abort(404)
#     return jsonify(task)


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    """ Post request that adds new task"""
    json = request.get_json(silent=True)
    if not json or 'title' not in request.json:
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
    return jsonify(task), 201


@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """ A PUT method that updates a present task with its ID number"""
    task = tasks_dict.get(task_id, None)

    if task is None:
        abort(400)
    json = request.get_json(silent=True)
    if not json:
        abort(400)

    # Validate data types (adjust based on your specific requirements)
    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400)
    if 'description' in request.json and not isinstance(request.json['description'], str):
        abort(400)
    if 'done' in request.json and not isinstance(request.json['done'], bool):
        abort(400)

    # Update task properties directly
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])

    tasks_dict[task_id] = task
    return jsonify({'Updated Task': task})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """ DELETE Method that deletes a task already there """
    if task_id not in tasks_dict:
        abort(404)

    del tasks_dict[task_id]
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    """ Function to handle errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
