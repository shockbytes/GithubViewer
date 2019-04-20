import json

from src.user.github_user import GithubUser


class CredentialsManager(object):

    def __init__(self, c_file):
        self.credentials_file = c_file

    def load_github_user(self):
        return self.__load_credentials_from_file()

    def __load_credentials_from_file(self):

        with open(self.credentials_file) as json_file:
            data = json.load(json_file)
            return GithubUser(data['username'], data['password'])

