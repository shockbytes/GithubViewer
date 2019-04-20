from github import Github

from src.github.git_commit_item import GitCommitItem
from src.user.credentials_manager import CredentialsManager


class GithubRepository(object):

    @staticmethod
    def __init_github(github_user):
        return Github(github_user.username, github_user.password)

    @staticmethod
    def __grab_repositories_of_user(_username, _repos):
        return list(filter(lambda _repo: _repo.owner.login == _username, _repos))

    def __init__(self, cred_file):
        """

        :param cred_file:
        """
        self.credentials_manager = CredentialsManager(cred_file)
        self.github = self.__init_github(self.credentials_manager.load_github_user())

    def grab_user_avatar_url(self):
        return self.github.get_user().avatar_url

    def get_repository_for_name(self, _name):
        return next(filter(lambda r: r.name == _name, self.get_repositories()))

    def get_repositories(self):
        return self.__grab_repositories_of_user(
            self.credentials_manager.load_github_user().username.lower(),
            self.github.get_user().get_repos()
        )

    def get_commits_for_repository(self, _repository_name):
        r = self.get_repository_for_name(_repository_name)
        return map(lambda c: GitCommitItem(c.commit.sha, c.commit.html_url, c.commit.message), r.get_commits().reversed)

    def get_user(self):
        return self.github.get_user()
