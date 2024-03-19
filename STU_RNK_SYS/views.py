from django.shortcuts import render,redirect
from django.http import request
from datastore.models import Student
import pandas as pd


def home(request):
    data = Student.objects.all()
    student_data = [{'Name': student.name,'Regd_No':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    top_student = df.sort_values(by='CGPA', ascending=False).head(3)
    dept_performance = df.groupby('Department')['CGPA'].mean().reset_index()
    dept_performance_sorted = dept_performance.sort_values(by='CGPA', ascending=False)
    print(dept_performance_sorted)

    context = {
        'top_student': top_student,
        'dept_performance_sorted': dept_performance_sorted, 
    }
    return render(request,'home.html',context)