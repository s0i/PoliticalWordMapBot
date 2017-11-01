import praw
import requests
import time
import json

threads = []
keywords = ['trump', 'the_donald', 'administration', 'president', 'impeach', 'Trump', 'Impeach', 'Administration', 'The_Donald', 'The_donald', 'President', 'Mueller', 'mueller', 'investigation', 'Investigation', 'Russia', 'russia', 'Kremlin', 'kremlin']
subs = []
counter = 0
pastes = []

api = {
	'key': 'fe41e9b514efe2d0118ceb24eb99bd35',
	'dev_key': 'b36153beb0b6dd9098d5de1a31cf7eff',
	'post': 'https://pastebin.com/api/api_post.php',
	'user': 's0i',
	'password': 'KQC-U3n-WXM-cuZ'
}

def main():
	counter = 0
	bot = praw.Reddit(user_agent='AutoMirrorBot v0.1',
					client_id='A9R6EChehHwOFg',
					client_secret='toXo534cDEp7gGioGYqdJ7tHPqE',
					username='AutoMirrorBot',
					password='cnS-QgK-K9U-XSQ')

	subreddit = bot.subreddit('Politics+WorldNews+WorldPolitics+WorldEvents+Business+USPolitics+AmericanPolitics+Libertarian+Conservative+Democrats+Socialism+Democracy')

	for sub in subreddit.stream.submissions():
		if any(keyword in sub.title for keyword in keywords):
			if not any(sub.title in thread['title'] for thread in threads):
				threads.append({'title': sub.title, 'time': time.time()})
				print(sub.title)
				subs.append(sub.title + '\n')
				counter += 1
				
			if counter == 10:
				post()
				counter = 0

def post():
	r = requests.post(api['post'], data={ 'api_dev_key': api['dev_key'], 'api_option': 'paste', 'api_paste_code': ''.join(subs), 'api_user_key': api['key'], 'api_paste_private': '1', 'api_paste_name': time.time() })
	pastes.append({'url': r.text, 'key': r.text.rsplit('/', 1)[-1]})

	print(pastes[-1]['url'])

if __name__ == '__main__':
	main()
