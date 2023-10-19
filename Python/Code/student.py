# Define class
class Student:
    def __init__(self,name, location):
        self.name = name
        self.location = location
def main():
    student = get_student()
    print(f"{student.name}")

def get_student():
    name = input("Enter Name:")
    location = input ("Enter location: ")
    student = Student(name,location)
    return student
if __name__ == "__main__":
    main()