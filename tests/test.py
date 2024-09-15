import unittest
from app.app import app, tasks_dict


class TestTodoAPI(unittest.TestCase):

    def test_get_tasks(self):
        """Tests that the GET /todo/api/v1/tasks endpoint returns all tasks."""
        with app.test_client() as client:
            response = client.get('/todo/api/v1/tasks')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'tasks': tasks_dict})

    def test_get_task(self):
        """Tests that the GET /todo/api/v1/tasks/<int:task_id> endpoint returns a single task."""
        task_id = 1
        with app.test_client() as client:
            response = client.get(f'/todo/api/v1/tasks/{task_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'task': tasks_dict[0]})

    def test_get_nonexistent_task(self):
        """Tests that the GET /todo/api/v1/tasks/<int:task_id> endpoint returns 404 for non-existent tasks."""
        task_id = 100
        with app.test_client() as client:
            response = client.get(f'/todo/api/v1/tasks/{task_id}')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()