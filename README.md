# NSS Application Translator
Due to the nature of our application process - prospective students may apply more than once, they may leave an answer blank, etc., NSS needed a system to track the current state of form submissions in HubSpot. This Django web application will take an exported csv file from a HubSpot form and filter the applications by cohort and display them for admin use.

## Directions for Browser Use:
0. Export form submissions from HubSpot
1. Navigate to [formatter.bangazon.com](formatter.bangazon.com) in your browser (the hosted version)
2. Upload the exported csv file from HubSpot to the application
3. Select the cohort to filter by, or select "All" to get a list of all prospective student applications
4. Click "Upload File"
5. To view a student's application, click on their name in the list
6. The admin options at the top of the page are clickable dropdowns (without styling for printing purposes)
7. Print!


## Directions for Local Use:
1. Clone the repository to your local machine
2. Create a virtual environment by running `python3 -m pip install --user formatter-env`
3. Activate the virtual environment by running `source formatter-env/bin/activate` in the root directory (where your formatter-env directory is located)
4. Finally, install dependencies for the application in the virtual environment by running `pip install -r requirements.txt`
5. To get the application up and running locally, run `python manage.py runserver` and follow the above steps in your browser

## Docker Version

1. `docker-compose build`
1. `docker-compose run apphost manage.py collectstatic --no-input`
1. `docker-compose up`