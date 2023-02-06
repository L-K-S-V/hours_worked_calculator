import datetime as dt
import tkinter
import customtkinter as ctk
import webbrowser
from PIL import Image, ImageTk



# Custom Tkinter Documentation: https://github.com/TomSchimansky/CustomTkinter/wiki
ctk.set_appearance_mode("dark") # This makes it dark regardless of system settings
ctk.set_default_color_theme("blue") # Themes: "blue" (standard), "green", "dark-blue"

# ***** IMAGES *****
# ******************
lv_logo = ctk.CTkImage(dark_image=Image.open(r"\\HCLV_Server\home\Programming\Projects\Python\Programs\Hours Worked Calculator\images\lv_logo_grau.png"), size=(60, 32))



# ***** TKinter MAIN WINDOW *****
# *******************************
main_window = ctk.CTk()
main_window.geometry("340 x 480")
main_window.minsize(340, 480) # WIDTH x HEIGHT
#main_window.maxsize(250, 390) # WIDTH x HEIGHT
main_window.title("Hours Worked Calculator")
main_window.iconbitmap(r"\\HCLV_Server\home\Programming\Projects\Python\Programs\Hours Worked Calculator\images\lv_icon_grau.ico") # Window icon

# ***** FUNCTIONS *****
# *********************

switch_morning_var = ctk.StringVar(value="no")
switch_afternoon_var = ctk.StringVar(value="no")

def switch_morning_event():
    pass

def switch_afternoon_event():
    pass

def total_time_calc ():
    """ This clusterfuck needs tidying up """
    global calc_result_hrs
    global calc_result_min
    get_start_hrs = int(entry_work_start_hrs.get())
    get_start_min = int(entry_work_start_min.get())
    morning_break_extra_15 = 15 #minutes
    get_lunch_start_hrs = int(entry_lunch_start_hrs.get())
    get_lunch_start_min = int(entry_lunch_start_min.get())
    get_lunch_end_hrs = int(entry_lunch_end_hrs.get())
    get_lunch_end_min = int(entry_lunch_end_min.get())
    afternoon_break_extra_15 = 15 #minutes
    get_end_hrs = int(entry_work_end_hrs.get())
    get_end_min = int(entry_work_end_min.get())
    #print(f"'get_start_hrs and mins {get_start_hrs}:{get_start_min}")
    #print(f"'get_end_hrs and mins {get_end_hrs}:{get_end_min}")
    time_started = dt.timedelta(hours=get_start_hrs, minutes=get_start_min)
    time_no_morning_break = dt.timedelta(minutes=morning_break_extra_15)
    time_lunch_started = dt.timedelta(hours=get_lunch_start_hrs, minutes=get_lunch_start_min)
    time_lunch_finished = dt.timedelta(hours=get_lunch_end_hrs, minutes=get_lunch_end_min)
    time_no_afternoon_break = dt.timedelta(minutes=afternoon_break_extra_15)
    time_finished = dt.timedelta(hours=get_end_hrs, minutes=get_end_min)
    time_difference = (time_finished - time_started) - (time_lunch_finished - time_lunch_started)
    #print(f"1st time diff: {time_difference}")
    morning_break = switch_morning_var.get()
    afternoon_break = switch_afternoon_var.get()
    #print(morning_break)
    #print(afternoon_break)
    if morning_break == "no":
        time_difference = time_difference + time_no_morning_break
    if afternoon_break == "no":
        time_difference = time_difference + time_no_afternoon_break
    #print(f"2nd time diff: {time_difference}")
    time_difference_str = str(time_difference)
    result = time_difference_str.split(":")
    result_hrs = result[0]
    result_min = result[1]
    #print(f"{result_hrs}h {result_min}m")
    entry_calculate_hrs.delete(0, 'end')
    entry_calculate_min.delete(0, 'end')
    entry_calculate_hrs.insert(index=0, string=result_hrs)
    entry_calculate_min.insert(index=0, string=result_min)

def link_to_website():
    webbrowser.open_new(r"https://lukasvegys.com/")

# ***** FONTS *****
# *****************
body_font = ctk.CTkFont(size=16, weight="normal")

