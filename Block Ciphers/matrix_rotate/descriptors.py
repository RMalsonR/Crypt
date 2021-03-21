import string
from abc import ABC
from copy import deepcopy


class MatrixValidator(ABC):
    """Validator class for Matrix Descriptor. Make using fields - private."""

    allowable_symbols = []

    def __set_name__(self, owner, name):
        """Set private name for field."""

        self.private_name = '_' + name
        self.owner_name = name

    def __get__(self, instance, owner):
        """Returning value from private field."""

        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        """Validate and setting value to private field."""

        self._validated_data = self.validate(value)
        setattr(instance, self.private_name, self._validated_data)

    def validate(self, value):
        """Validate matrix data.

        :parameter: value: raw matrix
        :return validated data
        """
        validated_data = deepcopy(value)
        if not validated_data or validated_data is None:
            raise ValueError(f'Matrix can not be empty in {self.owner_name}')
        if not isinstance(validated_data, list):
            raise TypeError(f'Expected matrix type `list`, got `{type(value)}` instead. In {self.owner_name}')

        if not self.allowable_symbols:
            raise ValueError(f'`allowable_symbols` can not be empty or None in `{self.__class__.__name__}`')

        # Create list of chars instead of strings
        for idx, val in enumerate(validated_data):
            if not isinstance(val, list):
                validated_data[idx] = [char for char in val if char in self.allowable_symbols]

        invalid_length_list = [len(item) for item in validated_data if len(item) != 5]

        if len(validated_data) != 5:
            raise ValueError(f'Expected matrix column shape = 5, got `{len(validated_data)}`'
                             f' instead in {self.owner_name}')
        if invalid_length_list:
            raise ValueError(f'Expected matrix row shape = 5, got `{invalid_length_list[0]}`'
                             f' instead in {self.owner_name}')

        return validated_data


class CipherMatrixDescriptor(MatrixValidator):
    """Descriptor for forward matrix."""
    allowable_symbols = string.ascii_lowercase


class CipherKeyMatrixDescriptor(MatrixValidator):
    """Descriptor for backward matrix."""
    allowable_symbols = ['X', '.']
