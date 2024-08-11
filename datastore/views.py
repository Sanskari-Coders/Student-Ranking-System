from django.shortcuts import render,redirect
from django.contrib import messages 

from datastore.models import Student
import pandas as pd
# Create your views here.

def upload_data(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if Student.objects !=None:
            Student.objects.all().delete()
            df = pd.read_excel(myfile)
        for index, row in df.iterrows():
            student = Student.objects.create(
                registration_number=row['STUDENT REGISTRATION NUMBER'],
                name=row['STUDENT NAME'],
                department=row['DEPARTMENT'],
                semester=row['SEMESTER'],
                sgpa=row['SGPA'],
                cgpa=row['CGPA']
            )
            student.save()
        return redirect('HOME')
    return render(request, 'admin.html')