container = ctk.CTkFrame(master=main_window, fg_color="transparent")
container.pack(expand=True)

container.rowconfigure(0)
container.rowconfigure(1)

container_frame_1 = ctk.CTkFrame(container, fg_color="transparent")
container_frame_1.grid(row=0, column=0, sticky="E", ipadx=50, pady=(15, 0))

frame_1_label = ctk.CTkButton(container_frame_1, fg_color="transparent", hover=False, text="", image=lv_logo, width=10, command=link_to_website)
frame_1_label.pack()

container_frame_2 = ctk.CTkFrame(container, fg_color="transparent")
container_frame_2.grid(row=1, column=0)

app = ctk.CTkFrame(master=container_frame_2, fg_color="transparent", border_width=1, border_color="#4c4c4c")
app.pack(pady=30, padx=30, expand=True)



# ***** COLUMN/GRID CONFIG *****
# ******************************

app.columnconfigure(0) # COLUMN 1
app.columnconfigure(1, minsize=70) # COLUMN 2
app.columnconfigure(2) # COLUMN 3
app.columnconfigure(3, minsize=70) # COLUMN 4

app.rowconfigure(0) # ROW 1
app.rowconfigure(1) # ROW 2
app.rowconfigure(2) # ROW 3
app.rowconfigure(3) # ROW 4
app.rowconfigure(4) # ROW 5
app.rowconfigure(5) # ROW 6
app.rowconfigure(6) # ROW 7
app.rowconfigure(7) # ROW 8



# ***** FRAMES *****
# ******************

# --- WORK START FRAME
frame_work_start_text = ctk.CTkFrame(app, fg_color="transparent")
frame_work_start_text.grid(row=0, column=0, pady=15)

frame_work_start_hrs = ctk.CTkFrame(app, fg_color="transparent")
frame_work_start_hrs.grid(row=0, column=1, ipadx=4, sticky="E", pady=15)

frame_work_start_colon = ctk.CTkFrame(app, fg_color="transparent")
frame_work_start_colon.grid(row=0, column=2, pady=15)

frame_work_start_min = ctk.CTkFrame(app, fg_color="transparent")
frame_work_start_min.grid(row=0, column=3, ipadx=4, sticky="W", pady=15)



# --- MORNING BREAK FRAME
frame_morning_break_text = ctk.CTkFrame(app, fg_color="transparent")
frame_morning_break_text.grid(row=1, column=0, pady=15)

frame_morning_break_toggle = ctk.CTkFrame(app, fg_color="transparent")
frame_morning_break_toggle.grid(row=1, column=1, columnspan=3, pady=15)

frame_morning_break_no = ctk.CTkFrame(app, fg_color="transparent")
frame_morning_break_no.grid(row=1, column=1, pady=15)

frame_morning_break_yes = ctk.CTkFrame(app, fg_color="transparent")
frame_morning_break_yes.grid(row=1, column=3, pady=15)



# --- LUNCH START FRAME
frame_lunch_start_text = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_start_text.grid(row=2, column=0, pady=5)

frame_lunch_start_hrs = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_start_hrs.grid(row=2, column=1, ipadx=4, sticky="E", pady=5)

frame_lunch_start_colon = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_start_colon.grid(row=2, column=2, sticky="NS", pady=5)

frame_lunch_start_min = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_start_min.grid(row=2, column=3, ipadx=4, sticky="W", pady=5)



# --- LUNCH END FRAME
frame_lunch_end_text = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_end_text.grid(row=3, column=0, pady=2)

frame_lunch_end_hrs = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_end_hrs.grid(row=3, column=1, ipadx=4, sticky="E", pady=2)

frame_lunch_end_colon = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_end_colon.grid(row=3, column=2, sticky="NSEW", pady=2)

frame_lunch_end_min = ctk.CTkFrame(app, fg_color="transparent")
frame_lunch_end_min.grid(row=3, column=3, ipadx=4, sticky="W", pady=2)



# --- AFTERNOON BREAK FRAME
frame_afternoon_break_text = ctk.CTkFrame(app, fg_color="transparent")
frame_afternoon_break_text.grid(row=4, column=0, pady=15)

