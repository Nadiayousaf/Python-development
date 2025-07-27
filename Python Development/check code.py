


def smart_marks_processor():
    student_name=input("Enter names:").split(",")
    marks=input("Enter marks:").split(",")
    marks=list(map(int,marks))
    paired=zip(list(student_name),(marks))

    filter_marks=filter(lambda m:m[1]>=50,paired)
    result=map(lambda x:f"{x[0]}-passed with {x[1]}%",filter_marks)

    for lines in result:
      print(lines)

smart_marks_processor()