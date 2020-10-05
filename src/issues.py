from github import Github
import os

token = os.getenv('GITHUB_SECRET')
g = Github(token)

def issuecreate(user, inbody):
	print('Issue query')
	if inbody == '':
		return 'You did not include your issue\'s text'

	repo = g.get_repo("gadhagod/GadhaBot")
	i = repo.create_issue(
		title='Issue created by discord user ' + user,
		body = ('From discord user ' + user + ':\n' + inbody),
		labels=[
		repo.get_label("from discord user")
		]
	)
	return 'Issue reported. Check https://github.com/gadhagod/GadhaBot/issues?q=is%3Aissue+is%3Aall to see all issues.'
