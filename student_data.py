import pandas as pd
import tkinter as tk
import csv
from tkinter import messagebox

# Read the CSV data into a DataFrame object
df = pd.read_excel("C:\\Users\\HP\\Desktop\\python\\demo\\4CEC.xlsx")

# Create a tkinter window
window = tk.Tk()
window.title('CSV Data')

# Create a Label widget to display the data
data_label = tk.Label(window)
data_label.grid()
heading_label = tk.Label(window, text='4-CE-C CLASS', font=('Arial', 24, 'bold'))
heading_label.grid(row=1,column=2, sticky='nsew')


checkbox_values=[]
j=3
# Loop through the rows of the DataFrame and concatenate the data into a string
data_str = ''
for i, row in df.iterrows():
        var = tk.BooleanVar()
        data_str += f"{row['NO']}, {row['NAME']}, {row['ENROLL_NO']}\n"


        checkbox = tk.Checkbutton(window,text=data_str ,variable=var , onvalue=True , offvalue=False )
        checkbox_values.append(var)


        data_str=''
         # checkbox.pack()
        checkbox.grid(row=j, column=2, padx=100)
        j+=1


def store():
    # create a list of the checkbox values
    checkbox_state_list = []
    for checkbox_var in checkbox_values:
        checkbox_state_list.append(checkbox_var.get())

    # convert the checkbox values to "Present" or "Absent" status strings
    status_list=[]
    for checkbox_state in checkbox_state_list:
        if checkbox_state == True:
            status_list.append("Present")
        else:
            status_list.append("Absent")

    # read the original CSV file into a DataFrame
    df = pd.read_excel("C:\\Users\\HP\\Desktop\\python\\demo\\4CEC.xlsx")

    # create a new DataFrame with the updated status values
    new_df = pd.DataFrame({
            'roll_no': df['NO'],
        'name': df['NAME'],
        'enroll_no': df['ENROLL_NO'],
        'status': status_list
    })

    # write the new DataFrame to the output CSV file
    new_df.to_csv("C:\\Users\\HP\\Desktop\\python\\demo\\FINAL_4ITC - Sheet1.csv", index=False)



#     # create a list of the checkbox values
#     checkbox_state_list = []
#     for checkbox_var in checkbox_values:
#         checkbox_state_list.append(checkbox_var.get())

#     status_list=[]
#     for  i in range(len(checkbox_state_list)):
#         if  i == True :
#              status_list.append("Present")
#         else :
#              status_list.append("Absent")

#     df2 = pd.read_csv("C:\\Users\\HP\\Desktop\\python\\demo\\FINAL_4ITC - Sheet1.csv")
#     appended_data = pd.DataFrame(columns=['roll_no', 'name', 'enroll_no','status'])
#     for i in range(len(checkbox_state_list)):
#         row_data = {'roll_no': df['No'], 'name': df['NAME'], 'enroll_no':df['ENROLL_NO'],'status':status_list}
#         # appended_data = appended_data.append(row_data, ignore_index=True)


#     # write the checkbox values to the CSV file

#     for i in range(len(checkbox_state_list)):
#         if i == True:
#             status = "present"
#         else :
#              status = "absent"
         
    # ceate a button to save the checkbox values to the CSV file
tk.Button(window, text='Save', command=store).grid(row=j+1,column=2)

# Start the tkinter event loop
window.mainloop()
