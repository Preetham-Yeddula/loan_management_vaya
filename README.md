# FastAPI Loan Application

This is a sample FastAPI application for managing loan applications.

## Setup Guide

Follow these steps to set up and run the FastAPI Loan Application:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository_url>
```

### 2. Install Dependencies

Navigate to the project directory and install the Python dependencies using pip:

```bash
cd loan_management_vaya
pip install -r requirements.txt
```

### 2.a Connection String

The password for the connection string will be provided in the mail or chat of wellfound along with the submittion link

### 3. Run the Application

Start the FastAPI application using the following command:

```bash
uvicorn app.main:app --reload
```

### 4. Test the Application

Import the provided Postman collection to test REST APIs

## Structure

Backend built using FastAPI framework of python
Database is a free tier mongodb storage hosted on AWS

Please reach out to me for access credentails to that DB cluster

```
app
├── Utils
│   ├── DataStoreInterface.py
│   ├── DictDataStore.py
│   └── MongoDataStore.py
├── controllers
│   └── loan_controller.py
├── main.py
├── models
│   └── loan_application.py
├── repositories
│   └── loan_repository.py
├── routes
│   └── loan.py
└── services
    └── risk_assessment.py
```
loan_repository.py - accepts Objects of IDataStore(in DataStoreInterface) as input 
loan_controller.py - injects that into loan_repository

## To-Do

### Non-functional
- Dockerize the application
- move the connection string to secret manager
- Unit-test case

### Code level enhancements
- using Strategy pattern for the decision taking
- add the dependency injection to all the layers of code
