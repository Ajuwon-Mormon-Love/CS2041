class Student:
 def __init__(self):
   self.first_name = ""
   self.last_name = ""
   self.id = 0
def prompt_student():
 student = Student()
 student.first_name = input("Please enter your first name: ")
 student.last_name = input("Please enter your last name: ")
 student.id = int(input("Please enter your id number: "))
 return student
def display_student(curr_student):
 print(f"{curr_student.id} - {curr_student.first_name} {curr_student.last_name}")
def main():
 my_student = prompt_student()
 print()
 print("Your information:")
 display_student(my_student)
if __name__ == "__main__":
 main()