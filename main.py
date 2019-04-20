from tkinter import Tk

from src.github.github_repository import GithubRepository
from src.ui.application_view_model import ApplicationViewModel
from src.ui.application_window import ApplicationWindow

if __name__ == '__main__':

    github_repository = GithubRepository("data/credentials.json")
    view_model = ApplicationViewModel(github_repository)
    width = 800
    geometry = "{0}x600+400+200".format(width)
    column_width = int(width / 2)

    window = ApplicationWindow(Tk(), view_model, geometry, column_width)

    """

    for userRepo in github_repository.get_repositories():
        print(userRepo.name)

    for commit in github_repository.get_commits_for_repository("CoreyWeb"):
        print(commit.sha)
        print(commit.message)
        print(commit.html_url)
        print("__________________")
    """

    window.mainloop()
