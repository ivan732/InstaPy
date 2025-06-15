import json
from .utils import find, fall, tmp_output, TmpObject
from . import Instagram

class Automation:
    def __init__(self, session: Instagram) -> None:
        self.__ses = session.session 
        self.__headers = session.headers
        self.__base_data = session.base_data 

    def like(self, post_id: str) -> TmpObject:
        data = {
            **self.__base_data,
            'fb_api_req_friendly_name':'usePolarisLikeMediaLikeMutation', 
            'variables': json.dumps({"media_id": str(post_id),"container_module":"single_post"}), 
            'doc_id': '23951234354462179'
        }

        post = self.__ses.post('https://www.instagram.com/graphql/query', data=data, headers=self.__headers).text
        if 'status":"ok"' in post: return tmp_output(s__=True, d__=None)
        else: return tmp_output(s__=False, d__=None)
