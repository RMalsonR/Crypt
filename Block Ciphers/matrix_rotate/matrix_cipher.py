from typing import List

from .descriptors import CipherMatrixDescriptor, CipherKeyMatrixDescriptor
from .enums import CipherMethodEnum


class ScramblerService:
    forward_matrix: List[List[str]] = CipherMatrixDescriptor()
    backward_matrix: List[List[str]] = CipherKeyMatrixDescriptor()
    input_matrix: List[str] = CipherMatrixDescriptor()

    ROTATING_COUNT = 5
    BACKWARD_KEY = 'X'

    def __init__(self, method,  forward_matrix=None, backward_matrix=None, input_matrix=None):
        if method == CipherMethodEnum.CRYPT.value:
            self.forward_matrix = forward_matrix
        if method == CipherMethodEnum.DECRYPT.value:
            self.backward_matrix = backward_matrix
            self.input_matrix = input_matrix

    def encrypt(self):
        """Encrypting using the forward matrix.
        :return: string, password
        """

        rotated_matrix = [list(reversed(col)) for col in zip(*self.forward_matrix)]
        for _ in range(0, self.ROTATING_COUNT):
            rotated_matrix = [list(reversed(col)) for col in zip(*rotated_matrix)]
        return ''.join(rotated_matrix[0])

    @staticmethod
    def _get_decrypted_chars(iterable: list, key: str):
        """Return generator like (idx_col, idx_val), where values are indexes of `key` in `iterable`
        :param iterable: the backward_matrix
        :param key: the finding key in iterable"""

        for idx_col, val_col in enumerate(iterable):
            for idx_row, val_row in val_col:
                if val_row == key:
                    yield idx_col, idx_row

    def get_psd(self):
        """Get password from backward and input matrix.
        :return string, password
        """

        key = self.BACKWARD_KEY

        char_idxes = self._get_decrypted_chars(self.backward_matrix, key)
        password_list = [self.input_matrix[idxes[0]][idxes[1]] for idxes in char_idxes]
        return ''.join(password_list)







