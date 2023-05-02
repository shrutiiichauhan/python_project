
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



root = tk.Tk()
root.geometry('300x100')
# root2=tk.Tk()
# root2.title('This is Second Window')
# root2.geometry('300x100')
data_label = tk.Label(root)
data_label2 = tk.Label(root)
data_label2.grid(row=7 , columns=1)
data_label.grid(row=8, columns=1)

def schedule():
    name = teacher_combobox.get()
    day = day_combobox.get()
            
    
    df = pd.read_excel(f"C:\\Users\\HP\\Desktop\\python\\demo\\time_table.xlsx" , sheet_name="Sheet3" )

    if day == 'Select Day' or name == "Select teacher" :
        
        # show messege for inappropriate input 
        messagebox.showinfo("Message", "Pls select proper day and name")
    
    elif day == 'All' :
            # pandas query search
        schedule_data = df[(df.faculty_name == name)]
         





        data_str = "'subject' ,' faculty_name' , 'day '  , 'starting_time' ,' ending_time' , 'session_type' , 'class_lab' ,' division'"
        data_label2.config(text = data_str)
        data_str = ''
        

        


        j=8
        div = []
        for i, row in schedule_data.iterrows():
            
            data_str += f"{row['subject']}    ,    {row['faculty_name']}   ,   {row['day']}   ,    {row['starting_time']}   ,   {row['ending_time']}    ,     {row['session_type']}   ,    {row['class_lab']}     ,    {row['division']}\n"
            
            button_str = f"{row['division'] }"
            div.append(button_str)
            check_schedule = tk.Button(root, text=button_str)
            check_schedule.grid(row = j , column= 2,pady=5,padx=5)
            j+=1

        data_label.config(text=data_str)

            
            





    elif df[df.day == day].empty:
        messagebox.showinfo("Message", "No schedule at that day")
    
    else : 
        
        # pandas query based on faculty_name and day in excel
        schedule_data = df[(df.faculty_name == name) &(df.day == day)]
        # print(schedule_data)
        
        data_str = "'subject' ,' faculty_name' , 'day '  , 'starting_time' ,' ending_time' , 'session_type' , 'class_lab' ,' division'"
        data_label2.config(text = data_str)
        data_str = ''
        j=8
        div = []
        for i, row in schedule_data.iterrows():
            data_str += f"{row['subject']}    ,    {row['faculty_name']}   ,   {row['day']}   ,    {row['starting_time']}   ,   {row['ending_time']}    ,     {row['session_type']}   ,    {row['class_lab']}     ,    {row['division']}\n"

            button_str = f"{ row['division'] }"
            div.append(button_str)
            check_schedule = tk.Button(root, text=button_str)
            check_schedule.grid(row = j , column= 2,pady=5,padx=5 )
            j+=1
        data_label.config(text=data_str)

            
# Create the login form widgets
teacher = ['Select teacher' , 'snehal_sir' , 'shivangi_mam']
teacher_combobox = ttk.Combobox(root, values=teacher)
teacher_combobox.current(0)
teacher_combobox.grid(row = 0, column=0)


days = ['Select Day','All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_combobox = ttk.Combobox(root, values=days)
day_combobox.current(0)
day_combobox.grid(row = 1, column=0)


check_schedule = tk.Button(root, text='Check Schedule', command=schedule)
check_schedule.grid(row = 3 , column= 0 , pady=5)

root.mainloop()






