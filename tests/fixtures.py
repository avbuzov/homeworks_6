import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = 'test'
    password = '123'
    django_user_model.objects.create(username=username, password=password)
    response = client.post('/user/token/', data={'username': username, 'password': password})
    return response.data.get('access')


@pytest.fixture
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    username = 'test'
    password = '123'
    user = django_user_model.objects.create(username=username, password=password)
    response = client.post('/user/token/', data={'username': username, 'password': password})
    return user, response.data.get('access')
