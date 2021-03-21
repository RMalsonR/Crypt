import pytest

from .matrix_cipher import ScramblerService
from .enums import CipherMethodEnum


def test_forward_ideal_conditions():
    method = CipherMethodEnum.CRYPT.value
    forward_matrix = ['itdfq', 'gdcex', 'atonf', 'qrdig', 'djdyr']
    service = ScramblerService(method=method, forward_matrix=forward_matrix)
    assert service.encrypt() == 'rydjd'


def test_backward_ideal_conditions():
    method = CipherMethodEnum.DECRYPT.value
    backward_matrix = ['X....', '..X..', 'X..X.', '.X...', '.....']
    input_matrix = ['itdfq', 'gdcex', 'atonf', 'qrdig', 'djdyr']
    service = ScramblerService(method=method, backward_matrix=backward_matrix, input_matrix=input_matrix)
    assert service.encrypt() == 'icanr'


def test_shape_value_error():
    method = CipherMethodEnum.CRYPT.value
    forward_matrix = ['itdf', 'gdex', 'anf', '', 'dr']
    with pytest.raises(ValueError):
        service = ScramblerService(method=method, forward_matrix=forward_matrix)
        service.encrypt()


def test_not_available_characters():
    method = CipherMethodEnum.CRYPT.value
    forward_matrix = ['itDfq', 'gdcEx', 'atЛnf', 'qrdiФ', 'пjdyр']
    with pytest.raises(ValueError):
        service = ScramblerService(method=method, forward_matrix=forward_matrix)
        service.encrypt()


def test_empty_matrix():
    method = CipherMethodEnum.CRYPT.value
    forward_matrix = []
    with pytest.raises(ValueError):
        service = ScramblerService(method=method, forward_matrix=forward_matrix)
        service.encrypt()


def test_incorrect_type_of_input_matrix():
    method = CipherMethodEnum.CRYPT.value
    forward_matrix = {
        '1': 'itxfq',
        '2': 'gdcex',
        '3': 'atlnf',
        '4': 'qrdif',
        '5': 'gjdyq'
    }
    with pytest.raises(TypeError):
        service = ScramblerService(method=method, forward_matrix=forward_matrix)
        service.encrypt()