frame_afternoon_break_toggle = ctk.CTkFrame(app, fg_color="transparent")
frame_afternoon_break_toggle.grid(row=4, column=1, columnspan=3, pady=15)

frame_afternoon_break_no = ctk.CTkFrame(app, fg_color="transparent")
frame_afternoon_break_no.grid(row=4, column=1, pady=15)

frame_afternoon_break_yes = ctk.CTkFrame(app, fg_color="transparent")
frame_afternoon_break_yes.grid(row=4, column=3, pady=15)



# --- WORK END FRAME
frame_work_end_text = ctk.CTkFrame(app, fg_color="transparent")
frame_work_end_text.grid(row=6, column=0, pady=5)

frame_work_end_hrs = ctk.CTkFrame(app, fg_color="transparent")
frame_work_end_hrs.grid(row=6, column=1, ipadx=4, sticky="E", pady=5)

frame_work_end_colon = ctk.CTkFrame(app, fg_color="transparent")
frame_work_end_colon.grid(row=6, column=2, sticky="NSEW", pady=5)

frame_work_end_min = ctk.CTkFrame(app, fg_color="transparent")
frame_work_end_min.grid(row=6, column=3, ipadx=4, sticky="W", pady=5)



# --- CALCULATE TOTAL FRAME
frame_calculate_btn = ctk.CTkFrame(app, fg_color="transparent")
frame_calculate_btn.grid(row=7, column=0, pady=15, padx=10)

frame_calculate_hrs = ctk.CTkFrame(app, fg_color="transparent")
frame_calculate_hrs.grid(row=7, column=1, ipadx=4, sticky="E", pady=15)

frame_calculate_colon = ctk.CTkFrame(app, fg_color="transparent")
frame_calculate_colon.grid(row=7, column=2, sticky="NSEW", pady=15)

frame_calculate_min = ctk.CTkFrame(app, fg_color="transparent")
frame_calculate_min.grid(row=7, column=3, ipadx=4, sticky="W", pady=15)




# ***** WIDGETS *****
# *******************

# --- WORK START WIDGETS
label_work_start_text = ctk.CTkLabel(frame_work_start_text, text="Started at", width=150, font=body_font)
label_work_start_text.pack()

calc_start_hrs = ""
entry_work_start_hrs = ctk.CTkEntry(frame_work_start_hrs, font=body_font, width=30)
entry_work_start_hrs.insert(index=0, string=calc_start_hrs)
entry_work_start_hrs.pack()

label_work_start_colon = ctk.CTkLabel(frame_work_start_colon, text=":", font=body_font, width=15)
label_work_start_colon.pack()

calc_start_min = ""
entry_work_start_min = ctk.CTkEntry(frame_work_start_min, font=body_font, width=30)
entry_work_start_min.insert(index=0, string=calc_start_min)
entry_work_start_min.pack()



# --- MORNING BREAK WIDGETS
label_morning_break_text = ctk.CTkLabel(frame_morning_break_text, text="Morning break?", width=150, font=body_font)
label_morning_break_text.pack()

label_morning_break_toggle = ctk.CTkSwitch(frame_morning_break_toggle, text="", progress_color="#e50065", width=5, command=switch_morning_event, variable=switch_morning_var, onvalue="yes", offvalue="no")
label_morning_break_toggle.pack()

label_morning_break_no = ctk.CTkLabel(frame_morning_break_no, text="N", font=body_font)
label_morning_break_no.pack()

label_morning_break_yes = ctk.CTkLabel(frame_morning_break_yes, text="Y", font=body_font)
label_morning_break_yes.pack()



# --- LUNCH START WIDGETS
label_lunch_start_text = ctk.CTkLabel(frame_lunch_start_text, text="Lunch from", width=150, font=body_font)
label_lunch_start_text.pack()

calc_lunch_start_hrs = ""
entry_lunch_start_hrs = ctk.CTkEntry(frame_lunch_start_hrs, font=body_font, width=30)
entry_lunch_start_hrs.insert(index=0, string=calc_lunch_start_hrs)
entry_lunch_start_hrs.pack()

