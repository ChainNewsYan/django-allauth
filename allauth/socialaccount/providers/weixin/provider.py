from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class WeixinAccount(ProviderAccount):

    def get_avatar_url(self):
        return self.account.extra_data.get('headimgurl')

    def to_str(self):
        return self.account.extra_data.get(
            'nickname',
            super(WeixinAccount, self).to_str())


class WeixinProvider(OAuth2Provider):
    id = 'weixin'
    name = 'Weixin'
    account_class = WeixinAccount

    def extract_uid(self, data):
        uid_type = self.get_uid_type()
        return data[uid_type]

    def get_default_scope(self):
        return ['snsapi_login']

    def extract_common_fields(self, data):
        return dict(username=data.get('nickname'),
                    name=data.get('nickname'))

    def get_uid_type(self):
        settings = self.get_settings()
        uid_type = settings.get('UID_TYPE', 'openid')
        return uid_type


provider_classes = [WeixinProvider]
