import facebook
from social_friends.backends import BaseFriendsProvider


class FacebookFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        Fetches friends from facebook using the oauth_token
        Returns:
            collection of friend objects fetched from facebook
        """
        # Get the access_token
        oauth_token = user.extra_data['access_token']
        graph = facebook.GraphAPI(oauth_token)

        return graph.get_connections("me", "friends")

    def fetch_friend_ids(self, user):
        """
        Fetches friend id's from facebook

        Return:
            collection of friend ids
        """
        friends = self.fetch_friends(user)
        friend_ids = []
        for friend in friends['data']:
            friend_ids.append(friend['id'])
        return friend_ids
