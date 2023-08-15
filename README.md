Project "Hello, World!" with Continuous Integration (CI) and RPM Packaging

This project represents a simple Python script that prints "Hello, World!".
How to Run Locally

    Install Python 3.8 or newer if not already installed.
    Clone this repository: git clone https://github.com/Jeka4el/HelloWorld-CI
    Navigate to the repository directory: cd your-repo
    Run the script: python hello_world.py

Continuous Integration (CI)

GitHub Actions is configured to execute the following stages:

    Linting: Checks coding style and presence of docstrings.
    Unit Testing: Validates the correct execution of the script.
    RPM Package Creation: Generates an RPM package from the script.
    Upload to GitHub Packages: The RPM package is uploaded to GitHub Packages.

Used Tools and Technologies

    Python 3.8
    Pylint
    unittest
    rpmbuild
    GitHub Actions
    GitHub Packages
