import unittest
from app import app, tasks_dict


class ToDoAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_tasks(self):
        response = self.app.get('/todo/api/v1/tasks')
        self.assertEqual(response.status_code, 200)

    def test_get_task_by_id_fail(self):
        task_id = 100
        response = self.app.get(f'/todo/api/v1/tasks/{task_id}')
        self.assertEqual(response.status_code, 404)

    def test_create_task_success(self):
        data = {'title': 'Buy Bread'}
        response = self.app.post('/todo/api/v1/tasks', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['title'], data['title'])

    def test_create_task_fail_no_json(self):
        response = self.app.post('/todo/api/v1/tasks')
        self.assertEqual(response.status_code, 400)

    def test_create_task_fail_missing_title(self):
        data = {'description': 'Need a loaf!'}
        response = self.app.post('/todo/api/v1/tasks', json=data)
        self.assertEqual(response.status_code, 400)

    def test_update_task_fail_not_found(self):
        task_id = 100
        data = {'title': 'Updated Grocery List'}
        response = self.app.put(f'/todo/api/v1/tasks/{task_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_update_task_fail_no_json(self):
        task_id = 1
        response = self.app.put(f'/todo/api/v1/tasks/{task_id}')
        self.assertEqual(response.status_code, 400)

    def test_delete_task_success(self):
        task_id = 1
        response = self.app.delete(f'/todo/api/v1/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': True})
        # Check if task is actually deleted (avoid modifying original data)
        self.assertNotIn(task_id, tasks_dict.copy())

    def test_delete_task_fail_not_found(self):
        task_id = 100
        response = self.app.delete(f'/todo/api/v1/tasks/{task_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()