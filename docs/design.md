#Sample Web Filtering Application
##General
This project was create per request from a recruiter to demonstrate design and implementation habit.
The project provides a framework for a simple web-filter application based on flask.
There are parts of the implementations that can be easily replaced by flask features or other 3rd party package, the 
not to use such packages was intentional.
##Requirement
* Implement flask based web-filtering application.
* Web browser will be configured to use the app as a proxy.
* The framework will load "plugins" that will perform the filtering.
* The system will have a configuration interface for changing various parameters such as:
    * incoming port.
    * Enable/Disable flag.
    * "plugin" configuration.
    * Block page.
* The system will use default python library to log activity and errors
