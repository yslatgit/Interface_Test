class Params:
    """根据传入参数的值，自动拼接请求参数"""
    def auto_params(params):
        for key in list(params.keys()):
            if not params.get(key):
                del params[key]
        return params



if __name__ == '__main__':
    pass