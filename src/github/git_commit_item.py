

class GitCommitItem(object):

    def __init__(self, sha, html_url, message):
        self.sha = sha
        self.html_url = html_url
        self.message = message

    def __str__(self):
        return "SHA: ".join(self.sha)\
            .join("\nMessage: ").join(self.message)\
            .join("\nURL: ").join(self.html_url)
