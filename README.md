# OCR / DA Python - Project9

## LITReview

Build a website (frontend/backend) using Django

### Introduction

These instructions allow you to :
- get the program
- install the required environment
- run and use it

### Requirements

1. modules
```
packages : python 3.11, python3.11-venv, python3-pip, git
```

### Installation

1. Clone this repo and go in the project's directory

2. Create the virtual environment
```
python3.11 -m venv env
source env/bin/activate
```

3. install environment 
```
pip install -r requirements.txt
```

## Execution

1. Go in the Django project directory
```
cd LITReview
```
2. Initialize the database
```
python manage.py migrate
```
3. Launch the test's server
```
python manage.py runserver
```
## Use  
Browse to http://127.0.0.1:8000

Register/Create a user (or more)  
Then connect ; you can create a Request or a Review  
When multiple users exist, you can follow others and see what they've published


## Author

YaL  <yann@needsome.coffee>

## License

MIT License  
Copyright (c) 2025 