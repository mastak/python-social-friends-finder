from django.conf import settings


class SocialFriendsFinderBackendFactory():

    @classmethod
    def get_backend(self, backend_name):
        """
        returns the given backend instance
        """
        if backend_name == 'twitter':
            from social_friends.backends.twitter_backend import TwitterFriendsProvider
            friends_provider = TwitterFriendsProvider()
        elif backend_name == 'facebook':
            from social_friends.backends.facebook_backend import FacebookFriendsProvider
            friends_provider = FacebookFriendsProvider()
        elif backend_name == 'vkontakte-oauth2':
            from social_friends.backends.vkontakte_backend import VKontakteFriendsProvider
            friends_provider = VKontakteFriendsProvider()
        else:
            raise NotImplementedError("provider: %s is not implemented" % backend_name)

        return friends_provider


def setting(name, default=None):
    """returns the setting value or default if not exists"""
    return getattr(settings, name, default)
