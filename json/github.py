import requests
import json

def main():
    user,repo = get_repo_info()
    #user=manuh-L
    #repo=manuh-L
    url = f'https://api.github.com/repos/{user}/{repo}'#.format(user,repo)
    #url = 'https://api.github.com/repos/{}/{}'#.format(user,repo)
#    'https://api.github.com/repos/manuh-L/facebooc'
    resp= requests.get(url)
    
    if resp.status_code != 200:
        print("Error: {}".format(resp.status_code))
        return
#    print(resp.text)
#    print(resp.json)
##    json_data= json.loads(resp.text)
#    print(json_data)
#    print(resp.status_code)
##    print(json.dumps(json_data,indent=True))
    repo_data = resp.json()
    clone = repo_data.get('clone_url', 'ERROR: NO DATA')
    
    print("git clone {}".format(clone))
##    print(repo_data)

def get_repo_info():
    user = input("User name? ")
    repo = input("What is the repo name? ")
    return user, repo

if __name__== '__main__':
    main()