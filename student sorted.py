class student():
  def __init__(self,name,roll,cgpa):
       self.name=name
       self.roll=roll
       self.cgpa=cgpa

def sortcgpa(sortlist):
  sortedstu=sorted(sortlist, key=lambda x: x.cgpa, reverse=True)
  return sortedstu

stuobj=[student("Deepak","22CS2101",8.9),student("Aswin","22CS2102",8.5),student("Harish","22CS2103",6.3),student("Subu","22CS2104",9.8)]
sortedstu=sortcgpa(stuobj)

for stu in sortedstu:
  print(f"Name: {stu.name}   Roll.no: {stu.roll}    CGPA: {stu.cgpa}")