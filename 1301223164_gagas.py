# ------------------------------------------------------
# Adding some basic OOP to the simple program
# ------------------------------------------------------

def my_info():
    my_info = {
        "Name": "Gagas Surya Laksana",
        "NIM": "1301223164"
    }
    return my_info

class StudentInfo:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    def get_name(self):
        return self.name

    def get_nim(self):
        return self.nim

    def print_info(self):
        print("Name\t: " + self.get_name())
        print("NIM\t: " + self.get_nim())

# main
my_info_data = my_info()
student = StudentInfo(my_info_data["Name"], my_info_data["NIM"])
student.print_info()
