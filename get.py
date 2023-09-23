import requests

def main():
#print("Hi from vs code dandy")
    url = 'https://training.talkpython.fm/'
#https://training.talkpython.fm/
#http://gitlab.lab.com

    rep= requests.get(url, verify=False)

    if rep.status_code != 200:
         print("Error Req URL, {}".format(rep.status_code))
         return
 
    print(rep.text[:500])
    
if __name__ == '__main__':
   main()