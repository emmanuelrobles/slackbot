import random
from enum import Enum

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
    return random.choice(_user[id]['names'])


class UsersEnums(str,Enum):
    PIERRE = 'U02DYBFSED6'
    EMMANUEL = 'U02D5NAHU1K'
    CK = 'U02D2HE7WMC'
    KLAJDI = 'U02D996Q51R'
    FRANCISCO = 'U02D98KAGHG'
    KEN = 'U02D99D0DA6'
    JARED = 'U02DMBMJLQH'
    SLACKBOT = 'U02CUDGHJ0P'

    def __str__(self):
        return str(self.value)


