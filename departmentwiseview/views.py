from django.shortcuts import render
from datastore.models import Student
import pandas as pd


def BCA(request):
    data = Student.objects.filter(department='BCA')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


def BSC_IT(request):
    data = Student.objects.filter(department='BSC(IT)')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


def BSC_PHY(request):
    data = Student.objects.filter(department='BSC(PHY)')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


def BSC_CHE(request):
    data = Student.objects.filter(department='BSC(CHE)')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


def BSC_MAT(request):
    data = Student.objects.filter(department='BSC(MAT)')
    student_data = [{'Name': student.name,'Regd_No':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


def BSC_BOT(request):
    data = Student.objects.filter(department='BSC(BOT)')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)

def BSC_ZOO(request):
    data = Student.objects.filter(department='BSC(ZOO)')
    student_data = [{'Name': student.name,'Regd_No.':student.registration_number,'Department':student.department,'Semester':student.semester,'SGPA':student.sgpa,'CGPA': student.cgpa} for student in data]
    df = pd.DataFrame(student_data)
    sorted_df = df.sort_values(by='CGPA', ascending=False)
    context = {
        'sorted_df': sorted_df,  
    }
    print(sorted_df)
    return render(request, 'departmentview.html', context)


