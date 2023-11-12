import json
import collections
import requests
import urllib.request
import urllib.error
import datetime

#https://consumerservicesapi.talkpython.fm/api/blog


Post = collections.namedtuple("Post", 'id title content published view_count')

base_url = 'http://consumer_services_api.talkpython.fm/'



def get_posts():
    url = base_url + 'api/blog'

    with urllib.request.urlopen(url) as resp:
        if resp.getcode() != 200:
            print("Error downloading posts: {} {}".format(resp.getcode(), resp.read()))

        text = resp.read()
        post_data = json.loads(text)

        return [
            Post(**post)
            for post in post_data
            ]

def get_post():
    url = 'https://consumerservicesapi.talkpython.fm/api/blog'
    headers = {"Content-Type": "application/json",
                "Accept": "application/json"
    }
    resp = requests.get(url, headers= headers)

    if resp.status_code == 200:
        return [
            #Post(**post)
            Post(id = post.get('id'), title = post.get('title'), content = post.get('content'), published = post.get('published'), view_count = post.get('view_count'))
            for post in resp.json()
        ]
    else:
        print(f"ERROR {resp.reason}, {resp.status_code}, {resp.text}")

def add_post():
    now = datetime.datetime.now()
    published_text = '{}-{}-{}'.format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

    title = input('title: ')
    content = input('content: ')
    view_count = int(input('view count: '))
    
    post_data = dict(title=title, content=content, view_count=view_count, published=published_text)
    url = base_url + 'api/blog'
    

    data = json.dumps(post_data).encode('utf-8')
    resp_ = requests.post(url, json=post_data, headers = {'content-type': 'application/json'} )
    req = urllib.request.Request(url, data=data, headers = {'content-type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req) as resp:
        if resp.getcode() != 201:
            print("Error creating post: {} {}".format(resp.getcode(), resp.read()))
            return

        text = resp.read()

    post = json.loads(text)

    print("Created this: ")
    print(post)


def show_posts(posts):
    if not posts:
        print("Sorry, no posts to show.")
        return

    print("------------------------------ BLOG POSTS -----------------------------------")
    max_width = max((len('{:,}'.format(int(p.view_count))) for p in posts))
    for idx, p in enumerate(posts):
        padded = ' ' * (max_width - len('{:,}'.format(int(p.view_count))))
        print("{}. {} [{}{:,}]: {}".format(idx + 1, p.id, padded, int(p.view_count), p.title))
    print()


if __name__ == '__main__':
#    print(json.dumps(get_posts(),indent=True))
#    print("\n \n \n")
#    print(get_posts())

#    print(json.dumps(get_post(),indent=True))
    add_post()
    print(get_post())