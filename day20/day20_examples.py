import numpy

lst = [1,2,3,4,5]
np_arr = numpy.array(lst)
print(np_arr)
print(np_arr * 2)
print(np_arr + 2)


import webbrowser # web browser module to open websites
'''
# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

'''
#unistalling
#pip uninstall packagename
    
#pip list -> To see the installed packages on our machine. We can use pip followed by list.
    
#show package
#pip show packagename
#daha fazla detay için --verbose -> pip show --verbose pandas
    
#PIP Freeze
#Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.
    

'''
get(): to open a network and fetch data from url - it returns a response object
status_code: After we fetched data, we can check the status of the operation (success, error, etc)
headers: To check the header types
text: to extract the text from the fetched response object
json: to extract json data Let's read a txt file from this website,
'''

import requests

url = 'https://sunflower-land.com/play/#/' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page


#read from api

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])

'''
Further Information About Packages
Database

SQLAlchemy or SQLObject - Object oriented access to several different database systems
pip install SQLAlchemy
Web Development

Django - High-level web framework.
pip install django
Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
pip install flask
HTML Parser

Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
pip install beautifulsoup4
PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
XML Processing

ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
GUI

PyQt - Bindings for the cross-platform Qt framework.
TkInter - The traditional Python user interface toolkit.
Data Analysis, Data Science and Machine learning

Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
TensorFlow: is a machine learning library built by Google.
Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
Network:

requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
pip install requests

'''