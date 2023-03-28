from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import ImageTk, Image
import subprocess
import os


def download_model():

    yolo_msg = ""
    if not os.path.exists("yolov7"):
        subprocess.Popen("wget https://github.com/WongKinYiu/yolov7")
        yolo_msg += "YOLOv7 model is Installed!"
    else:
        yolo_msg += "YOLOv7 model is already exist!"
        pass

    req1 = "requirements.txt"
    req2 = "requirements_gpu.txt"

    pip_msg = ""
    if req1 and req2 not in os.listdir('./yolov7'):
        subprocess.Popen("pip install -r ./yolov7/requirements.txt")
        subprocess.Popen("pip install -r ./yolov7/requirements_gpu.txt")
        pip_msg += "Dependencies are successfully installed!"
    else:
        pip_msg += "Dependencies are already exist!"
        pass

    return yolo_msg, pip_msg


def test_model(source):
    if source.isnumeric():
        process = subprocess.Popen('python ./yolov7/detect.py --weights ./best_old.pt --source {} --img-size 640 --no-trace'.format(
            eval(source)), shell=True, stdout=subprocess.PIPE)
    else:
        path = source.replace('\\', '/')
        process = subprocess.Popen('python ./yolov7/detect.py --weights ./best_old.pt --source {} --img-size 640 --no-trace'.format(path), shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')


class Intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Road Damage Detector")
        self.width = 764
        self.height = 520
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth -
                                                              self.width) / 2, (screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#b7eba9')

        '''Logo Label Button'''
        logo_img = ImageTk.PhotoImage(Image.open(
            'H:/BIT STUDY/8th Semester/thesis project/stop.png'))
        logo_label = tk.Label(self.root, image=logo_img)
        logo_label.image = logo_img  # keep a reference to prevent garbage collection
        logo_label.place(x=150, y=40, width=50, height=53)

        '''Welcome title'''
        welcomeTitle = tk.Message(self.root)
        welcomeTitle["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=16)
        welcomeTitle["font"] = ft
        welcomeTitle["fg"] = "#3656b7"
        welcomeTitle["bg"] = "#b7eba9"
        welcomeTitle["justify"] = "center"
        welcomeTitle["text"] = "Welcome\n to \nRoad Damage Detector"
        welcomeTitle.place(x=250, y=40, width=260, height=88)

        '''Team Label'''
        teamLabel = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=14)
        teamLabel["font"] = ft
        teamLabel["fg"] = "#333333"
        teamLabel["bg"] = "#b7eba9"
        teamLabel["justify"] = "left"
        teamLabel["text"] = "Developed by Team71"
        teamLabel.place(x=255, y=170, width=247, height=55)

        '''Author Label'''
        first_author = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        first_author["font"] = ft
        first_author["fg"] = "#333333"
        first_author["bg"] = "#b7eba9"
        first_author["justify"] = "left"
        first_author["text"] = "(1) MUSTAKIM MD MIZANUR RAHMAN\n   School of Computer Science & Technology"
        first_author.place(x=130, y=220, width=247, height=55)

        co = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        co["font"] = ft
        co["fg"] = "#333333"
        co["bg"] = "#b7eba9"
        co["justify"] = "center"
        co["text"] = "(2) AHAMED MUSTAK \n  School of Automation"
        co.place(x=500, y=220, width=136, height=55)

        '''Instruction label'''
        inst_button = tk.Button(self.root)
        inst_button["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=10)
        inst_button["font"] = ft
        inst_button["fg"] = "#000000"
        inst_button["justify"] = "center"
        inst_button["text"] = "Install"
        inst_button.place(x=650, y=335, width=75, height=30)
        inst_button["command"] = self.inst_button_command

        '''Install Dependencies'''
        install_button = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        install_button["font"] = ft
        install_button["fg"] = "#333333"
        install_button["bg"] = "#e7d8d8"
        install_button["justify"] = "center"
        install_button["text"] = "Install the dependency files.\n(Check the readme.txt file. If the requirements meet your system, no need to install the dependencies."
        install_button.place(x=90, y=330, width=550, height=38)

        '''Msg Box'''
        self.msg = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        self.msg["font"] = ft
        self.msg["fg"] = "#333333"
        self.msg["justify"] = "left"
        self.msg["text"] = ""
        self.msg.place(x=90, y=390, width=400, height=100)

        '''Next Button'''
        next_button = tk.Button(self.root)
        next_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        next_button["font"] = ft
        next_button["fg"] = "#000000"
        next_button["justify"] = "center"
        next_button["text"] = "Next"
        next_button.place(x=582, y=480, width=70, height=25)
        next_button["command"] = self.next_button_command

        '''Quit Button'''
        quit_button = tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=657, y=480, width=70, height=25)
        quit_button["command"] = self.quit_button_command

    def inst_button_command(self):
        a, b = download_model()
        self.msg.config(text='>>'+a+'\n>>'+b)

    def next_button_command(self):
        self.root.destroy()
        root2 = tk.Tk()
        app1 = App(root2)
        root2.mainloop()
        # print("command")

    def quit_button_command(self):
        self.root.destroy()


class App:
    def __init__(self, root):
        self.root = root
        # setting title
        self.root.title("Road Damage Detector")
        # setting window size
        self.width = 764
        self.height = 520
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth -
                                                              self.width) / 2, (screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#b7eba9')

        '''Logo Label Button'''
        logo_img = ImageTk.PhotoImage(Image.open(
            'H:/BIT STUDY/8th Semester/thesis project/stop.png'))
        logo_label = tk.Label(self.root, image=logo_img)
        logo_label.image = logo_img  # keep a reference to prevent garbage collection
        logo_label.place(x=150, y=40, width=50, height=53)

        '''Welcome title'''
        welcomeTitle = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=16)
        welcomeTitle["font"] = ft
        welcomeTitle["fg"] = "#3656b7"
        welcomeTitle["bg"] = "#b7eba9"
        welcomeTitle["justify"] = "center"
        welcomeTitle["text"] = "Road Damage Detector"
        welcomeTitle.place(x=230, y=30, width=300, height=88)

        '''Another Instruction Label'''
        inst2_label = tk.Label(self.root)
        inst2_label["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=14)
        inst2_label["font"] = ft
        inst2_label["fg"] = "#333333"
        inst2_label["justify"] = "left"
        inst2_label["text"] = "Choose your processing method"
        inst2_label.place(x=250, y=150, width=270, height=45)

        '''Select Label'''
        select_label = tk.Label(self.root)
        select_label["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=14)
        select_label["font"] = ft
        select_label["fg"] = "#333333"
        select_label["justify"] = "left"
        select_label["text"] = "Select :"
        select_label.place(x=100, y=198, width=60, height=30)

        '''Test Button'''
        test_button = tk.Button(self.root)
        test_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        test_button["font"] = ft
        test_button["fg"] = "#000000"
        test_button["justify"] = "center"
        test_button["text"] = "Test"
        test_button.place(x=582, y=480, width=70, height=25)
        test_button["command"] = self.test_button_command

        '''Quit Button'''
        quit_button = tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=657, y=480, width=70, height=25)
        quit_button["command"] = self.quit_button_command

        '''Back Button'''
        back_button = tk.Button(self.root)
        back_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        back_button["font"] = ft
        back_button["fg"] = "#000000"
        back_button["justify"] = "center"
        back_button["text"] = "Back"
        back_button.place(x=505, y=480, width=70, height=25)
        back_button["command"] = self.back_button_command

        '''Check Box. 
        webcam1, 
        webcam2,
        Video, 
        Image'''

        self.webcam1_checked = tk.BooleanVar()
        self.webcam2_checked = tk.BooleanVar()
        self.video_checked = tk.BooleanVar()
        self.image_checked = tk.BooleanVar()

        webcam1_check = tk.Checkbutton(
            self.root, variable=self.webcam1_checked, command=self.on_checkbox_clicked)
        webcam1_check["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=12)
        webcam1_check["font"] = ft
        webcam1_check["fg"] = "#333333"
        webcam1_check["justify"] = "center"
        webcam1_check["text"] = "Webcam1"
        webcam1_check.place(x=200, y=200, width=85, height=25)
        webcam1_check["offvalue"] = "0"
        webcam1_check["onvalue"] = "1"
        webcam1_check["command"] = self.on_checkbox_clicked

        webcam2_check = tk.Checkbutton(
            self.root, variable=self.webcam2_checked, command=self.on_checkbox_clicked)
        webcam2_check["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=12)
        webcam2_check["font"] = ft
        webcam2_check["fg"] = "#333333"
        webcam2_check["justify"] = "center"
        webcam2_check["text"] = "Webcam2"
        webcam2_check.place(x=330, y=200, width=85, height=25)
        webcam2_check["offvalue"] = "0"
        webcam2_check["onvalue"] = "1"
        webcam2_check["command"] = self.on_checkbox_clicked

        video_check = tk.Checkbutton(
            self.root, variable=self.video_checked, command=self.on_checkbox_clicked)
        video_check["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=12)
        video_check["font"] = ft
        video_check["fg"] = "#333333"
        video_check["justify"] = "center"
        video_check["text"] = "Video"
        video_check.place(x=455, y=200, width=70, height=25)
        video_check["offvalue"] = "0"
        video_check["onvalue"] = "1"
        video_check["command"] = self.on_checkbox_clicked

        image_check = tk.Checkbutton(
            self.root, variable=self.image_checked, command=self.on_checkbox_clicked)
        image_check["bg"] = "#b7eba9"
        ft = tkFont.Font(family='Times', size=12)
        image_check["font"] = ft
        image_check["fg"] = "#333333"
        image_check["justify"] = "center"
        image_check["text"] = "Image"
        image_check.place(x=575, y=200, width=70, height=25)
        image_check["offvalue"] = "0"
        image_check["onvalue"] = "1"
        image_check["command"] = self.on_checkbox_clicked

    def back_button_command(self):
        self.root.destroy()
        root1 = tk.Tk()
        app1 = Intro(root1)
        root1.mainloop()

    def test_button_command(self):
        resultLabel = tk.Label(self.root)
        resultLabel["anchor"] = "n"
        ft = tkFont.Font(family='Times', size=8)
        resultLabel["font"] = ft
        resultLabel["fg"] = "#333333"
        resultLabel["justify"] = "left"
        resultLabel.place(x=130, y=310, width=480, height=90)

        if self.webcam1_checked.get():
            path = str(0)
            output = test_model(path)
            resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]
        elif self.webcam2_checked.get():
            path = str(1)
            output = test_model(path)
            resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]
        else:
            path = self.file_path()
            output = test_model(path)
            resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]

    def quit_button_command(self):
        self.root.destroy()

    def file_browse(self, condition):
        if condition:
            # save the reference to the widget as an instance attribute
            self.browseLabel = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.browseLabel["font"] = ft
            self.browseLabel["fg"] = "#ae9696"
            self.browseLabel["justify"] = "center"
            self.browseLabel["text"] = "Select your file"
            self.browseLabel.place(x=130, y=260, width=480, height=30)

            # save the reference to the widget as an instance attribute
            self.browseButton = tk.Button(self.root)
            self.browseButton["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.browseButton["font"] = ft
            self.browseButton["fg"] = "#000000"
            self.browseButton["justify"] = "center"
            self.browseButton["text"] = "Browse"
            self.browseButton.place(x=620, y=260, width=52, height=30)
        else:
            # check if the widget has been created before attempting to destroy it
            if hasattr(self, 'browseLabel'):
                self.browseLabel.destroy()
                del self.browseLabel  # remove the instance attribute reference
            if hasattr(self, 'browseButton'):
                self.browseButton.destroy()
                del self.browseButton

    def on_checkbox_clicked(self):
        if self.webcam1_checked.get():
            self.webcam2_checked.set(False)
            self.video_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(False)

        elif self.webcam2_checked.get():
            self.webcam1_checked.set(False)
            self.video_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(False)

        elif self.video_checked.get():
            self.webcam1_checked.set(False)
            self.webcam2_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(self.video_checked.get())
            self.browseButton["command"] = self.browseButton_command_video

        elif self.image_checked.get():
            self.webcam1_checked.set(False)
            self.webcam2_checked.set(False)
            self.video_checked.set(False)
            self.file_browse(self.image_checked.get())
            self.browseButton["command"] = self.browseButton_command_photo
        else:
            self.file_browse(False)

        if not self.webcam1_checked.get() and not self.webcam2_checked.get() and not self.video_checked.get() and not self.image_checked.get():
            self.file_browse(False)

    def browseButton_command_video(self):
        # For all file type use ("all files", "*.*") in the filetypes tuple
        self.filepath = filedialog.askopenfilename(
            title="Open file", filetypes=(("video files", "*.mp4"), ("all files", "*.*")))

        if self.filepath != "":
            self.browseLabel.config(text=self.filepath)

    def browseButton_command_photo(self):
        # For all file type use ("all files", "*.*") in the filetypes tuple
        self.filepath = filedialog.askopenfilename(
            title="Open file", filetypes=(("Image files", "*.jpg"), ("all files", "*.*")))

        if self.filepath != "":
            self.browseLabel.config(text=self.filepath)

    def file_path(self):
        return self.filepath


if __name__ == "__main__":
    root1 = tk.Tk()
    app1 = Intro(root1)
    root1.mainloop()
