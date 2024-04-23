import os
import yaml
import json
from helper.log import Logger

logger = Logger(logger="Prepare Data").get_log()


def load_yaml_case_data(filename):
    # logger.info("获取测试用例yaml文件地址")
    path = os.getcwd()
    yaml_file = os.path.join(path, filename)
    # logger.info("获取测试用例数据")
    with open(yaml_file, "r") as file:
        return yaml.safe_load(file)


def assert_body(yaml_data, response_body):
    for assert_type in yaml_data['assert']:
        for key, value in assert_type.items():
            for assert_key, assert_value in value.items():
                if key == "eq":
                    print(type(assert_value))
                    print(type(response_body[assert_key]))
                    print(f"{assert_key}: {assert_value}")
                    assert assert_value == response_body[assert_key]
                elif key == "contains":
                    assert response_body[assert_key] in assert_value
                else:
                    print("No Other Assert Type")
