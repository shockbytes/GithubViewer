import rx
from rx.concurrency import ThreadPoolScheduler


class ApplicationViewModel(object):

    def __init__(self, github_repository):
        self.__github_repository = github_repository

    @property
    def user_name(self):
        return self.__github_repository.get_user().name

    @property
    def user_company(self):
        return self.__github_repository.get_user().company

    @property
    def user_image_url(self):
        return self.__github_repository.grab_user_avatar_url()

    def get_repositories_async(self):
        return rx.from_callable(lambda: self.__github_repository.get_repositories(), scheduler=ThreadPoolScheduler(4))
