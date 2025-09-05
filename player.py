from inventory import Inventory

class Player:
    health: int = 10
    hunger: int = 10
    
    inventory: Inventory = Inventory()

if __name__ == "__main__":
    player = Player()
    player.inventory.add_item("coal", 10)
    player.inventory.view()