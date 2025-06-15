import json
from .utils import find, fall, tmp_output, TmpObject
from . import Instagram

class Scraping:
    def __init__(self, session: Instagram) -> None:
        self.__ses = session.session 
        self.__headers = session.headers 
        self.__base_data = session.base_data 

    def timeline_post(self, cursor: str = None) -> TmpObject:
        data = {
            **self.__base_data,
            'fb_api_req_friendly_name': 'PolarisFeedRootPaginationCachedQuery_subscribe',
            'variables': json.dumps({"after": cursor, "before": None,"data": {"device_id": "44EC41CC-42E5-42E2-8A09-DA64530E08B4","is_async_ads_double_request": "0","is_async_ads_in_headload_enabled": "0","is_async_ads_rti": "0","rti_delivery_backend": "0","feed_view_info": [{"media_id": '', "media_pct": 1, "time_info": {"10": 1327, "25": 1327, "50": 1327, "75": 1327}, "version": 24}]},"first": 12, "last": None, "variant": "home","__relay_internal__pv__PolarisIsLoggedInrelayprovider": True,"__relay_internal__pv__PolarisShareSheetV3relayprovider": True}),
            'doc_id': '9818107414934772'
        }
        post = self.__ses.post('https://www.instagram.com/graphql/query', data=data, headers=self.__headers).text
        extract = lambda pattern: fall(pattern, post)

        post_data = zip(
            extract(r'\{"media":\{"id":"(.*?)_.*?"'),
            extract(r'"code":"(.*?)"'),
            extract(r'"pk":".*?","text":"(.*?)"'),
            extract(r'"comment_count":(.*?),'),
            extract(r'"story_cta":null,"like_count":(.*?),'),
            extract(r',"transparency_label":.*?,"username":"(.*?)","ai_agent'),
            extract(r'"owner":\{"pk":"(.*?)"')
        )
        collected_data = [{'user': {'username': username,'user_id': user_id},'post_id': post_id,'post_url': post_url,'caption': caption,'comment_count': comment_count,'like_count': like_count} for post_id, post_url, caption, comment_count, like_count, username, user_id in post_data]
        cursor = find(r'"page_info":{"has_next_page":true,"end_cursor":"(.*?)"', post).group(1)

        return tmp_output(s__=True, d__={'cursor': cursor, 'post': collected_data})

