from concurrent import futures

from rf_handler import RFHandler

__author__ = 'wolfenfeld'

from tkinter import messagebox
from tkinter import *
from svm_handler import SVMHandler
from mail import sendemail
import threading

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)


def run_gui():
    root = Tk()
    root.title("SVM & RF GUI")
    # Here you need to set the frame, grid, row and column configurations of the root.

    # Root Configuration
    root_photo = PhotoImage(file="download.png")
    w = root_photo.width()
    h = root_photo.height()
    root.geometry("%dx%d+0+0" % (w, h))
    label_for_image = Label(root, image=root_photo)
    label_for_image.pack()

    # Creating main screen title
    root_title_label = Label(root, text="Welcome !\n              Please choose a button:")
    root_title_label.config(font=("Courier", 35))
    root_title_label.place(relx=0.2, rely=0.1, anchor=N)

    # Creating classifier Instance
    svm_handler = SVMHandler("data/adult.data", "data/adult.test", "rbf")
    rf_handler = RFHandler("data/adult.data", "data/adult.test")

    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?

    # a function to train the svm classifier
    def train_svm():
        try:
            print('train_svm')
            svm_handler.train()
            messagebox.showinfo("Information", "Done SVM training")

        except Exception as err:
            print("Error: ", err)

        finally:
            return

    # a function to train the rf classifier
    def train_rf():
        try:
            print('train_rf')
            rf_handler.train()
            messagebox.showinfo("Information", "Done RF training")

        except Exception as err:
            print("Error: ", err)

        finally:
            return

    # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?

    # a function to test the svm classifier
    def test_svm():
        try:
            print("test_svm")
            if svm_handler.X_train is not None:
                svm_handler.test()
                svm_handler.X_train = []
                messagebox.showinfo("Information", "Done SVM testing")
            else:
                messagebox.showerror("Error", "Train first !")


        except Exception as err:
            print("Error: ", err)

        finally:
            return

    # a function to test the rf classifier
    def test_rf():
        try:
            print('test_rf')
            if rf_handler.X_train is not None:
                rf_handler.test()
                rf_handler.X_train = []
                messagebox.showinfo("Information", "Done RF testing")
            else:
                messagebox.showerror("Error", "Train first !")



        except Exception as err:
            print("Error: ", err)

        finally:
            return

    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?

    # a function to sent mail using Gmail API
    def send_mail():
        try:
            if svm_handler.error_percentage:
                message = "Hello Hadas,\n" \
                          "Im done working on the project \n " \
                          "The lowest error percentage using SVM classifier i manage to get is: " + str(
                    svm_handler.error_percentage) + "%\n\n\n" \
                                                    "Best Regards\n" \
                                                    "Matan Zilka"
                svm_handler.error_percentage = []
                sendemail(message)
                messagebox.showinfo("Information", "Mail sent")

            elif rf_handler.error_percentage:
                message = "Hello Hadas,\n" \
                          "Im done working on the project \n " \
                          "The lowest error percentage using Random Forest classifier i manage to get is: " + str(
                    rf_handler.error_percentage) + "%\n\n\n" \
                                                   "Best Regards\n" \
                                                   "Matan Zilka"

                rf_handler.error_percentage = []
                sendemail(message)
                messagebox.showinfo("Information", "Mail sent")

            else:
                messagebox.showerror("Error", "Train and test first !")


        except Exception as err:
            print("Error: ", err)

        finally:
            return

    # Configure thread objects
    train_thread_svm = threading.Thread(target=train_svm, daemon=True)
    train_thread_rf = threading.Thread(target=train_rf, daemon=True)
    test_thread_svm = threading.Thread(target=test_svm, daemon=True)
    test_thread_rf = threading.Thread(target=test_rf, daemon=True)
    send_mail_thread = threading.Thread(target=send_mail, daemon=True)

    # a function to determine which thread to start using GUI buttons (user interaction)
    def function_chooser(thread_to_start):
        try:
            if thread_to_start.isAlive():
                thread_to_start.join()
            else:
                thread_to_start.start()

        except Exception as err:
            print("Error: ", err)

        finally:
            return

    '''
    def function_selector(fun_num):
        try:
            if(fun_num == 1 and flag_1):
                flag_1 = True
                return thread_pool_executor.submit(train_svm()),
            elif(fun_num == 2 and flag_2):
                flag_2 = True
                return thread_pool_executor.submit(test_svm()),
            elif (fun_num == 3 and flag_3):
                flag_3 = True
                return thread_pool_executor.submit(train_rf()),
            elif (fun_num == 4 and flag_4):
                flag_4 = True
                return thread_pool_executor.submit(train_rf()),
            elif (fun_num == 5 and flag_5):
                flag_5 = True
                return thread_pool_executor.submit(send_mail())

            return
        except Exception as err:
            print("Error: ", err)

        finally:
            return
    '''

    # Here you need to implement three buttons, one for each action.

    # Configure train button for SVM
    train_svm_btn = Button(root, text="Activate SVM train", height=3, width=25,
                           command=lambda: train_thread_svm.start())
    train_svm_btn.place(relx=0.2, rely=0.85, anchor=S)

    # Configure test button for SVM
    test_svm_btn = Button(root, text="Activate SVM test", height=3, width=25,
                          command=lambda: function_chooser(test_thread_svm))
    test_svm_btn.place(relx=0.5, rely=0.85, anchor=S)

    # Configure train button for RF
    train_rf_btn = Button(root, text="Activate RF train ", height=3, width=25,
                          command=lambda: function_chooser(train_thread_rf))
    train_rf_btn.place(relx=0.2, rely=0.95, anchor=S)

    # Configure test button for RF
    test_rf_btn = Button(root, text="Activate RF test", height=3, width=25,
                         command=lambda: function_chooser(test_thread_rf))
    test_rf_btn.place(relx=0.5, rely=0.95, anchor=S)

    # Configure send_mail button
    send_mail_btn = Button(root, text="Send mail", height=3, width=25,
                           command=lambda: function_chooser(send_mail_thread))
    send_mail_btn.place(relx=0.8, rely=0.9, anchor=S)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
