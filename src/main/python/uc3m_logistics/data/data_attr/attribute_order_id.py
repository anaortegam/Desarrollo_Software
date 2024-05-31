"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class OrderId(Attribute):
    """Clase hija, atributo OrderId"""
    __ERROR = "order id is not valid"
    __PATTERN = r"[0-9a-fA-F]{32}$"
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = self.__ERROR
        self._validation_pattern = self.__PATTERN
        self._attr_value = self._validate(attr_value)