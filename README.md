# NSS Application Translator
This Django web application will take an exported csv file from a HubSpot form and filter the applications by cohort and display them for admin use. 

## Directions for Browser Use:
1. Export form submissions from HubSpot
2. Navigate to formatter.bangazon.com
3. Upload the exported csv file from HubSpot to the application
4. Select the cohort to filter by, or select "All" to get a list of all prospective student applications
5. Click "Upload File"
6. To view a student's application, click on their name in the list 
7. The admin options at the top of the page are clickable dropdowns (without styling for printing purposes)
8. Print!


## Directions for Local Use:
1. create a virtual environment by running `python3 -m pip install --user formatter-env`
2. activate the virtual environment by running`source formatter-env/bin/activate` in the root directory (where your formatter-env directory is)
3. finally, install dependencies for the application by running `pip install -r requirements.txt`
4. to get the application up and running, run `python manage.py runserver` and follow the above steps in your browser!
