import pytest
from jsonschema import validate
from schema import get
from helper.data import load_yaml_case_data, assert_body
from helper.log import Logger
from helper.api_client import ApiClient

logger = Logger(logger="TestDemo").get_log()

@pytest.mark.parametrize('data', load_yaml_case_data("cases/post.yaml"))
def test_post(data):
    # logger.info("Make a request")
    # print(f"======================================= \n {data['request']}")
    # print(data['request'])
    response = ApiClient().send_request(**data['request'])
    # print(response)
    # logger.info("Assert response body and status")
    assert validate(instance=response.json(), schema=get.schema) is None
    assert_body(data, response.json())
    assert response.status_code == 200
