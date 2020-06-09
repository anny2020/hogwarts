import yaml

class Animal():
    def __init__(self,name,color,age,sex):
        self.name = name
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    @classmethod
    def can_call(cls):
        print("could call")

    @classmethod
    def can_run(cls):
        print("could run")

class Cat(Animal):
    def __init__(self,name,color,age,sex):
        super().__init__(name,color,age,sex)
    hair = "short hair"

    def catch_mouse(self):
        return "caught the mouse"

    def can_run(self):
        print("meow meow~~~")

class Dog(Animal):
    def __init__(self,name,color,age,sex):
        super().__init__(name,color,age,sex)
        self.hair = "long hair"

    def watch_home(self):
        print("could watch home")

    def can_call(self):
        print("bark bark~~~~")

if __name__ == '__main__':
    print("-------------cat---------------------")
    #实例化猫
    cat = Cat("xiaohuang","white",1,'male')
    catch_mouse = cat.catch_mouse()
    cat.can_run()
    print(f"{cat.name,cat.color,cat.age,cat.sex,cat.hair,catch_mouse}")
    print("---------------------dog-----------------------")
    #实例化狗
    dog = Dog("xiaobai","black",2,'female')
    #调用会看家
    dog.watch_home()
    dog.can_call()
    print(f"{dog.name,dog.color,dog.age,dog.sex,dog.hair}")


    #使用Yaml文件的值传参
    with open("data.yaml","r") as f:
        data = yaml.safe_load(f)

    print("---------------yaml  cat-------------------")
    yaml_cat = Cat(data['cat']['name'],data['cat']['color'],data['cat']['age'],data['cat']['sex'])
    yaml_cat.hair = data['cat']['hair']
    yaml_catch_mouse = yaml_cat.catch_mouse()
    print(f"{yaml_cat.name,yaml_cat.color,yaml_cat.age,yaml_cat.sex,yaml_cat.hair,yaml_catch_mouse}")

    print("---------------yaml  dog-------------------")
    yaml_dog = Dog(data['dog']['name'],data['dog']['color'],data['dog']['age'],data['dog']['sex'])
    yaml_dog.hair = data['dog']['hair']
    yaml_dog.watch_home()
    print(f"{yaml_dog.name,yaml_dog.color,yaml_dog.age,yaml_dog.sex,yaml_dog.hair}")
