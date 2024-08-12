# Q18) Write a Python program that retrieves the top stories from Google News

from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews.search('India')
googlenews.get_page(1)
result = googlenews.result()
for x in result:
    print("-"*50)
    print("Title--",x['title'])
    print("Date/Time--",x['date'])
    print("Description--",x['desc'])
    print("Link--",x['link'])