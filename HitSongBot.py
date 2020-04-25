import tweepy
import time
import random

CONSUMER_KEY = 'nt0ilxs3zrufBkfERUsFjzAz1'
CONSUMER_SECRET = '7PnVz1QFDKMoGjoxCvL5X4DnrYrJGTmcH5PbWRkfx2mEjzUvGj'
ACCESS_KEY = '1243929084310290432-VkNa00Amg5j73Rm6FyPemrkPNZrSg4'
ACCESS_SECRET = 'rDlkrSpJxohU6KYEFFOjXY6zlHSxgTsUBg5YEahQsXn0U'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# gets the randpm song title and artists and tweets out the hit song
def create_tweet():
    # //////////////////////////     TITLE    //////////////////////////
    # access 'all_words.txt' file and place all the words into a list
    all_words = open('all_words.txt', 'r')
    words = [line for line in all_words.readlines()]
    all_words.close()

    # for either 1 or 2 times do this
    i = random.randint(1, 2)
    title = []
    for x in range(i):
        # select a random word from the words list and append to title, remove trailing \n
        title.append(random.choice(words).rstrip('\n').capitalize())

    # transfer title list to a string
    title_to_str = ' '.join(map(str, title))

    # //////////////////////////     ARTISTS    //////////////////////////
    # access 'artists.txt' file and place all the artists into a list
    all_artists = open('artists.txt', 'r')
    artists = [line for line in all_artists.readlines()]
    all_artists.close()

    # randomly select a main artist
    main_artist = random.choice(artists)

    # remove main_artist from artists list, then strip enter key
    artists.remove(main_artist)
    main_artist = main_artist.rstrip('\n')

    # randomy select a featruing artist
    feature = random.choice(artists).rstrip('\n')

    # combine title and artists to create hit song
    song = main_artist + ' - ' + title_to_str + ' Ft. ' + feature
    print(song)

    # tweet the song
    api.update_status(song)

while True:
    create_tweet()
    time.sleep(7200)
    #time.sleep(2)
