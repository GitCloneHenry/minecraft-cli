from typing import List, Dict

from inventory import Inventory
from items import *

class CraftingSystem:
    inventory: Inventory

    def __init__(self, inventory) -> None:
        self.inventory = inventory

    def view_craftable_items(self) -> List[str]:
        craftable_items: List[str] = []
        
        for item, info in zip(items.keys(), items.values()):
            if not info["craftable"]:
                continue
    
        return craftable_items