class Student:
  exam_given=[]
  def __init__(self,id):
    self.roll_no=id
    self.college="PWIOI"
st1=Student(5)
st2=Student(7)
st1.exam_given.append("jee")
st2.exam_given.append("neet")
print(st1.roll_no)
print(st2.roll_no)
print(st1.exam_given)
print(st2.exam_given)
print(st1.college)
