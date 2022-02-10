import pytest
import requests
from Validator import Validator
from data_to_test import poly_data_different_val_types
from data_to_test import poly_data_wrong_keys
from data_to_test import poly_data_wrong_schema
from data_to_test import poly_data_extra_keys
from datetime import datetime
from datetime import timedelta

user_details = {"username": "test", "password": "1234"}
url = "http://localhost:8000/api/poly"
request = requests.post("http://localhost:8000/api/auth", json=user_details)
assert request.status_code == 200
auth_str = request.json()["access_token"]
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {auth_str}"}

GET_MAX_TIME = timedelta(seconds=20)
POST_MAX_TIME = timedelta(seconds=10)
DELETE_MAX_TIME = timedelta(seconds=10)


def get_all_poly_data():
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    return response.json()


def get_all_poly_object_id():
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    list_poly_data = response.json()
    object_id_list = []
    for poly_data in list_poly_data:
        object_id_list.append(poly_data['object_id'])
    return object_id_list


def get_poly_data(object_id):
    response = requests.get(f'{url}/{object_id}', headers=headers)
    assert response.status_code == 200
    return response.json()


def delete_poly_data(object_id):
    response = requests.delete(f'{url}/{object_id}', headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize('json_data', poly_data_different_val_types)
def test_add_different_types_val(json_data):
    # Add three items to db with different types.
    # Check if data saved in the correct schema and value.
    # Check if val type equal to valType.
    response = requests.post(url, headers=headers, json=json_data)
    assert response.status_code == 200
    object_id = response.json()['id']
    poly_data = get_poly_data(object_id)
    validator = Validator(**poly_data)
    assert validator.validate_types() is True
    assert json_data['data'] == poly_data['data'] and object_id == poly_data['object_id']
def test_post_performance():
    #Check the time take to do a post request
    start = datetime.now()
    json_data = {'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
    poly_data = requests.post(url, headers=headers, json=json_data)
    assert datetime.now() - start < GET_MAX_TIME
    assert poly_data.status_code == 200


def test_get_all_poly_performance():
    # Check the time take to do a get request
    start = datetime.now()
    response = requests.get(url, headers=headers)
    assert datetime.now() - start < GET_MAX_TIME
    assert response.status_code == 200


def test_get_one_performance():
    # Check the time take to do a get request
    object_id_list = get_all_poly_object_id()
    if object_id_list:
        start = datetime.now()
        response = requests.get(f'{url}/{object_id_list[0]}', headers=headers)
        assert datetime.now() - start < GET_MAX_TIME
        assert response.status_code == 200


def test_delete_performance():
    # Check the time take to do a delete request
    object_id_list = get_all_poly_object_id()
    if object_id_list:
        start = datetime.now()
        response = requests.delete(f'{url}/{object_id_list[0]}', headers=headers)
        assert datetime.now() - start < GET_MAX_TIME
        assert response.status_code == 200


def test_add_one_poly_with_valid_data():
    # Add data to db.
    json_data = {'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
    poly_data = requests.post(url, headers=headers, json=json_data)
    assert poly_data.status_code == 200
    id = poly_data.json()['id']
    poly_data = get_poly_data(id)
    assert json_data['data'] == poly_data['data'] and id == poly_data['object_id']


@pytest.mark.parametrize('poly_data', poly_data_wrong_keys)
def test_add_data_with_wrong_keys(poly_data):
    # Change the keys of the poly data
    # Send poly data with the invalid keys
    # Expecting to fail
    response = requests.post(url, headers=headers, json=poly_data)
    assert response.status_code == 400


@pytest.mark.parametrize('poly_data', poly_data_wrong_schema)
def test_add_wrong_schema(poly_data):
    response = requests.post(url, headers=headers, json=poly_data)
    assert response.status_code == 400


@pytest.mark.parametrize('poly_data', poly_data_extra_keys)
def test_add_extra_key(poly_data):
    # Add more keys to poly data
    # send poly data
    # Expecting to fail.
    response = requests.post(url, headers=headers, json=poly_data)
    assert response.status_code == 400





def test_get_all_poly_data_and_check_values_types():
    # Validating that all types are correct.
    # object_id is int
    # type(val)==valType
    list_poly_data = get_all_poly_data()
    for poly_data in list_poly_data:
        validator = Validator(**poly_data)
        assert validator.validate_types() is True


def test_delete_and_get_poly_data():
    # Get All poly object id
    # Delete poly data  by id
    # Try to get the poly data by id  after deleted.-Expecting Fail
    object_id_list = get_all_poly_object_id()
    if object_id_list:
        object_id = object_id_list[0]
        delete_poly_data(object_id)
        get_poly_data_after_delete = requests.get(f'{url}/{object_id}', headers=headers)
        assert get_poly_data_after_delete.status_code == 404
        assert get_poly_data_after_delete.json()['message'] == f'Resource with id {object_id} was not found'


def test_delete_all_poly_data():
    # Get all poly data list.
    # run around the list and delete .
    # after finished delete all verify the list is empty.
    object_id_list = get_all_poly_object_id()
    for object_id in object_id_list:
        delete_poly_data(object_id)
        get_poly_data_after_delete = requests.get(f'{url}/{object_id}', headers=headers)
        assert get_poly_data_after_delete.status_code == 404
        assert get_poly_data_after_delete.json()['message'] == f'Resource with id {object_id} was not found'

    list_poly_data_after_deleted_all = get_all_poly_data()
    assert list_poly_data_after_deleted_all == []


if __name__ == '__main__':
    pytest.main()
