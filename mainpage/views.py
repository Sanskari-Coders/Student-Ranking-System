from django.shortcuts import render
from datastore.models import Student
import pandas as pd
# Create your views here.
import pandas as pd


def mainpage(request):
    data = Student.objects.all()
    student_data = [{'Name': student.name,
                     'Regd_No': student.registration_number,
                     'Department': student.department,
                     'Semester': student.semester,
                     'SGPA': student.sgpa,
                     'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    topstudents = df.sort_values(by='CGPA', ascending=False).head(3).to_dict(orient='records')
    for i, student in enumerate(topstudents):
        student['Rank'] = i + 1
    
    dept_performance = df.groupby('Department')['CGPA'].mean().reset_index()
    dept_performance_sorted = dept_performance.sort_values(by='CGPA', ascending=False).to_dict(orient='records')
    
    total_students=df.sort_values(by='CGPA',ascending=False).__len__()
    context = {'topstudents': topstudents,
               'dept_performance':dept_performance_sorted,
               'total_students':total_students}
    return render(request, 'mainpage.html', context)
