class student:
    def __init__(self, name, mark, dept):
          self.name = name
          self.mark = mark
          self.dept = dept

    def display(self):
          print("name=", self.name)
          print("mark=", self.mark)
          print("dept=", self.dept)
student1 = student("roshmi", 100, "mca")
student1.display()