label_lunch_start_colon = ctk.CTkLabel(frame_lunch_start_colon, text=":", font=body_font, width=15)
label_lunch_start_colon.pack()

calc_lunch_start_min = ""
entry_lunch_start_min = ctk.CTkEntry(frame_lunch_start_min, font=body_font, width=30)
entry_lunch_start_min.insert(index=0, string=calc_lunch_start_min)
entry_lunch_start_min.pack()



# --- LUNCH END WIDGETS
label_lunch_end_text = ctk.CTkLabel(frame_lunch_end_text, text="Lunch to", width=150, font=body_font)
label_lunch_end_text.pack()

calc_lunch_end_hrs = ""
entry_lunch_end_hrs = ctk.CTkEntry(frame_lunch_end_hrs, font=body_font, width=30)
entry_lunch_end_hrs.insert(index=0, string=calc_lunch_end_hrs)
entry_lunch_end_hrs.pack()

label_lunch_end_colon = ctk.CTkLabel(frame_lunch_end_colon, text=":", font=body_font, width=15)
label_lunch_end_colon.pack()

calc_lunch_end_min = ""
entry_lunch_end_min = ctk.CTkEntry(frame_lunch_end_min, font=body_font, width=30)
entry_lunch_end_min.insert(index=0, string=calc_lunch_end_min)
entry_lunch_end_min.pack()



# --- AFTERNOON BREAK WIDGETS
label_afternoon_break_text = ctk.CTkLabel(frame_afternoon_break_text, text="Afternoon break?", width=150, font=body_font)
label_afternoon_break_text.pack()

label_afternoon_break_toggle = ctk.CTkSwitch(frame_afternoon_break_toggle, text="", progress_color="#e50065", width=5, command=switch_afternoon_event, variable=switch_afternoon_var, onvalue="yes", offvalue="no")
label_afternoon_break_toggle.pack()

label_afternoon_break_no = ctk.CTkLabel(frame_afternoon_break_no, text="N", font=body_font)
label_afternoon_break_no.pack()

label_afternoon_break_yes = ctk.CTkLabel(frame_afternoon_break_yes, text="Y", font=body_font)
label_afternoon_break_yes.pack()



# --- WORK END WIDGETS
label_work_end_text = ctk.CTkLabel(frame_work_end_text, text="Finished at", width=150, font=body_font)
label_work_end_text.pack()

calc_end_hrs = ""
entry_work_end_hrs = ctk.CTkEntry(frame_work_end_hrs, font=body_font, width=30)
entry_work_end_hrs.insert(index=0, string=calc_end_hrs)
entry_work_end_hrs.pack()

label_work_end_colon = ctk.CTkLabel(frame_work_end_colon, text=":", font=body_font, width=15)
label_work_end_colon.pack()

calc_end_min = ""
entry_work_end_min = ctk.CTkEntry(frame_work_end_min, font=body_font, width=30)
entry_work_end_min.insert(index=0, string=calc_end_min)
entry_work_end_min.pack()



# --- CALCULATE TOTAL WIDGETS
btn_calculate = ctk.CTkButton(frame_calculate_btn, text="Calculate", width=150, font=body_font, command=total_time_calc, fg_color="#e50065", hover_color="#d10059")
btn_calculate.pack()

calc_result_hrs = ""
entry_calculate_hrs = ctk.CTkEntry(frame_calculate_hrs, font=body_font, width=30)
entry_calculate_hrs.insert(index=0, string=calc_result_hrs)
entry_calculate_hrs.pack()

label_calculate_colon = ctk.CTkLabel(frame_calculate_colon, text=":", font=body_font, width=15)
label_calculate_colon.pack()

calc_result_min = ""
entry_calculate_min = ctk.CTkEntry(frame_calculate_min, font=body_font, width=30)
entry_calculate_min.insert(index=0, string=calc_result_min)
entry_calculate_min.pack()



# MAGIC TO MAKE IT FUNCTION
main_window.mainloop()

# placeholder_text="00", placeholder_text_color="#8d8d8d"