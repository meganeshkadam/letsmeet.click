from rest_framework import serializers

from .models import Community


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = (
            'id',
            'url',
            'name',
            'slug',
            'description',
            'cname',
            'twitter',
            'github',
            'homepage',
            'irc_network',
            'irc_channel',
            'slack',
        )
