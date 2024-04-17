import time

from datetime import datetime, date

current_time = datetime.now()
print(current_time)



# def lower (st):
#     return st.lower
# st = "HI"
# print(st.lower())  do a change on the attributes of the object
def xyz():
    pass

class Person: #Camel case naming | Data type Object
    pass
    # def __init__(self):   method overloading vs overriding
    #     pass                   by default
    def __init__ (self,name,dob):
        print("New Object")
        self.__name = name
        # self.name = name # attribute # public by default
        self._dob = dob # attribute   # protected
        self.__smart = None  # attribute # private
        self.hands =[] # attribute   # mutable
        pass
    pass


    def __get_name(self):
        return self.__name

    def __set_name(self,name):
        if not name.strip() :
            raise ValueError(f"Person attribute 'name' can not be empty") # clear messaging

        if self.__name is not None:
            raise ValueError(f"Person attribute 'name' is already provided")
        self.__name=name
    name = property(
        fget=__get_name,
        fset=__set_name,
    )
    def get_hands(self):
        return self.hands.copy()
    def eat(self,food): # action     #method
        print(f"{self.name} is eating {food}")
        time.sleep(5)  # waiting 5 second
        print(f"{self.name} finished eating")

    pass


if __name__ =='__main__':
    # ahamd =Person()
    # mohammad = Person()
    osama = Person(name="osama",dob=date(2003,3,6))
    # amro = Person()
    # anas = Person()
    # p1 = Person(name= "Ahamd")
    # p1.eat("Mansaf")
    # p1.eat("Knafa")
    # print(p1.hands)
    # print(p1.get_hands())
    print(osama.__get_name())
    osama.__name ="waleed"
    print(osama.__name())
    print(osama.get_name())
    # osama.set_name("motaz")
    # print(osama._dob)
    # print(isinstance(anas,object))
    # print(isinstance(Person,object))
    # print(isinstance(xyz, object))
