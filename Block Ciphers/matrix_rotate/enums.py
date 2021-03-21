from enum import Enum


class CipherMethodEnum(Enum):
    CRYPT = 'CRYPT'
    DECRYPT = 'DECRYPT'

    @classmethod
    def as_tuples(cls):
        return (
            (cls.CRYPT.value, 'forward crypt'),
            (cls.DECRYPT.value, 'backward decrypt')
        )
