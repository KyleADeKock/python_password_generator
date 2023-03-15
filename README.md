# python_password_generator
This is a basic python flask project. User clicks a button on a web page to generate a random 16 character password.

## Basic Functionality
### Logging
On running the code for the first time a logging file is created from which you can see chars being added to the password

### Secure random numbers
This project makes use of the 'secrets' module to generate secure random numbers that are apparently closer to "true" random number generation than the 'random' module python provides.

### flask and html
flask is used to connect the html templates to the python back end

### testing - pytest
A test file is included and instructions on how to run it is commented within that file.
