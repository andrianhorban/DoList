"""api tests"""
from DoList import create_app, db
from DoList.DoList.models import Item
import json

app = create_app('testing')


def test_dolist_get_200():
    with app.test_client() as client:
        response = client.get('/api/dolist')
        print(response.status_code)
        assert response.status_code == 200


def test_dolist_post_201():
    with app.test_client() as client:
        response = client.post('/api/dolist', json=dict(
            title='koly1231',
            text='sdgldsgld',
            slug='koly-title1231',
            is_completed=True
        ))
        assert response.status_code == 201


def test_dolist_delete_204():
    with app.test_client() as client:
        response = client.delete('/api/dolist?item_title=koly1231', json=dict(
            title='koly1231',
            text='sdgldsgld',
            slug='koly-title1231',
            is_completed=True
        ))
        print(response.status_code)
        assert response.status_code == 204


def test_dolist_put_202():
    with app.test_client() as client:
        response = client.put('/api/dolist?item_title=title1', json=dict(
            title='title1',
            text='changed',
            slug='koly-title12313',
            is_completed=True
        ))
        print(response.status_code)
        assert response.status_code == 202
