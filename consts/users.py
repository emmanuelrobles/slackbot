import random

_user = {
    'U02D2HE7WMC': {
        'names': ['CK', 'Cornelius']
    },
    'U02D5NAHU1K': {
        'names': ['Manny', 'Emmanuel']
    },
    'U02D68SFM0D': {
        'names': ['Aaron']
    },
    'U02D98KAGHG': {
        'names': ['Francisco', 'Cisco']
    },
    'U02D996Q51R': {
        'names': ['Klajdi']
    },
    'U02D99D0DA6': {
        'names': ['Ken']
    },
    'U02DMBMJLQH': {
        'names': ['Jared']
    },
    'U02DYBFSED6': {
        'names': ['Pierre']
    },
}


def get_all_names(id: str):
    return _user[id]['names']

def get_a_name(id: str):
   return random.choice( _user[id]['names'])
