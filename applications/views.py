from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage
from datetime import datetime


def index(request):
    return render(request, 'applications/index.html')

def upload_csv(request):
    """
    # This view allows a user to upload the exported csv file from HubSpot to the application to read
    """
    print("this is running immediately")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.delete('all_applications')
        filename = fs.save('all_applications', myfile)
        uploaded_file_url = fs.url(filename)
        data = request.POST
        
        date = request.POST['application_date']

    return HttpResponseRedirect('/applications/show_applications/' + date)

def show_applications(request, date):
    print("THIS IS THE DATE", date)
    with open('all_applications', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        appData = list()
        for line in csv_reader:

            datetime_object = datetime.strptime(line['Conversion Date'], '%Y-%m-%d %H:%M:%S %p')

            user_datetime = datetime.strptime(date, '%Y-%m-%d')
            # import pdb; pdb.set_trace()
            if datetime_object < user_datetime:
                print(line)
                appData.append(line)

        applicant_names = list()
        for application in appData:
            applicant_name = {
                'first_name': application['First Name'],
                'last_name': application['Last Name'],
                'email': application['Email']
            }
            applicant_names.append(applicant_name)
        print(applicant_names)

        for name in applicant_names:
            print(name['first_name'])
        print(type(applicant_names))

    return render(request, 'applications/show_applications.html', {'applicant_names': applicant_names})



def show_single_application(request, email):

    with open('all_applications', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        appData = list()

        for line in csv_reader:
            appData.append(line)

        singleApp = list()
        for application in appData:
            if application['Email'] == email:
                questions = list(application.keys())
                answers = list(application.values())
                singleApp.append(list(zip(questions, answers)))
            
    return render(request, 'applications/show_single_application.html', {'singleApp': singleApp})