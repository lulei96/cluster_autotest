import os
import pytest
from common.images.images import Images
from common.video.video import *
from common.utils import *
from common.utils import case_fail
from common.utils import read_yaml
from common.can.canoe import CANoe
from common.can.dbc import DBCtoXML

#zcan
###########################################
# dbc_path = './common/can/canoe_project/A8E_Proj_IHU_PFET_CMX+V1.25_20230421.dbc'
# data = [0,0,0,0,0,0,0,0]
# message_id = 0x260
# signal_name1 = 'BCS_VehSpd'
# signal_name2 = 'BCS_VehSpdVD'
# signal_value1 = 92
# signal_value2 = 1
# message_fram1=physical_to_frame(dbc_path,data,message_id,signal_name1,signal_value1)
# message_fram2=physical_to_frame(dbc_path,message_fram1,message_id,signal_name2,signal_value2)
# can_transmit(message_fram2,10)
# #Close CAN
# ret=zcanlib.ResetCAN(chn_handle)
# if ret==1:
#     print("ResetCAN success! ")
# #Close Device
# ret=zcanlib.CloseDevice(handle)
# if ret==1:
#     print("CloseDevice success! ")
#CANoe
#############################################
#config_data=read_yaml.read_yaml('./config/config.yaml')
#app = CANoe() #定义CANoe为app
#app.open_cfg(config_data["cfg_path"]) #导入某个CANoe config
#app.start_Measurement()
#app.set_SysVar("GW_BCS_2_B_260","BCS_VehSpd",92) #发送报文
#app.set_SysVar("GW_BCS_2_B_260","BCS_VehSpdVD",1) #发送报文
#app.get_SigVal(1, "ACU_HVAC_1_B", "ACU_HVACFR_RrTempSetting", bus_type="CAN")#接收报文
#app.import_all_SysVar()#导入xml到系统变量
#dbc to xml
#############################################
#test_data=read_yaml.read_yaml('./config/config.yaml')
#test=DBCtoXML()
#path=test.DictoXML(r"C:/Users/Administrator/Desktop/A02/CANdb/A02Project_CMX_IDC_V6.3.3(G38.0)20230308.dbc",r"C:/Users/Administrator/Desktop/A02/SystemVariable") #生成xml文件返回路径

if __name__ == '__main__':
    pytest.main([
                "-q",
                "-s", 
                "-ra", 
                r".\test\testcase\test_a8e_panel.py",
                '--alluredir',
                r'.\test\output_report',
                '--clean-alluredir'
                ])
    #方式一：直接打开默认浏览器展示报告
    #allure serve ./result/
    #方式二：从结果生成报告
    #生成报告
    #allure generate ./result/ -o ./report/ --clean (覆盖路径加--clean)
    #打开报告
    #allure open -h 127.0.0.1 -p 8883 ./report/
    os.system(r'allure serve .\test\output_report')