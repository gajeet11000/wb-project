# WhatBytes Project

## To get it run locally follow these steps:

1. Clone the repository using `git clone https://github.com/gajeet11000/wb-project.git`
2. Change into the directory `cd wb-project`
3. Create a virtual environment `python -m venv venv` (on Windows) or `python3 -m venv venv` (on macOS/Linux)
4. Activate the virtual environment `venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on macOS/Linux)
5. Install the dependencies `pip install -r requirements.txt`
6. Run the migrations `python manage.py migrate`
7. Run the server `python manage.py runserver`
8. Go to `https://localhost:8000`