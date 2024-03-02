from typing import List, Set, Dict, Union, Any


class DataBlock:
    def __init__(self, addressList: Union[List[int], Set[int], None] = None,
                 mappedData: Union[Dict[int, Any], None] = None) -> None:
        self.dataBlock: Dict[int, Any] = {}

        if addressList is not None:
            self.dataBlock = {address: 0 for address in addressList if
                              isinstance(address, int) and 0 <= address <= 0xFFFF}
        elif mappedData is not None:
            self.dataBlock = {k: v for k, v in mappedData.items() if isinstance(k, int) and 0 <= k <= 0xFFFF}

    def add(self, data: Union[Dict[int, Any], List[int], Set[int], int]) -> None:
        if isinstance(data, dict):
            valid_data = {k: 0 for k, v in data.items() if
                          isinstance(k, int) and 0 <= k <= 0xFFFF and k not in self.dataBlock}
            self.dataBlock.update(valid_data)
        elif isinstance(data, (list, set)):
            valid_items = {item for item in data if
                           isinstance(item, int) and 0 <= item <= 0xFFFF and item not in self.dataBlock}
            self.dataBlock.update({item: 0 for item in valid_items})
        elif isinstance(data, int) and 0 <= data <= 0xFFFF:
            self.dataBlock.setdefault(data, 0)
        else:
            raise ValueError("Unsupported data type for addition to DataBlock.")

    def update(self, data: Union[Dict[int, Any], List[Union[int, Any]], Set[Union[int, Any]]]) -> None:
        if isinstance(data, dict):
            for key, value in data.items():
                if key in self.dataBlock:
                    self.dataBlock[key] = value
        elif isinstance(data, (list, set)) and len(data) == 2:
            key, value = data
            if key in self.dataBlock and isinstance(value, int):
                self.dataBlock[key] = value

    def resetValues(self) -> None:
        self.dataBlock = {key: 0 for key in self.dataBlock}

    def remove(self, key: int) -> Any:
        return self.dataBlock.pop(key, None)

    def get(self) -> Dict[int, Any]:
        return self.dataBlock

    def reset(self) -> None:
        self.dataBlock = {}


class DataContextList:
    def __init__(self, slave_id, dataBlock=None, single=True):
        self.dataContextList = [{slave_id: dataBlock if isinstance(dataBlock, DataBlock) else DataBlock(dataBlock)}]
        self.single = single

        def add(self, dataBlock):
            dataContext = {slave_id: dataBlock if isinstance(dataBlock, DataBlock) else DataBlock(dataBlock)}
            self.dataContextList.push(dataContext)
            return self

        def copyBlockKeysOnly(self):
            temp_keys = self.dataBlock.keys()

        # def copyBlockValuesOnly(self):


# blok = DataBlock([1, 20, 3, 66, 4, 22, 30, 8])
# block3 = DataBlock(addressList=[1, 20, 3, 66, 4, 22, 30, 8], mappedData= {1: 'asdasd', 2: 'asdasdasd', 3: 4, 4: 12})
# blok2 = DataBlock({1, 2, 3, 4, 5, 6, 7, 8, 9})
# print(blok.get())
# print(blok2.get())
# print(block3.get())
# block3.resetValues()
# block3.add(12)
# print(block3.get())