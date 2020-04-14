# Salary-classifier

Open source machine learning classier model which can classify between less/higher than 50k salary's with 91.5% accuracy 

# Project Notes:

* adding mean,median and variance as extra features

* using SVM and Random Forest which provide the lowest error percentage (9.3%).

* each train or test of both classifier is less than a minute.. 

* GUI is easy to use with user interactions and nice picture.

* using threads for each button insuring that the GUI isn't going to freeze until its finish the task if a button is pressed.

* using Gmail API to send model result via mails.



# Project Files:

gmail_send_email.py - provide function to build and send mail using Gmail API

google_api_auth.py - provide Gmail API authentication.

gui.py - configure GUI ,buttons , threads , and GUI main frame.

mail.py - send mail with message using Gmail API

parse_data.py - parse each line of a certain data file, storing and return it as x_vector (train vector) and y_vector(= (label vector)

rf_handler.py - random forest handler class with train and test functions

single_point.py - same as before , i did add to all dictionaries '?' as it gave me better error percentage result.

svm_handler.py - SVM handler  class with train and test functions



## FYI:

* I exclud the client_secret.json which provide the Gmail API credentials, if you want to use the send mail function you will have to add this file.
