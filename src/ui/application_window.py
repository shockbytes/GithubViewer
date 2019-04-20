from tkinter import *
from src.utils.utils import load_image_from_url

import tkinter as tk


class ApplicationWindow(Frame):

    def __create_widgets(self, col_width):

        # Image URL
        img = load_image_from_url(self.__view_model.user_image_url, 128, 128)
        self.user_image = tk.Label(self, image=img, width=col_width)
        self.user_image.image = img
        self.user_image.grid(column=0)

        # Username
        self.user_name_label = tk.Label(
            self,
            text=self.__view_model.user_name,
            font='helvetica 20',
            pady=12
        )
        self.user_name_label.grid(column=0)

        # Company
        self.user_company_label = tk.Label(self, text=self.__view_model.user_company, font='helvetica 15', pady=6)
        self.user_company_label.grid(column=0)

        # List of repositories
        self.__view_model.get_repositories_async()\
            .subscribe_(
                on_next=lambda repos: self.__setup_repository_list(repos),
                on_error=lambda error: print(error),
                on_completed=lambda: "Loading repositories completed"
            )

        # Repository content
        self.var_selected_repo = StringVar(self, value="")
        self.selected_repo_label = tk.Label(
            self,
            textvariable=self.var_selected_repo,
            font='helvetica 25 bold',
            width=25
        )
        self.selected_repo_label.grid(column=1, row=0)

    def __setup_repository_list(self, repos):

        # Setup header label
        self.repository_list_label = tk.Label(self, text='Repositories', font='helvetica 12', pady=12)
        self.repository_list_label.grid()

        self.repository_list = tk.Listbox(self)

        for r in repos:
            self.repository_list.insert(END, r.name)

        self.repository_list.bind("<<ListboxSelect>>", self.__on_list_item_select)

        self.repository_list.grid(column=0)

    def __on_list_item_select(self, event):
        idx = event.widget.curselection()[0]
        repo_name = self.repository_list.get(idx)

        self.var_selected_repo.set(repo_name)

    def __show_app_icon(self):
        self.root.iconbitmap('data/icons/github_icon.jpg')

    def __init__(self, master, application_view_model, geometry, column_width):
        self.__view_model = application_view_model
        Frame.__init__(self, master, pady=42)
        self.pack()

        self.root = master
        self.root.resizable(False, False)
        self.root.wm_title("Github Viewer v0.1")
        self.root.geometry(geometry)
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.lift()

        self.__create_widgets(column_width)
        # self.__show_app_icon()
