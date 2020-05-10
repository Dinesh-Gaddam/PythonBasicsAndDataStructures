class Lesson1_PythonBasicsAssigment(object):
    """description of class"""


def show_excitement():
    statement ="I am super excited for this course!"
    space=" "
    output=""
    for itr in  range(5):
        output += statement
        output += space

    return output



print(show_excitement())