
class Employee:
  holidays=["new year"]
  def __init__(self,id,dept,salary):
    self.id=id
    self.dept=dept
    self.salary=salary
  def get_tax(self):
    return 0.3*self.salary
  @classmethod
  def get_holidays(cls):
    return cls.holidays
emp1=Employee(1,"AB",10)
emp2=Employee(2,"BC",20)
print(emp1.get_tax())
print(emp2.get_tax())
print(Employee.get_holidays())




