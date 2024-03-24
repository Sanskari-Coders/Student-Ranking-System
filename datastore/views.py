from django.shortcuts import render,redirect
from django.contrib import messages 

from datastore.models import Student
from datastore.models import data_store
import pandas as pd
# Create your views here.

def upload_data(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        myfile.name='ranks.xlsx'
        newfile=data_store(excel=myfile)
        newfile.save()
        data = pd.read_excel('media/DATA/ranks.xlsx')
        Student.objects.all().delete()
        for index, row in data.iterrows():
            student = Student.objects.create(
                registration_number=row['STUDENT REGISTRATION NUMBER'],
                name=row['STUDENT NAME'],
                department=row['DEPARTMENT'],
                semester=row['SEMESTER'],
                sgpa=row['SGPA'],
                cgpa=row['CGPA']
            )
            student.save()
            print(student.registration_number)
        return redirect('HOME')
    return render(request, 'admin.html')