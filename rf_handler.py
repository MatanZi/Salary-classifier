# Import svm model

import time

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

from calc_error_pct import *
from parse_data import parse_data


# Random Forset handler class
class RFHandler:
    """ In this class you will implement the classifier and it's methods. """
    '''
    @:param 
    data_file_full_path : location of the data file
    test_file_full_path : location of the test file
    classifier : Instance of the classifier model
    sc : Instance of the StandardScaler 
    self.X_train : data model vector
    self.y_train : data label vector
    self.X_test : test model vector
    self.y_test : test label vector
    self.y_pred : prediction vector
    self.error_percentage : error_percentage value
    '''

    def __init__(self, data_file_full_path, test_file_full_path):
        self.data_file_full_path = data_file_full_path
        self.test_file_full_path = test_file_full_path
        self.classifier = RandomForestClassifier(n_estimators=2000, criterion='entropy')
        self.sc = StandardScaler()
        self.X_train, self.y_train, self.X_test, self.y_test, self.y_pred, self.error_percentage = ([],) * 6

    # Training the model
    def train(self):
        try:
            start_time = time.time()
            # Train the model using the training sets
            print("Start training...")
            self.X_train, self.y_train = parse_data(self.data_file_full_path)
            self.X_test, self.y_test = parse_data(self.test_file_full_path)

            self.X_train = self.sc.fit_transform(self.X_train)
            self.X_test = self.sc.fit_transform(self.X_test)

            self.classifier.fit(self.X_train, self.y_train)


        except Exception as err:
            print("Error: ", err)

        finally:
            print("---Train: %s seconds ---" % (time.time() - start_time))

    # Testing the model
    def test(self):
        try:
            start_time = time.time()
            # Predict the response for test dataset
            print("Start predicting...\n")
            self.y_pred = self.classifier.predict(self.X_test)

            # print(confusion_matrix(y_test, y_pred))
            # print(classification_report(self.y_test, self.y_pred))

            # Model Accuracy: how often is the classifier correct?
            print("Accuracy:", metrics.accuracy_score(self.y_test, self.y_pred) * 100, "%")

            # Model Precision: what percentage of positive tuples are labeled as such?
            # print("Precision:", metrics.precision_score(self.y_test, self.y_pred) * 100, "%")

            # Model Recall: what percentage of positive tuples are labelled as such?
            # print("Recall:", metrics.recall_score(self.y_test, self.y_pred) * 100, "%")

            print("calculate_error_percentage:", calculate_error_percentage(self.y_pred, self.y_test))

            self.error_percentage = calculate_error_percentage(self.y_test, self.y_pred)
        except Exception as err:
            print("Error: ", err)

        finally:
            print("\n---Predication: %s seconds ---" % (time.time() - start_time))

# rf = RFHandler("data/adult.data", "data/adult.test")
# rf.train()
# rf.test()
