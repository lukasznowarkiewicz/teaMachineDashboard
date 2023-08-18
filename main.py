import customtkinter
import os
from PIL import Image

class LoadingWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("loading")
        self.geometry("1024x600")
        customtkinter.set_appearance_mode("Dark")
        self.attributes('-fullscreen', True)
        self.label = customtkinter.CTkLabel(self, text="Loading")
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("teaMachineDashboard.py")
        self.geometry("1024x600")
        self.bind("<Escape>", self.toggle_fullscreen)
        customtkinter.set_appearance_mode("Dark")
        
        # loading = LoadingWindow()
        # loading.after(5000, loading.destroy)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.blackTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "BlackTea.png")), size=(120, 120))
        self.BlackTeaWithLemonImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "BlackTeaWithLemon.png")), size=(120, 120))
        self.ChamomoileTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ChamomoileTea.png")), size=(120, 120))
        self.CherryTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CherryTea.png")), size=(120, 120))
        self.FruitsTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "FruitsTea.png")), size=(120, 120))
        self.GreenTeaWithOrangeImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "GreenTeaWithOrange.png")), size=(120, 120))
        self.MatchaTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "MatchaTea.png")), size=(120, 120))
        self.RaspberryTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "RaspberryTea.png")), size=(120, 120))
        self.StrawberryTeaImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "StrawberryTea.png")), size=(120, 120))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame on the left
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(9, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Tea machine", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Tea choice",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        self.home_button_description = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=10, text="Tea description",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_description_event, font=customtkinter.CTkFont(size=12))
        self.home_button_description.grid(row=2, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Water base",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Brewing",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=4, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sweetness",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=5, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Solid additives",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=6, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=0, text="Liquid Additives",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=7, column=0, sticky="ew")

        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Done",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=8, column=0, sticky="ew")

        self.frame_8_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_8_button_event)
        self.frame_8_button.grid(row=9, column=0, sticky="esw")



        # create home frame on the right - main window
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, sticky="nesw")
        self.home_frame.columnconfigure(5, weight=1)
        self.home_frame.rowconfigure(1, weight=1)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Black Tea", image=self.blackTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_1.grid(row=0, column=0, padx=0, pady=0)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Black Tea with lemon", image=self.BlackTeaWithLemonImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_2.grid(row=1, column=0, padx=0, pady=0)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Chamomoile Tea", image=self.ChamomoileTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_3.grid(row=0, column=1, padx=0, pady=0)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Cherry Tea", image=self.CherryTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_4.grid(row=1, column=1, padx=0, pady=0)
        self.home_frame_button_5 = customtkinter.CTkButton(self.home_frame, text="Fruits Tea", image=self.FruitsTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_5.grid(row=0, column=2, padx=0, pady=0)
        self.home_frame_button_6 = customtkinter.CTkButton(self.home_frame, text="Green Tea with orange", image=self.GreenTeaWithOrangeImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_6.grid(row=1, column=2, padx=0, pady=0)
        self.home_frame_button_7 = customtkinter.CTkButton(self.home_frame, text="Matcha Tea", image=self.MatchaTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_7.grid(row=0, column=3, padx=0, pady=0)
        self.home_frame_button_8 = customtkinter.CTkButton(self.home_frame, text="Raspberry Tea", image=self.RaspberryTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_8.grid(row=1, column=3, padx=0, pady=0)
        self.home_frame_button_9 = customtkinter.CTkButton(self.home_frame, text="Strawberry Tea", image=self.StrawberryTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_9.grid(row=0, column=4, padx=0, pady=0)
        self.home_frame_button_10 = customtkinter.CTkButton(self.home_frame, text="Herbata+", image=self.blackTeaImage, compound="top", font=("arial", 18), border_spacing=10)
        self.home_frame_button_10.grid(row=1, column=4, padx=0, pady=0)


         # create description_tea frame on the right - main window

        self.description_tea = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.description_tea.grid(row=0, column=0, sticky="nesw")
        #self.description_tea.columnconfigure(5, weight=1)
        #self.description_tea.rowconfigure(2, weight=1)

        self.description_tea_Dec1 = customtkinter.CTkButton(self.description_tea, text="Black Tea - Simple tea Bla bla bla", compound="top", font=("arial", 18), border_spacing=10)
        self.description_tea_Dec1.grid(row=0, column=0, padx=30, pady=20)


        teaList = {"blackTea", "cherryTea", "greenTea"}

        for tea in teaList:
            # self.home
            pass

        # frame frame "Water base"
        self.waterBase_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Brewing"
        self.brewing_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Sweetness"
        self.sweetness_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Solid Additives"
        self.solidAdditives_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Liquid Additives"
        self.liquidAdditives_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Done"
        self.done_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Settings"
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create frame "Manual Control"
        self.manualControl_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.home_button_description.configure(fg_color=("gray75", "gray25") if name == "description_tea" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")
        self.frame_8_button.configure(fg_color=("gray75", "gray25") if name == "frame_8" else "transparent")


        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "description_tea":
            self.description_tea.grid(row=0, column=1, sticky="nsew")
        else:
            self.description_tea.grid_forget()
        if name == "frame_2":
            self.waterBase_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.waterBase_frame.grid_forget()
        if name == "frame_3":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        if name == "frame_4":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        if name == "frame_5":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        if name == "frame_6":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        if name == "frame_7":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        if name == "frame_8":
            self.brewing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.brewing_frame.grid_forget()
        

    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not is_fullscreen)


    def home_button_event(self):
        self.select_frame_by_name("home")

    def home_button_description_event(self):
        self.select_frame_by_name("description_tea")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")  

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")    

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")  

    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")   

    def frame_8_button_event(self):
        self.select_frame_by_name("frame_8")


if __name__ == "__main__":
    app = App()
    app.mainloop()

