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

    return HttpResponseRedirect('show_applications/' + date)

def show_applications(request, date):
    with open('all_applications', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        appData = list()
        for line in csv_reader:

            datetime_object = datetime.strptime(line['Conversion Date'], '%Y-%m-%d %H:%M:%S %p')

            user_datetime = datetime.strptime(date, '%Y-%m-%d')
            # import pdb; pdb.set_trace()
            if datetime_object < user_datetime:
                appData.append(line)

        applicant_names = list()
        for application in appData:
            date = datetime.strptime(application['Conversion Date'], '%Y-%m-%d %H:%M:%S %p')
            applicant_name = {
                'first_name': application['First Name'],
                'last_name': application['Last Name'],
                'email': application['Email'],
                'date' : date
            }
            applicant_names.append(applicant_name)

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
                questions = list(application.keys())[:-1]
                answers = list(application.values())[:-1]
                singleApp.append(list(zip(questions, answers)))


        applicantName = singleApp[0][0][1] + " " + singleApp[0][1][1]
            
    return render(request, 'applications/show_single_application.html', {'singleApp': singleApp, 'applicantName': applicantName})