from django.conf import settings
from twython import Twython

from social_friends.backends import BaseFriendsProvider


class TwitterFriendsProvider(BaseFriendsProvider):

    def _auth_data(self, user):
        tokens = user.extra_data['access_token']
        return {
            'app_key': settings.SOCIAL_AUTH_TWITTER_KEY,
            'app_secret': settings.SOCIAL_AUTH_TWITTER_SECRET,
            'oauth_token': tokens['oauth_token'],
            'oauth_token_secret': tokens['oauth_token_secret']
        }

    def fetch_friends(self, user):
        """
        fetches the friends from twitter

        Returns:
            collection of friend objects fetched from Twitter
        """
        auth_data = self._auth_data(user)
        tw = Twython(**auth_data)
        cursor = -1
        friends = []
        while True:
            data = tw.get_friends_list(cursor=cursor)
            friends += data.get('users', [])

            next_cursor = data.get('next_cursor', 0)
            prev_cursor = data.get('prev_cursor', 0)
            if not next_cursor or next_cursor == prev_cursor:
                break
            else:
                cursor = next_cursor
        return friends

    def fetch_friend_ids(self, user):
        """
        fetches friend id's from twitter

        Return:
            collection of friend ids
        """
        auth_data = self._auth_data(user)
        tw = Twython(**auth_data)
        cursor = -1
        friend_ids = []
        while True:
            data = tw.get_friends_ids(cursor=cursor)
            friend_ids += data.get('ids', [])

            next_cursor = data.get('next_cursor', 0)
            prev_cursor = data.get('prev_cursor', 0)
            if not next_cursor or next_cursor == prev_cursor:
                break
            else:
                cursor = next_cursor
        return friend_ids
