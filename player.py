from typing import List

from item import Item

class Player:
    health: int = 10
    hunger: int = 10
    
    inventory: List[Item] = [Item("coal"),Item("coal")]

    def view_inventory(self) -> None:
        inventory_items: List[Item] = []

        for item in self.inventory:
            if item in self.inventory and not item in inventory_items:
                inventory_items.append(item)

        for item in inventory_items:
            print(self.inventory.count(item))

player = Player()
player.view_inventory()