"""api tests"""
from DoList import create_app, db
from DoList.DoList.models import Item
import json

app = create_app('testing')


def test_dolist_get_200():
    """get test"""
    with app.test_client() as client:
        response = client.get('/api/dolist')
        print(response.status_code)
        assert response.status_code == 200


def test_dolist_post_201():
    """post test"""
    with app.test_client() as client:
        response = client.post('/api/dolist', json=dict(
            title='kolyTEST',
            text='sdgldsgld',
            slug='koly-titleTEST',
            is_completed=True
        ))
        assert response.status_code == 201


def test_dolist_post_500():
    """post test exists"""
    with app.test_client() as client:
        response = client.post('/api/dolist', json=dict(
            title='kolyTEST',
            text='sdgldsgld',
            slug='koly-titleTEST',
            is_completed=True
        ))
        assert response.status_code == 500


def test_dolist_put_500():
    """put test exists"""
    with app.test_client() as client:
        response = client.put('/api/dolist?item_title=kolyTEST', json=dict(
            title='kolyTEST',
            text='sdgldsgld',
            slug='koly-titleTEST',
            is_completed=True
        ))
        print(response.status_code)
        assert response.status_code == 500


def test_dolist_put_202():
    """put test"""
    with app.test_client() as client:
        response = client.put('/api/dolist?item_title=kolyTEST', json=dict(
            title='title',
            text='changed',
            slug='koly-titleTEST',
            is_completed=True
        ))
        print(response.status_code)
        assert response.status_code == 202


def test_dolist_delete_204():
    """delete test"""
    with app.test_client() as client:
        response = client.delete('/api/dolist?item_title=title')
        print(response.status_code)
        assert response.status_code == 204


def test_dolist_delete_500():
    """deleting not existing element"""
    with app.test_client() as client:
        response = client.delete('/api/dolist?item_title=title')
        print(response.status_code)
        assert response.status_code == 500
