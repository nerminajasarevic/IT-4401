from tweet import Tweet
import pickle
import os

#create
def make_tweet(tweets):
    
    name = input("What is your name? ")
    text = input("What would you like to tweet? ")

    #check if less than 140 characters
    if len(text) > 140:
        print("Tweets can only be 140 characters!")
        
    #post tweet
    else:
        tweets.append(Tweet(name, text))
        serialize(tweets)
        print(f"{name}, your tweet has been saved.")
        print()

#view
def view_recent_tweets(tweets):
    
    print("Recent Tweets")
    print("-——————")

    #no tweets
    if not tweets:
        print("There are no recent tweets.")
        
    #print tweets from most to least recent
    else:
        for tweet in reversed(tweets[-5:]):
            print(f"{tweet.get_author()} - {tweet.get_age()}")
            print(tweet.get_text())
            print()

#search
def search_tweets(tweets):
    
    #no tweets
    if not tweets:
        print("There are no tweets to search.")
        print()
        return
    
    keyword = input("What would you like to search for? ").lower()

    search = []

    #look for a keyword and add to search
    for tweet in tweets:
        if keyword in tweet.get_text().lower():
            search.append(tweet)

    print()
    print("Search Results")
    print("-——————")

    #keyword does not exist
    if not search:
        print(f"No tweets contained {keyword}")
        
    #keyword exists
    else:
        for tweet in reversed(search):
            print(f"{tweet.get_author()} - {tweet.get_age()}")
            print(tweet.get_text())
            print()

def serialize(tweets):

    #write tweets to file
    with open("tweets.dat", "wb") as f:
        pickle.dump(tweets, f)

def deserialize():

    #read saved tweets from file and return as list
    if os.path.isfile("tweets.dat"):
        with open("tweets.dat", "rb") as f:
            tweets = pickle.load(f)
            
    else:
        tweets = []
        
    return tweets

#print menu
def display_menu():
    print("Tweet Menu")
    print("-—————")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    print()

def main():
    
    #create list of saved tweets from file
    tweets = deserialize()

    display_menu()

    while True:
        option = input("What would you like to do? ")

        #error checking
        try:
            option = int(option)

        except ValueError:
            print("Please enter a numeric value.")
            print()
            continue

        if option < 1 or option > 4:
            print("Please select a valid option.")
            print()
            continue

        if option == 1:
            make_tweet(tweets)
            
        elif option == 2:
            view_recent_tweets(tweets)
            
        elif option == 3:
            search_tweets(tweets)
            
        elif option == 4:
            print("Thank you for using the Tweet Manager!")
            break

        display_menu()


main()

