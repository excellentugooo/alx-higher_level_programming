#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, att_value):
        """Override == opeartor with != behavior."""
        return self.real != att_value

    def __ne__(self, att_value):
        """Override != operator with == behavior."""
        return self.real == att_value
