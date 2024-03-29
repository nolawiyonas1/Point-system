import math  # importing the math module to use its functions
import tkinter as tk  # importing the tkinter module to create a GUI for this program

window = tk.Tk()
window.geometry('775x450')  # setting window size 775 x 450 pixels
window.title("Point system")  # title of the window

###### Question 1 ######
# creating a frame for the first question
question1_frame = tk.Frame(window)
question1_frame.grid(row=1, column=1)

# creating a frame for the above button
above_button_frame = tk.Frame(window)
above_button_frame.grid(row=1, column=1)

###### Question 2 ######
# creating a frame for the second question
question2_frame = tk.Frame(window)
question2_frame.grid(row=1, column=1)

###### Question 3 ######
# creating a frame for the third question
question3_frame = tk.Frame(window)
question3_frame.grid(row=1, column=1)

# creating a frame for the no button
question3_nobutton_frame = tk.Frame(window)
question3_nobutton_frame.grid(row=1, column=1)

###### Question 4 ######
# creating a frame for the fourth question
question4_frame = tk.Frame(window)
question4_frame.grid(row=1, column=1)

# creating a frame for the above_70k button
above_70k_frame = tk.Frame(window)
above_70k_frame.grid(row=1, column=1)

###### Question 5 ######
# creating a frame for the fifth question
question5_frame = tk.Frame(window)
question5_frame.grid(row=1, column=1)

###### Question 6 ######
# creating a frame for the sixth question
question6_frame = tk.Frame(window)
question6_frame.grid(row=1, column=1)

###### Question 7 ######
# creating a frame for the seventh question
question7_frame = tk.Frame(window)
question7_frame.grid(row=1, column=1)

###### Question 8 ######
# creating a frame for the eighth question
question8_frame = tk.Frame(window)
question8_frame.grid(row=1, column=1)

# creating a frame to display final points
final_points_frame = tk.Frame(window)
final_points_frame.grid(row=1, column=1)
final_msg_frame = tk.Frame(window)
final_msg_frame.grid(row=3, column=1)

# Functions

def add_points(
        point):  # this function adds points to the current_score variable
    # creating the point counter
    global current_score
    try:
        current_score
    except NameError:
        current_score = 0
    current_score += point


###### Question 1 ######


def question1():  # this function will be called if the start button is clicked
    # destroying the welcome page
    welcome_msg1.destroy()
    welcome_msg2.destroy()
    welcome_label.destroy()
    start_button.destroy()

    def above_button(
    ):  # this function will be called if teh above button is clicked
        # destroying the question 1 frame
        question1_frame.destroy()

        # Above button question
        above_question = tk.Label(
            above_button_frame,
            text=
            "Are you in a program that spans for more than 4 years or a Master's?",
            font=("Arial Bold", 13),
            fg="blue")

        # above_question choices
        above_yes = tk.Button(
            above_button_frame,
            text="Yes",
            padx=113,
            pady=27,
            command=lambda: [add_points(1), question2()]
        )  # lambda is used to call two functions at once, add_points() is used to add points, and question2() will go to the next question
        above_no = tk.Button(
            above_button_frame,
            text="No",
            padx=113,
            pady=27,
            command=lambda: [add_points(0), question2()])

        # above_question positioning
        above_question.grid(row=0, column=1, columnspan=2)

        above_yes.grid(row=1, column=1)
        above_no.grid(row=1, column=2)

    # Question 1
    question_1 = tk.Label(question1_frame,
                          text="Question 1: What is your upcoming class year?",
                          font=("Arial Bold", 15),
                          fg="blue")

    # Question 1 Choices
    first_year = tk.Button(
        question1_frame,
        text="1st year",
        padx=113,
        pady=27,
        command=lambda: [add_points(4), question2()])
    second_year = tk.Button(
        question1_frame,
        text="2nd year",
        padx=113,
        pady=27,
        command=lambda: [add_points(3), question2()])
    third_year = tk.Button(
        question1_frame,
        text="3rd year",
        padx=113,
        pady=27,
        command=lambda: [add_points(2), question2()])
    fourth_year = tk.Button(
        question1_frame,
        text="4th year",
        padx=113,
        pady=27,
        command=lambda: [add_points(1), question2()])
    above_button = tk.Button(question1_frame,
                             text="Above",
                             padx=113,
                             pady=27,
                             command=above_button)

    # Question 1 positioning
    question_1.grid(row=0, column=1, columnspan=2)

    first_year.grid(row=1, column=1)
    second_year.grid(row=1, column=2)
    third_year.grid(row=2, column=1)
    fourth_year.grid(row=2, column=2)
    above_button.grid(row=3, column=1, columnspan=2)


###### Question 2 ######


