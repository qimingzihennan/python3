class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %d' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    student1 = Student('Bart Simpson', 59)
    name = student1.name
    print("name:" + str(name))
    score = student1.score
    print("score:" + str(score))

    student1.print_score()
    evaluate = student1.get_grade()
    print("评价:" + evaluate)
    print("=============")
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.age = 8
    print("bart.age:" + str(bart.age))
    lisa.age = 12312
    print("lisa.age:" + str(lisa.age))
    print("bart.age:" + str(bart.age))
    bart = lisa
    print("bart.age:" + str(bart.age))
