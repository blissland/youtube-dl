# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from .ooyala import OoyalaIE


class AftenpostenIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?aftenposten\.no/webtv/(?:#!/)?video/(?P<id>\d+)'
    _TEST = {
        'url': 'http://www.aftenposten.no/webtv/#!/video/21039/trailer-sweatshop-i-can-t-take-any-more',
        'md5': 'fd828cd29774a729bf4d4425fe192972',
        'info_dict': {
            'id': 'k0ZzRsczqA7nN0MMdbzX31-3afP-v_KU',
            'ext': 'mp4',
            'title': 'TRAILER: «SWEATSHOP» - I can´t take any more',
            'description': 'md5:21891f2b0dd7ec2f78d84a50e54f8238',
        },
        'params': {
            # Requires ffmpeg (m3u8 manifest)
            'skip_download': True,
        },
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')
	data = self._download_json("http://player.ooyala.com/player_api/v1/content_tree/external_id/5udHQxOmhnN72MyLVIuJla_kMSEl/" + video_id + "?_=1432299662045", video_id)
	content_id = data['content_tree'].keys()[0]
        ooyala_code = data['content_tree'][content_id]['embed_code']
	return OoyalaIE._build_url_result(ooyala_code)
	