def question2(
):  # this function will be called if the user completes the first question
    # destroying the question 1 and above button frame
    question1_frame.destroy()
    above_button_frame.destroy()

    # Question 2
    question_2 = tk.Label(question2_frame,
                          text="Question 2: How old are you?",
                          font=("Arial Bold", 15),
                          fg="blue")

    # Question 2 Choices
    seventeen_twentytwo = tk.Button(
        question2_frame,
        text="17-22",
        padx=113,
        pady=27,
        command=lambda: [add_points(2), question3()])
    above_twentythree = tk.Button(
        question2_frame,
        text="23+",
        padx=113,
        pady=27,
        command=lambda: [add_points(1), question3()])

    # Question 2 positioning
    question_2.grid(row=0, column=1, columnspan=2)

    seventeen_twentytwo.grid(row=1, column=1)
    above_twentythree.grid(row=1, column=2)


###### Question 3 ######


def question3(
):  # this function will be called if the user completes the second question
    # destroying the question 2 frame
    question2_frame.destroy()

    def question3_no_button(
    ):  # this function will be called if the user clicks on 'No' for question 3
        # destroying the question 3 frame
        question3_frame.destroy()

        # Question if 'No' button is clicked
        question3_nobutton = tk.Label(
            question3_nobutton_frame,
            text="Do you live outside the GTA (Greater Toronto Area)?",
            font=("Arial Bold", 13),
            fg="blue")

        # question3_nobutton_question choices
        question3_nobutton_yes = tk.Button(
            question3_nobutton_frame,
            text="Yes",
            padx=113,
            pady=27,
            command=lambda: [add_points(4), question4()])
        question3_nobutton_no = tk.Button(
            question3_nobutton_frame,
            text="No",
            padx=113,
            pady=27,
            command=lambda: [add_points(0), question4()])

        # above_question positioning
        question3_nobutton.grid(row=0, column=1, columnspan=2)

        question3_nobutton_yes.grid(row=1, column=1)
        question3_nobutton_no.grid(row=1, column=2)

    # Question 3
    question_3 = tk.Label(
        question3_frame,
        text=
        "Question 3: Are you an international student or live outside of Ontario?",
        font=("Arial Bold", 13),
        fg="blue")

    # Question 3 Choices
    question3_yes = tk.Button(
        question3_frame,
        text="Yes",
        padx=113,
        pady=27,
        command=lambda: [add_points(6), question4()])
    question3_no = tk.Button(question3_frame,
                             text="No",
                             padx=113,
                             pady=27,
                             command=question3_no_button)

    # Question 3 positioning
    question_3.grid(row=0, column=1, columnspan=2)

    question3_yes.grid(row=1, column=1)
    question3_no.grid(row=1, column=2)


###### Question 4 ######


def question4(
):  # this function will be called if the user completes the third question
    # destroying the question 3 and question 3 no button frame
    question3_frame.destroy()
    question3_nobutton_frame.destroy()

    def above_70k_button():
        # destroying the question 4 frame
        question4_frame.destroy()

        # this variable is used to direct the user
        directing_user = tk.Label(
            above_70k_frame,
            text=
            "Answer the question on the console below. \nPlease press enter once finished.",
            font=("Arial Bold", 15))

        # positioning
        directing_user.grid(row=1, column=1)

        income_points_calculated = 69999  # income points not yet calculated, so set to false
        while income_points_calculated < 70000:  # While the above is false, keep running until it is true
            try:
                # creating the area for the user to write their exact income
                exact_income = int(
                    input(
                        "What is your exact income? It must be over $70000!\n "
                    ))
                point_deducted = math.floor(float(
                    -exact_income / 200000))  # round the number down
                if point_deducted < -4:  # maximum points the program can deduct is 4
                    point_deducted = -4
                income_points_calculated = exact_income  # income points now calculated, so set to true
            except:
                print("Enter an integer over 70000!")

        to_question5 = tk.Button(
            above_70k_frame,
            text="Click this to proceed to question 5.",
            padx=110,
            pady=20,
            height=3,
            width=3,
            command=lambda: [add_points(point_deducted),
                             question5()])

        # positioning
        to_question5.grid(row=2, column=1)

    # Question 4
    question_4 = tk.Label(question4_frame,
                          text="Question 4: What is your gross family income?",
                          font=("Arial Bold", 15),
                          fg="blue")

    # Question 4 Choices
    below_70k = tk.Button(
        question4_frame,
        text="$70,000 & Below",
        padx=113,
        pady=27,
        command=lambda: [add_points(3), question5()])
    above_70k = tk.Button(
        question4_frame,
        text="Above $70,000",
        padx=113,
        pady=27,
        command=lambda: [add_points(0), above_70k_button()])

    # Question 4 positioning
    question_4.grid(row=0, column=1, columnspan=2)

    below_70k.grid(row=1, column=1)
    above_70k.grid(row=1, column=2)


###### Question 5 ######


