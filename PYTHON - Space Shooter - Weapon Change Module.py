class Weapon:
    def __init__(self, name, damage, rate_of_fire):
        self.name = name
        self.damage = damage
        self.rate_of_fire = rate_of_fire

    def __str__(self):
        return f"Weapon(name={self.name}, damage={self.damage}, rate_of_fire={self.rate_of_fire})"

class WeaponManager:
    def __init__(self):
        self.weapons = []
        self.current_weapon_index = 0

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def switch_weapon(self):
        if not self.weapons:
            print("No weapons available to switch!")
            return None
        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
        return self.get_current_weapon()

    def get_current_weapon(self):
        if not self.weapons:
            print("No weapons available!")
            return None
        return self.weapons[self.current_weapon_index]

    def __str__(self):
        return f"Current Weapon: {self.get_current_weapon()}"

# Example usage
if __name__ == "__main__":
    # Create some weapons
    laser = Weapon("Laser", 10, 0.5)
    missile = Weapon("Missile", 25, 1.5)
    plasma = Weapon("Plasma", 15, 1.0)

    # Create the weapon manager and add weapons
    weapon_manager = WeaponManager()
    weapon_manager.add_weapon(laser)
    weapon_manager.add_weapon(missile)
    weapon_manager.add_weapon(plasma)

    # Display the current weapon
    print("Initial weapon:", weapon_manager)

    # Switch weapons and display the current weapon after each switch
    for _ in range(5):
        weapon_manager.switch_weapon()
        print("Switched weapon:", weapon_manager)
