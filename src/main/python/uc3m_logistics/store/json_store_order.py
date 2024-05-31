"""MODULES"""
from uc3m_logistics.store.json_store_master import JsonStoreMaster
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class JsonOrderStore(JsonStoreMaster):
    """Clase JsonOrderStore"""
    _FILE_PATH = JSON_FILES_PATH + "orders_store.json"
    _data_list = []
    _ID_FIELD = "_OrderRequest__order_id"
    __instance = None
    def __new__(cls):
        """Patron Songleton"""
        if JsonOrderStore.__instance is None:
            JsonOrderStore.__instance = object.__new__(cls)
        return JsonOrderStore.__instance
    def __init__(self)->None:
        """Constructor de JsonDeliverStore"""
        super(JsonStoreMaster, self).__init__()
    def add_item(self, item:any)->None:
        """Añade un elemento"""
        self.load_store()
        item_found = self.find_data(item.order_id)
        if item_found is None:
            self._data_list.append(item.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        self.save_store()
