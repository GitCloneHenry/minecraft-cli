from typing import Dict

class Inventory:
    items: Dict[str, int] = {}

    def add_item(self, item_id: str, amount: int) -> None:
        if not item_id in self.items.keys():
            self.items[item_id] = amount
        else:
            self.items[item_id] += amount
    
    def view(self) -> None:
        for item, amount in zip(self.items.keys(), self.items.values()):
            print(f"{item}: {amount}")