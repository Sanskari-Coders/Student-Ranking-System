from django.shortcuts import render
from datastore.models import Student
import pandas as pd

def login(request):
    return render(request,'login.html')


def OVERALL(request):
    data=Student.objects.all()
    student_data = [{'Name': student.name,'Regd_No':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    students_count = df.__len__()
    overall=True
    context = {
        'sorted_df': sorted_df,
        'students_count': students_count,
        'isoverall':overall,  
    }
    print(sorted_df)
    return render(request, 'overal.html',context=context)


def topten(request):
    data=Student.objects.all()
    student_data = [{'Name': student.name,'Regd_No':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False).head(10)
    students_count = sorted_df.__len__()
    overall=True
    context = {
        'sorted_df': sorted_df,
        'students_count': students_count,
        'isoverall':overall,  
    }
    print(sorted_df)
    return render(request, 'top10.html',context=context)


