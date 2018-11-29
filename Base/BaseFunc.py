import json
class Func:

    def __init__(self,data):
        self.data = data

    def str_to_json(self):
        if len(self.data) == 0:
            return {}
        else:
            j = json.loads(self.data)
            return j

    def str_to_int(self):
        if len(str(self.data)) == 0:
            return None
        else:
            i = int(self.data)
            return i

if __name__ == '__main__':
    print(Func('{"begin":"10000","end":"20000"}').str_to_json())