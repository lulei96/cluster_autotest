from ..common import adb,qnx,images
from ..utils import read_yaml
import pytest
import allure

class TestUint_Panel():
    def setup_class(self):
        print("前置条件")

    def teardown_class(self):
        print("后置条件")
    @pytest.mark.parametrize("test_data", [read_yaml.read_yaml('./cluster_autotest/config/config.yaml')])
    def test_01_spd(self,test_data):
        test_qnx = qnx.qnx(test_data["devices"],test_data["qnx_ip"],test_data["qnx_user"],test_data["qnx_passwd"])
        test_qnx.qnx_screenshot(test_data["qnx_screenshot_path"])
        test = adb.adb.adb_pull_image(test_data["devices"],
                                        test_data["adb_pull_source"],
                                        test_data["adb_pull_dest"])
        test_image=images.Images()
        test_result = test_image.compare_by_matrix_in_same_area(
                                                                test_data["input_images_path_spd"],
                                                                test,
                                                                test_data["image_position_spd"])
        allure.attach.file(test_data["input_images_path_spd"], name="预期结果", attachment_type=allure.attachment_type.BMP)
        allure.attach.file(test, name="实际结果", attachment_type=allure.attachment_type.BMP)
        assert test_result == None

class TestUint_Warning():

    def setup_class(self):
        print("前置条件")

    def teardown_class(self):
        print("后置条件")
    @pytest.mark.parametrize("test_data", [read_yaml.read_yaml('./cluster_autotest/config/config.yaml')])
    def test_02_eps(self,test_data):
        test_qnx = qnx.qnx(test_data["devices"],test_data["qnx_ip"],test_data["qnx_user"],test_data["qnx_passwd"])
        test_qnx.qnx_screenshot(test_data["qnx_screenshot_path"])
        test = adb.adb.adb_pull_image(test_data["devices"],
                                    test_data["adb_pull_source"],
                                    test_data["adb_pull_dest"])
        test_image=images.Images()
        test_result = test_image.compare_by_matrix_in_same_area(test_data["input_images_path_eps"],
                                                                test,
                                                                test_data["image_position_eps"])
        allure.attach.file(test_data["input_images_path_eps"], name="预期结果", attachment_type=allure.attachment_type.BMP)
        allure.attach.file(test, name="实际结果", attachment_type=allure.attachment_type.BMP)
        assert test_result == None