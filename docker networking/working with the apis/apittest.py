import requests

def fetch_random_cat_fact():
    url="https://meowfacts.herokuapp.com"

    try:
        response=requests.get(url)
        response.raise_for_status()  #check for any http errors

        fact = response.text
        return fact
    except requests.exceptions.RequestException as e:
        print(f"An error occureed : {e}")
        return None
#this is the the function to call that thing
def main():
    fact=fetch_random_cat_fact()
    if fact:
        print("Random cat Fact : ")
        print(fact)
#this is the driver function : it's actually calling the main 
if __name__=="__main__":
    main()