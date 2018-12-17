class Params:
    def auto_params(params):
        for key in list(params.keys()):
            # print(key)
            if not params.get(key):
                del params[key]
        return params


if __name__ == '__main__':
    # p = Params('case_name,method,cookie,account')
    # print(p.params())
    pass