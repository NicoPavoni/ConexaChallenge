# Conexa-Automation-Challenge

## 🏗️ Project Structure <a name="project-structure"></a>

The project is organized into the following key components:
- `screens`: Screens organized as separate class files.
- `step_defs`: Step definition files for each test
- `reports`: Contains the reports that are generated after every execution.

## 📁 Folder Structure <a name="folder-structure"></a>

    .
    ├── reports                        # Reports files
    │   └── reports.html               # Automated tests report on HTML format
    ├── tests                          # Automated tests
    │   ├── step_defs                  # Step definition modules for each test case
    │   └── conftest.py                # Shared configuration for tests
    ├── pytest.ini                     # Command line options
    └── README.md

**Setup Process**

1 - In order to install the project properly, make sure to install all the dependencies by running the following command in the terminal:

    pip install -r requirements.txt 


**EXECUTION**

You can execute all the tests cases by running the following command :

    pytest

Notes : After the execution, pytest will generate an HTML report with the tests results.
