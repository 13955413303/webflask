# encoding=utf8
import platform
sys = platform.system()
print(sys)
if sys == 'Windows':
    pass
if sys == 'Linux':
    import sys, os
    os.chdir(r'/home/admin/webflask/api')
    default_path = os.getcwd()
    sys.path.append(default_path)
    sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))



from flask import Flask, request, render_template
import json

from sql_util.link_mysql import insert_info, select_info

app = Flask(__name__)


# 只接受get方法访问
@app.route("/test_1.0", methods=["GET"])
def zhuce():
    # 默认返回内容
    # return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': True}
    # 判断入参是否为空
    if not len(request.args):
        return_dict = {'return_code': '5004', 'return_info': '请求参数为空', 'result': False}
        return json.dumps(return_dict, ensure_ascii=False), 5004
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')
    print(name,age)
    try:
        insert_info(name, int(age))
    except BaseException:
        return_dict = {'return_code': '444', 'return_info': '数据写入失败', 'result': False}
        print('write db failed!')
        return json.dumps(return_dict, ensure_ascii=False), 444
    # 对参数进行操作
    return_dict = {'return_code': '200', 'return_info': tt(name, age), 'result': True}
    return json.dumps(return_dict, ensure_ascii=False), 200


@app.route('/test_2.0', methods=["GET", "POST"])
def denglu():
    if request.method == "GET":
        return_dict = {'return_code': '5004', 'return_info': '请求参数为空', 'result': False}
        return json.dumps(return_dict, ensure_ascii=False), 5004
    elif request.method == 'POST':
        name = request.form['name']
        print(name)
        try:
            result = select_info(name)
        except BaseException:
            return_dict = {'return_code': '444', 'return_info': '登录出错', 'result': False}
            return json.dumps(return_dict, ensure_ascii=False), 444
        # 对参数进行操作
        if len(result) == 0:
            return_dict = {'return_code': '445', 'return_info': '信息有误，登录失败', 'result': False}
        else:
            name = result[0]['name']
            age = str(result[0]['age'])
            return_dict = {'return_code': '200', 'return_info': tt(name, age), 'result': True}
        return json.dumps(return_dict, ensure_ascii=False), 200


# 功能函数
def tt(name, age):
    result_str = "%s今年%s岁" % (name, age)
    return result_str


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
