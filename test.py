import requests

headers = {"cookie":"JSESSIONID=9C24F9A635C1E65673A0F8388D13036E"}
class ABC:
    def __init__(self,name="ysl"):
        self.name = name

    def __str__(self):
        return "姓名是%s"%self.name

# print(ABC())
# a = ABC("YSS")
# print(a)

class Screen:
    __slots__ = ('__width','height')

    def __init__(self,width=0,height=0):
        self.__width = width
        self.height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

class D(ABC,Screen):
    pass



if __name__ == '__main__':
    # a = Screen()
    # a.width = 10
    # print(a.width)
    print(D.__mro__)
