import pytest
from jsonschema import validate
from schema import get
from helper.data import load_yaml_case_data, assert_body
from helper.log import Logger
from helper.api_client import ApiClient

logger = Logger(logger="TestDemo").get_log()

@pytest.mark.parametrize('data', load_yaml_case_data("cases/get.yaml"))
def test_get(data):
    response = ApiClient().send_request(**data['request'])
    assert validate(instance=response.json(), schema=get.schema) is None
    assert_body(data, response.json())
    assert response.status_code == 200

# def test_post():
#     response = requests.post(f'{api_host}/post', data={'key': 'value'})
#     rj = response.json()
#     assert response.status_code == 200
#     assert rj['form'] == {'key': 'value'}
#
# def test_put():
#     response = requests.put(f'{api_host}/put', data={'key': 'value2'})
#     rj = response.json()
#     assert response.status_code == 200
#     assert rj['form'] == {'key': 'value2'}
#
# def test_delete():
#     response = requests.delete(f'{api_host}/delete')
#     assert response.status_code == 200
