#encoding = utf-8
#作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
class Student():
    def __init__(self,name,age,sex,classname,homework):
        self.name = name
        self.age = age
        self.sex = sex
        self.classname = classname
        self.homework = homework

#有返回值
    def student_info(self):
        student_info = self.name + ": " + str(self.age) +  " " + self.sex + " " + self.classname
        return student_info
#无返回值
    def do_homework(self):
        print(f"{self.name}要做的作业是：{self.homework}。")

#默认参数
    def get_score(self,score,name="李华"):
        print(f"{name}的成绩是: {score}")

#传参数
student = Student("张三",10,'男',"三一班","写一篇作业")
get_info = student.student_info()
print(get_info)
#无参数
student.do_homework()
#默认参数
student.get_score(90)




