from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from models import SocialFriendList
from utils import setting

REDIRECT_IF_NO_ACCOUNT = setting('SF_REDIRECT_IF_NO_SOCIAL_ACCOUNT_FOUND', False)
REDIRECT_URL = setting('SF_REDIRECT_URL', "/")


class FriendListView(TemplateView):
    """
    displays existing social friends of the current user
    """
    template_name = "social_friends/friend_list.html"

    def get(self, request, *args, **kwargs):
        """prepare the social friend model"""
        provider = kwargs.pop('provider')

        # Get the social auth connections
        self.social_auths = request.user.social_auth.all()

        # if the user did not connect any social accounts, no need to continue
        if self.social_auths.count() == 0:
            if REDIRECT_IF_NO_ACCOUNT:
                return HttpResponseRedirect(REDIRECT_URL)
            return super(FriendListView, self).get(request)

        # for each social network, get or create social_friend_list
        self.social_friend_lists = SocialFriendList.objects.get_or_create_with_social_auths(self.social_auths)

        return super(FriendListView, self).get(request)

    def get_context_data(self, **kwargs):
        """
        checks if there is SocialFrind model record for the user
        if not attempt to create one
        if all fail, redirects to the next page
        """
        context = super(FriendListView, self).get_context_data(**kwargs)

        friends = []
        for friend_list in self.social_friend_lists:
            fs = friend_list.existing_social_friends()
            for f in fs:
                friends.append(f)

        # Add friends to context
        context['friends'] = friends

        connected_providers = []
        for sa in self.social_auths:
            connected_providers.append(sa.provider)
        context['connected_providers'] = connected_providers

        return context
