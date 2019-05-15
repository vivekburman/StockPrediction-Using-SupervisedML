from Controllers.SVMController import SVMController
import os, fnmatch
from tkinter import *
from Controllers.DecisionTreeController import DecisionTreeController

def trigger_process(selected_company, selected_model, option):

    if selected_model == 'SVM':
        svm = SVMController()
        svm.solve_svm(selected_company, option)
    elif selected_model == 'Decision Tree':
        dc = DecisionTreeController()
        dc.solve_decision_tree(selected_company, option)
    return None

def main():
    #use GUI
    window = Tk()
    window.title("Welcome to Stock Predictor")
    window.geometry('350x200')
    window.resizable(width=True, height=True)

    #choose a company
    company_list = [f[:-4] for f in os.listdir('./data_files') if f.endswith('.csv')]
    selected_company = StringVar()
    selected_company.set(company_list[0])
    label = Label(window, text = 'Company: ')
    label.grid(row=0, column=0)
    company_menu = OptionMenu(window, selected_company, *company_list)
    company_menu.grid(row=0, column=1)

    #choose a model
    model_list = ['SVM', 'DC']
    selected_model = StringVar()
    selected_model.set(model_list[0])
    label = Label(window, text = 'Model: ')
    label.grid(row=1, column=0)
    model_menu = OptionMenu(window, selected_model, *model_list)
    model_menu.grid(column=1,row=1)

    #choose Period
    period_list = [1,3]
    selected_period = StringVar()
    selected_period.set(period_list[0])
    label = Label(window, text = 'Period: ')
    label.grid(row=2, column=0)
    period_menu = OptionMenu(window, selected_period, *period_list)
    period_menu.grid(column=1,row=2)

    button_submit = Button(window, text= 'Submit',
        command=lambda: trigger_process(selected_company.get(), selected_model.get(), 
                int(selected_period.get())))
    button_submit.grid(column=1,row=4)
    window.mainloop()
if __name__ == '__main__':
    main()
    print ('Thank You!')
