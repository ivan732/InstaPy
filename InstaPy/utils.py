import re 

save = lambda _: open('/sdcard/source.html', 'w').write(str(_))
find = lambda _, __: re.search(_, __)
fall = lambda _, __: re.findall(_, __)

class TmpObject:
    def __init__(self, data):
        for _, __ in data.items():
            if isinstance(__, dict): setattr(self, _, TmpObject(__))
            elif isinstance(__, list): setattr(self, _, [TmpObject(i__) if isinstance(i__, dict) else i__ for i__ in __])
            else: setattr(self, _, __)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, TmpObject):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [v.to_dict() if isinstance(v, TmpObject) else v for v in value]
            else:
                result[key] = value
        return result

    def __repr__(self) -> dict:
        return repr(self.to_dict())


tmp_output = lambda s__, d__: TmpObject({'status': s__, 'data': d__, 'author': './ipan'})
payload = lambda source: {'av': find(r'actorID":"(.*?)"', source).group(1),'__d': 'www','__user': '0','__a': '1','__req': '1g','__hs': find(r'"haste_session":"(.*?)"', source).group(1),'dpr': '3','__ccg': 'POOR','__rev': find(r'client_revision":(.*?),', source).group(1),'__s': '','__hsi': find(r'hsi":"(.*?)"', source).group(1),'__comet_req': '7','fb_dtsg': find(r'DTSGInitData",\[\],{"token":"(.*?)"', source).group(1),'jazoest': find(r'jazoest=(.*?)",', source).group(1),'lsd': find(r'LSD",\[\],{"token":"(.*?)"', source).group(1),'__spin_r': find(r'__spin_r":(.*?),', source).group(1),'__spin_b': 'trunk','__spin_t': find(r'__spin_t":(.*?),', source).group(1),'__crn': 'comet.igweb.PolarisFeedRoute','fb_api_caller_class': 'RelayModern','server_timestamps': 'true'}