def question5(
):  # this function will be called if the user completes the fourth question
    # destroying the question 4 frames
    question4_frame.destroy()
    above_70k_frame.destroy()

    # Question 5
    question_5 = tk.Label(
        question5_frame,
        text="Question 5: Are you First Nations, Mètis, Inuit, etc.?",
        font=("Arial Bold", 15),
        fg="blue")

    # Question 5 Choices
    question5_yes = tk.Button(
        question5_frame,
        text="Yes",
        padx=113,
        pady=27,
        command=lambda: [add_points(2), question6()])
    question5_no = tk.Button(
        question5_frame,
        text="No",
        padx=113,
        pady=27,
        command=lambda: [add_points(2), question6()])

    # Question 5 positioning
    question_5.grid(row=0, column=1, columnspan=2)

    question5_yes.grid(row=1, column=1)
    question5_no.grid(row=1, column=2)


###### Question 6 ######


def question6(
):  # this function will be called if the user completes the fifth question
    # destroying the question 5 frame
    question5_frame.destroy()

    # Question 6
    question_6 = tk.Label(
        question6_frame,
        text=
        "Question 6: Are you clinically diagnosed with any chronic \nphysical disabilities?",
        font=("Arial Bold", 15),
        fg="blue")

    # Question 6 Choices
    question6_yes = tk.Button(
        question6_frame,
        text="Yes",
        padx=113,
        pady=27,
        command=lambda: [add_points(4), question7()])
    question6_no = tk.Button(
        question6_frame,
        text="No",
        padx=113,
        pady=27,
        command=lambda: [add_points(0), question7()])

    # Question 6 positioning
    question_6.grid(row=0, column=1, columnspan=2)

    question6_yes.grid(row=1, column=1)
    question6_no.grid(row=1, column=2)


###### Question 7 ######


def question7(
):  # this function will be called if the user completes the sixth question
    # destroying the question 6 frame
    question6_frame.destroy()

    # Question 7
    question_7 = tk.Label(
        question7_frame,
        text=
        "Question 7: Are you clinically diagnosed with any chronic \nmental health problems?",
        font=("Arial Bold", 15),
        fg="blue")

    # Question 7 Choices
    question7_yes = tk.Button(
        question7_frame,
        text="Yes",
        padx=113,
        pady=27,
        command=lambda: [add_points(3), question8()])
    question7_no = tk.Button(
        question7_frame,
        text="No",
        padx=113,
        pady=27,
        command=lambda: [add_points(0), question8()])

    # Question 7 positioning
    question_7.grid(row=0, column=1, columnspan=2)

    question7_yes.grid(row=1, column=1)
    question7_no.grid(row=1, column=2)


###### Question 8 ######


def question8(
):  # this function will be called if the user completes the seventh question
    # destroying the question 7 frame
    question7_frame.destroy()

    # Question 8
    question_8 = tk.Label(
        question8_frame,
        text="Question 8: Are you on academic probation or suspension?",
        font=("Arial Bold", 15),
        fg="red")

    # Question 8 Choices
    question8_yes = tk.Button(
        question8_frame,
        text="Yes",
        padx=113,
        pady=27,
        command=lambda: [add_points(-3),
                         display_final_points()])
    question8_no = tk.Button(
        question8_frame,
        text="No",
        padx=113,
        pady=27,
        command=lambda: [add_points(0), display_final_points()])

    # Question 8 positioning
    question_8.grid(row=0, column=1, columnspan=2)

    question8_yes.grid(row=1, column=1)
    question8_no.grid(row=1, column=2)


def display_final_points(
):  # this function will display the final points of the user
    # destroying the question 8 frame
    question8_frame.destroy()
    final_points = tk.Label(final_points_frame,
                            text="Your final points are " + str(current_score),
                            font=("Arial Bold", 18),
                            fg="blue")
    final_msg = tk.Label(
        final_msg_frame,
        text=
        "Thank you for using the University of Mary Ward's \nHousing Score Algorithm. \nWe hope to see you next year!",
        font=("Arial Bold", 13))
    final_msg.grid(row=2, column=1)
    final_points.grid(row=1, column=1)


##### Welcome page and start Button #####
welcome_msg1 = tk.Label(
    window,
    text="Welcome to Toronto's University of Mary Ward's point system.",
    font=("Arial Bold", 12))
welcome_msg2 = tk.Label(window,
                        text="Click the button below to start the program.",
                        font=("Arial Bold", 12),
                        fg="blue")
start_button = tk.Button(window,
                         text="START",
                         font=("Symbol", 15),
                         height=2,
                         width=10,
                         command=question1)

#placing university logo in welcome screen
img = tk.PhotoImage(file="university_picture.png")
welcome_img = img.subsample(5)
welcome_label = tk.Label(window, image=welcome_img)
welcome_label.grid(row=5, column=1)

# positioning
welcome_msg1.grid(row=1, column=1, padx=50, pady=10)
welcome_msg2.grid(row=2, column=1, padx=30, pady=10)
start_button.grid(row=3, column=1, padx=250, pady=10, sticky="s")

window.mainloop(
)  # This function calls the endless loop of the window, so the window will wait for any user interaction till we close it.
