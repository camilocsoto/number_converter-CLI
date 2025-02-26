from typing import Protocol

class ConvertInt(Protocol):


    def next_transform(self, num_to_transform:str) -> str:
        ...
    
    def reverse_transform(self, num_to_transform:str) -> str:
        ...