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
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.delete('all_applications')
        filename = fs.save('all_applications', myfile)
        uploaded_file_url = fs.url(filename)
        data = request.POST

        cohortSort = request.POST['cohort']

    return HttpResponseRedirect('show_applications/' + cohortSort)

def show_applications(request, cohortSort):
    with open('all_applications', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        cohorts = {
            "C32": "April 2019 Full-time (Day) Web Developer Bootcamp",
            "C33": "May 2019 Full-time (Day) Web Developer Bootcamp",
            "DA1": "May 2019 Part-time Data Analytics Bootcamp",
            "C34": "July 2019 Full-time (Day) Web Developer Bootcamp",
            "DS3": "August 2019 Data Science Bootcamp",
            "E10": "August 2019 Part-time (Evening) Web Developer Bootcamp",
            "C35": "August 2019 Full-time (Day) Front-end Web Designer/Developer Bootcamp",
            "C36": "October 2019 Full-time (Day) Web Developer Bootcamp",
            "C37": "November 2019 Full-time (Day) Web Developer Bootcamp"
        }

        cohortsAppliedTo = list()
        appData = list()

        for line in csv_reader:
            cohortsAppliedTo = line['Which student cohort / program date are you applying for?']
            if(cohortSort == "All"):
                appData.append(line)
            elif cohorts[cohortSort] in cohortsAppliedTo:
                appData.append(line)


        applicant_names = list()
        for application in appData:
            date = datetime.strptime(application['Conversion Date'], '%Y-%m-%d %H:%M:%S %p')
            applicant_name = {
                'first_name': application['First Name'],
                'last_name': application['Last Name'],
                'email': application['Email'],
                'date' : date,
                'cohort': cohortSort
            }
            applicant_names.append(applicant_name)

    return render(request, 'applications/show_applications.html', {'applicant_names': applicant_names})



def show_single_application(request, email, cohort):

    cohorts = {
            "C32": "April 2019 Full-time (Day) Web Developer Bootcamp",
            "C33": "May 2019 Full-time (Day) Web Developer Bootcamp",
            "DA1": "May 2019 Part-time Data Analytics Bootcamp",
            "C34": "July 2019 Full-time (Day) Web Developer Bootcamp",
            "DS3": "August 2019 Data Science Bootcamp",
            "E10": "August 2019 Part-time (Evening) Web Developer Bootcamp",
            "C35": "August 2019 Full-time (Day) Front-end Web Designer/Developer Bootcamp",
            "C36": "October 2019 Full-time (Day) Web Developer Bootcamp",
            "C37": "November 2019 Full-time (Day) Web Developer Bootcamp"
        }

    with open('all_applications', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        appData = list()
        for line in csv_reader:
            appData.append(line)

        singleApp = list()
        for application in appData:
            if application['Email'] == email and cohorts[cohort] in application['Which student cohort / program date are you applying for?']:
                questions = list(application.keys())[:-1]
                answers = list(application.values())[:-1]
                singleApp.append(list(zip(questions, answers)))

        applicantName = singleApp[0][0][1] + " " + singleApp[0][1][1]

    return render(request, 'applications/show_single_application.html', {'singleApp': singleApp, 'applicantName': applicantName})