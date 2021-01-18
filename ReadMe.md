python 3.6

安装依赖环境
pip install -r request.txt

使用命令生成JSON格式的测试数据并保存在result目录下，
即behave -f allure_behave.formatter:AllureFormatter -o result ./features

安装allure 
使用命令将result目录下的JSON格式的测试数据转换成测试报告并且保存在report目录下：
allure generate ./result/ -o ./report/ --clean


框架结构树：
- features
    - steps  # 存放执行代码，用content上下文传参
    - utils  # 工具类
    - feature # feature 文件
    - environment.py  # 配置环境变量
- test 测试自己的代码
- report allure 报告
- result 报告json 文件
    