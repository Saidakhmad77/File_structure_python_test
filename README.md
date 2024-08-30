
This is file structure organization for me later on to look at.

<h2>Python File Structure Recommended Layout</h2>

```
project_root/
│
├── src/
│   ├── __init__.py
│   ├── example.py
│
├── tests/
│   ├── __init__.py
│   ├── t_square.py
│
├── venv
│   ├── bin (or Scripts on Windows)
│   ├── include
│   ├── lib (or Library on Windows)
└── __init__.py
```

<h3>Setup</h3>

1. Create the initial folder and an "app" folder inside of the projects root folder

2. Create a "src" and "tests" directory inside "app" (NO CAPITALIZATIONS)

3. In your terminal type "cd app" to go from your root project directory into your app directory

4. Create your virtual environment, see below

<h3>Virtual Environment Setup</h3>

- In the terminal the command should be similar to this:
  - ```python3 -m venv name_of_virtual_environment```
- Activate the virtual environment
  - Mac/Linux -> ```source name_of_virtual_environment/bin/activate```
  - Windows (gross) -> ```name_of_virtual_environment\Scripts\activate```

- add an __init\__.py to your *app*, *src*, and *tests* directories so that we can make each of them their own module

<h3>Pytest</h3>

- ```pip install pytest``` to install pytest
- ```pytest tests/name_of_testing_file_goes_here.py``` to run that test file

<h3>Organization</h3>

- Put your project files and actual source code inside your *src* directory
- Put any tests inside your *tests* folder (and don't forget to import whichever modules you are attempting to test at the top of the file!) 
