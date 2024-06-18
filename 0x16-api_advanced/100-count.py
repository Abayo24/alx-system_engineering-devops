#!/usr/bin/python3
"""Count it"""

from collections import defaultdict
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom user agent'}
    params = {'limit': 100, 'after': after}

    word_count = defaultdict(int)
    word_list = [word.lower() for word in word_list]

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                for title in hot_list:
                    words = title.lower().split()
                    for word in words:
                        if word in word_list:
                            word_count[word] += 1

                sorted_word_count = sorted(word_count.items(),
                                           key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
