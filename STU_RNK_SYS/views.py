from django.shortcuts import render

def login(request):
    return render(request,'login.html')


# def home(request):
#     data = Student.objects.all()
#     student_data = [{'Name': student.name,'Regd_No':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
#     df = pd.DataFrame(student_data)
#     top_students = df.sort_values(by='CGPA', ascending=False).head(3)
#     top_students['Rank'] = ['1st', '2nd', '3rd'] 
#     print(top_students)
#     # dept_performance = df.groupby('Department')['CGPA'].mean().reset_index()
#     # dept_performance_sorted = dept_performance.sort_values(by='CGPA', ascending=False)
#     context = {
#         'top_student': top_students
#         # 'dept_performance_sorted': dept_performance_sorted, 
#     }
#     print(context)
#     return render(request,'home.html',context)

# def home(request):
#     data = Student.objects.all()
#     student_data = [{'Name': student.name, 'Regd_No': student.registration_number, 'Department': student.department,'Semester': student.semester, 'SGPA': student.sgpa, 'CGPA': student.cgpa} for student in data]
#     df = pd.DataFrame(student_data)
#     topthree = df.sort_values(by='CGPA', ascending=False).head(3)
#     print(topthree)
#     context = {
#         'topstudents': topthree,
#     }
#     print(context)
#     return render(request, 'homee.html', context)

