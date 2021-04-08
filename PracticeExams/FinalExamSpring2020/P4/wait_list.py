
class Student:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.phone) + " " + str(self.address)

    def __lt__(self, other):
        return self.name < other.name

class FunCourse:
    def __init__(self, capacity = 0):
        self.course_list = {}
        self.wait_list = []
        self.max_participants = capacity

    def add_student(self, student):
        if len(self.course_list) < self.max_participants:
            self.course_list[student.id] = student
        else:
            self.wait_list.append(student)
    
    def remove_student(self, id):
        try:
            del self.course_list[id]

            if len(self.wait_list) > 0:
                removed_student = self.wait_list.pop(0)
                self.course_list[removed_student.id] = removed_student
        except:
            for student in self.wait_list:
                if student.id == id:
                    self.wait_list.remove(student)
    
    def get_participant_string(self):
        ordered_list = []
        for id in self.course_list:
            ordered_list.append(self.course_list[id])
        ordered_list.sort()

        ret_str = ""
        for student in ordered_list:
            ret_str += str(student) + "\n"

        return ret_str
    
    def get_wait_list_string(self):
        ret_str = ""

        for student in self.wait_list:
            ret_str += str(student) + "\n"
        
        return ret_str


if __name__ == "__main__":
    course = FunCourse(3)
    course.add_student(Student(123, "Kári Halldórsson", "1234567", "Heimahagar 57"))
    course.add_student(Student(176, "Guðni Magnússon", "87685", "Heimahlíð 2"))
    course.add_student(Student(654, "Jón Jónsson", "54321", "Heimaholt 54"))
    course.add_student(Student(12, "Holgeir Friðgeirsson", "2354456567", "Heimateigur 65"))
    course.add_student(Student(32, "Geir Friðriksson", "99875", "Heimageisli 12"))

    print()
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 654
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 176
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 12
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())