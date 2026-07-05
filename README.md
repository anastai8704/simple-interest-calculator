# Simple Interest Calculator

A beginner-friendly Python Tkinter application that calculates simple interest using the formula:

SI = (P * R * N) / 100

## Features
- Easy input for Principal, Rate, and Time
- Clear result display
- Beginner-friendly interface

## Project Structure
- app.py: Tkinter GUI application
- simple_interest_calculator.py: Core calculation logic
- tests/test_simple_interest.py: Unit tests for the calculation logic

## Setup Instructions
1. Ensure Python 3 is installed.
2. Clone the repository.
3. Install the required dependencies (none required beyond Python standard library).
4. Run the app:
   ```bash
   python3 app.py
   ```
5. Run tests:
   ```bash
   python3 -m unittest discover -s tests
   ```

## Jenkins with Docker

### Install Jenkins using Docker
```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

### Access Jenkins
1. Open http://localhost:8080
2. Retrieve the initial admin password:
   ```bash
   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```
3. Install the recommended plugins.

### Set up a CI/CD Pipeline in Jenkins
1. Create a new job and choose "Freestyle project".
2. Configure Git repository URL.
3. Add a build step to run tests:
   ```bash
   python3 -m unittest discover -s tests
   ```
4. Optionally add a build step to run the app or package it.
5. Save and run the job to verify the pipeline.

## Learning Notes
This project is designed for beginners to understand:
- Python functions
- Simple formulas
- GUI basics with Tkinter
- Unit testing
- CI/CD basics with Jenkins
