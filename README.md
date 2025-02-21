# Gas Utility Customer Service Management System 

This Django-based application is designed to help a gas utility company manage high volumes of customer service requests efficiently. It provides features for customers to submit service requests, track their status, and manage their accounts. Additionally, customer support representatives can manage and resolve service requests.




## Features 

- Create Service Request: Users can fill out a form to create service requests, upload attachments, and specify request types.

- Track Request Status: View the status of your submitted service requests at any time.

## Technology Stack 

Backend: Django (Python Framework) Frontend: HTML, CSS Database: SQLite (default Django database)



## Setup Instructions

Follow these steps to set up the project on your local system:

1.Clone the repository: git clone cd gas_utility_project

2.Install dependencies: pip install -r requirements.txt

3.Apply migrations: python manage.py makemigrations python manage.py migrate

4.Run the server: python manage.py runserver : Open your browser and navigate to http://127.0.0.1:8000/service/create/ to create a service request.




