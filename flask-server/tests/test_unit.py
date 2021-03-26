"""api tests"""
from DoList import create_app, db

app = create_app('testing')


def test_dolist_get_200():
    with app.test_client() as client:
        response = client.get('/api/dolist')
        print(response.status_code)
        assert response.status_code, 200


def test_dolist_post_302():
    with app.test_client() as client:
        data = {
            'id': 2,
            'title': 'test title2',
            'text': 'test text2',
            'slug': 'test-title2',
            'is_completed': True
        }
        response = client.post('/dolist/add', data=data)
        assert response.status_code, 302


