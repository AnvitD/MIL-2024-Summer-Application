from enum import Enum
from datetime import datetime
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from collections import defaultdict

# Define Enums for different types of parts
class SolderType(Enum):
    lead = "lead"
    lead_free = "lead_free"
    rosin_core = "rosin_core"
    acid_core = "acid_core"

class DisplayCableType(Enum):
    hdmi = "hdmi"
    vga = "vga"
    displayport = "displayport"
    micro_hdmi = "micro_hdmi"

class EthernetCableAlphaType(Enum):
    male = "male"
    female = "female"

class EthernetCableBetaType(Enum):
    male = "male"
    female = "female"

class EthernetCableSpeed(Enum):
    speed_10MBPS = "10mbps"
    speed_100MBPS = "100mbps"
    speed_1GBPS = "1gbps"
    speed_10GBPS = "10gbps"

# Define a base class for parts 
class Part:
    def __init__(self, update: datetime):
        self.update = update

    def __str__(self):
        return f"Last Updated Date: {str(self.update)}" # converts the date and time to a human readable format

class Resistor(Part):
    def __init__(self, update: datetime, resistance: int, tolerance: int):
        super().__init__(update)
        self.resistance = resistance
        self.tolerance = tolerance

    def __str__(self):
        return f"{super().__str__()}, Resistance: {self.resistance}, Tolerance: {self.tolerance}"

class Solder(Part):
    def __init__(self, update: datetime, solder_type: SolderType, length: float):
        super().__init__(update)
        self.solder_type = solder_type
        self.length = length

    def __str__(self):
        return f"{super().__str__()}, Solder Type: {self.solder_type}, Length: {self.length}"

class Wire(Part):
    def __init__(self, update: datetime, gauge, length):
        super().__init__(update)
        self.gauge = gauge
        self.length = length

    def __str__(self):
        return f"{super().__str__()}, Gauge: {self.gauge}, Length: {self.length}"

class DisplayCable(Part):
    def __init__(self, update: datetime, cable_type: DisplayCableType, length: float, color: str):
        super().__init__(update)
        self.cable_type = cable_type
        self.length = length
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Cable Type: {self.cable_type}, Length: {self.length}, Color: {self.color}"

class EthernetCable(Part):
    def __init__(self, update: datetime, alpha_type: EthernetCableAlphaType, beta_type: EthernetCableBetaType, ether_speed: EthernetCableSpeed, length: float):
        super().__init__(update)
        self.alpha_type = alpha_type
        self.beta_type = beta_type
        self.ether_speed = ether_speed
        self.length = length

    def __str__(self):
        return f"{super().__str__()}, Alpha Type: {self.alpha_type}, Beta Type: {self.beta_type}, Speed: {self.ether_speed}, Length: {self.length}"
# Dictionary to map part class strings to their respective classes
PART_CLASSES = { 
    "1": Resistor,
    "2": Solder,
    "3": Wire,
    "4": DisplayCable,
    "5": EthernetCable
}

# Inventory class to manage parts and quantities
class Inventory:
    def __init__(self):
        self.inventory: Dict[int, Dict[str, Part]] = {}

    max_limit = 1000000

    def add_part(self, sku: int, part: Part):
        try:
            if len(self.inventory) >= self.max_limit:
                raise ValueError("Maximum number of parts reached (1 million). Cannot add more parts.")
            if sku in self.inventory:
                raise ValueError(f"SKU {sku} already exists.")
            self.inventory[sku] = {"part": part, "quantity": 0}
        except ValueError as e:
            print(f"Error adding part with SKU {sku}: {e}")

    def add_inventory(self, sku: int, quantity: int):
        try:
            if sku < 0:
                raise ValueError("Value cannot be less than 0")
            if sku not in self.inventory:
                raise ValueError(f"SKU {sku} does not exist.")
            
            current_quantity = self.inventory[sku]["quantity"]
            new_quantity = current_quantity + quantity

            if new_quantity < 0:
                raise ValueError("Quantity cannot go below 0")

            self.inventory[sku]["quantity"] = new_quantity

            if new_quantity == 0:
                print(f"SKU {sku} is now out of stock.")
        except ValueError as e:
            print(f"Error adding inventory for part with SKU {sku}: {e}")

    def get_quantity(self, sku: int) -> int:
        try:
            if sku not in self.inventory:
                raise ValueError(f"SKU {sku} does not exist.")
            return self.inventory[sku]["quantity"]
        except ValueError as e:
            print(f"Error getting quantity for part with SKU {sku}: {e}")
            return 0

    def get_inventory(self) -> List[Tuple[int, Dict[str, Part]]]:
        try:
            return [(sku, data) for sku, data in self.inventory.items()]
        except Exception as e:
            print(f"Error getting inventory: {e}")
            return []

    def get_part(self, sku: int) -> Part:
        try:
            if sku not in self.inventory:
                raise ValueError(f"SKU {sku} does not exist.")
            return self.inventory[sku]["part"]
        except ValueError as e:
            print(f"Error getting part with SKU {sku}: {e}")
            return None

    def search(self, part_class: str, **kwargs) -> List[Part]:
        try:
            if part_class not in PART_CLASSES:
                raise ValueError(f"Invalid part class: {part_class}")
            
            part_type = PART_CLASSES[part_class]

            return [part["part"] for part in self.inventory.values() if isinstance(part["part"], part_type) and all(getattr(part["part"], attr) == value for attr, value in kwargs.items())]
        except Exception as e:
            print(f"Error searching for part: {e}")
            return []


    def delete_part(self, sku: int):
        try:
            del self.inventory[sku]
        except KeyError as e:
            print(f"Error deleting part with SKU {sku}: {e}")

# main class
if __name__ == "__main__":
    inventory = Inventory()

# Display menu options to the user
    while True:
        print("\n Welcome to Inventory Management System")
        print("-----------------------------------------")
        print("1. Add Part")
        print("2. Add Inventory")
        print("3. Get Quantity")
        print("4. Get Inventory")
        print("5. Search")
        print("6. Delete Part")
        print("7. Show Graph")
        print("8. Exit")

        # Get user input for menu choice
        choice = input("Enter your choice: ")

        # Handle user choices based on the selected option
        if choice == "1":
            sku = int(input("Enter SKU: "))
            part_type = input("Choose part type (1. Resistor, 2. Solder, 3. Wire, 4. Display Cable, 5. Ethernet Cable): ")

            # Add a new part to the inventory
            # Based on the selected part type, creates an instance of that part and adds it to the inventory
            if part_type == "1":
                resistance = int(input("Enter resistance: "))
                tolerance = int(input("Enter tolerance: "))
                inventory.add_part(sku, Resistor(datetime.now(), resistance, tolerance))
                print("Part added succesfully")
            elif part_type == "2":             
                solder_type = SolderType[input("Enter solder type (lead, lead_free, rosin_core, acid_core): ")]
                length = float(input("Enter length: "))
                inventory.add_part(sku, Solder(datetime.now(), solder_type, length))
                print("Part added succesfully")
            elif part_type == "3":            
                gauge = float(input("Enter gauge: "))
                length = float(input("Enter length: "))
                inventory.add_part(sku, Wire(datetime.now(), gauge, length))
                print("Part added succesfully")
            elif part_type == "4":            
                cable_type = DisplayCableType[input("Enter cable type (hdmi, vga, displayport, micro_hdmi): ")]
                length = float(input("Enter length: "))
                color = input("Enter color: ")
                inventory.add_part(sku, DisplayCable(datetime.now(), cable_type, length, color))
                print("Part added succesfully")
            elif part_type == "5":             
                alpha_type = EthernetCableAlphaType[input("Enter alpha type (male, female): ")]
                beta_type = EthernetCableBetaType[input("Enter beta type (male, female): ")]
                speed = EthernetCableSpeed[input("Enter speed (speed_10MBPS, speed_100MBPS, speed_1GBPS, speed_10GBPS): ")]
                length = float(input("Enter length: "))
                inventory.add_part(sku, EthernetCable(datetime.now(), alpha_type, beta_type, speed, length))
                print("Part added succesfully")
            else:
                print("Invalid part type. Please try again.")

        elif choice == "2":            # Add inventory to an existing part
            sku = int(input("Enter SKU: "))
            quantity = int(input("Enter quantity: "))
            inventory.add_inventory(sku, quantity)
            print("Inventory Updated")

        elif choice == "3":            # Get the quantity of a specific part in the inventory
            sku = int(input("Enter SKU: "))
            print("Quantity:", inventory.get_quantity(sku))

        elif choice == "4":            # Get the entire inventory with details of each part
            print("Inventory:")
            for sku, item in inventory.get_inventory():
                part = item['part']
                quantity = item['quantity']
                part_name = ""
                part_characteristics = ""
                if isinstance(part, Resistor):
                    part_name = "Resistor"
                    part_characteristics = f"Resistance: {part.resistance} ohms, Tolerance: {part.tolerance}%"
                elif isinstance(part, Solder):
                    part_name = "Solder"
                    part_characteristics = f"Type: {part.solder_type.value}, Length: {part.length} ft"
                elif isinstance(part, Wire):
                    part_name = "Wire"
                    part_characteristics = f"Gauge: {part.gauge}, Length: {part.length} ft"
                elif isinstance(part, DisplayCable):
                    part_name = "Display Cable"
                    part_characteristics = f"Type: {part.cable_type.value}, Length: {part.length} ft, Color: {part.color}"
                elif isinstance(part, EthernetCable):
                    part_name = "Ethernet Cable"
                    part_characteristics = f"Alpha Type: {part.alpha_type.value}, Beta Type: {part.beta_type.value}, Speed: {part.ether_speed.value}, Length: {part.length} ft"
                print(f"SKU: {sku}, Part: {part_name}, Characteristics: {part_characteristics}, Quantity: {quantity}")

        elif choice == "5":            # Search for a specific part based on user-provided attributes
            part_class = input("Enter part class (1. Resistor, 2. Solder, 3. Wire, 4. Display Cable, 5. Ethernet Cable): ")
            attributes = {}
            if part_class == "1":
                attributes["resistance"] = int(input("Enter resistance: "))
                attributes["tolerance"] = int(input("Enter tolerance: "))
            elif part_class == "2":
                attributes["solder_type"] = SolderType[input("Enter solder type (lead, lead_free, rosin_core, acid_core): ")]
                attributes["length"] = float(input("Enter length: "))
            elif part_class == "3":
                attributes["gauge"] = int(input("Enter gauge: "))
                attributes["length"] = float(input("Enter length: "))
            elif part_class == "4":
                attributes["cable_type"] = DisplayCableType[input("Enter cable type (hdmi, vga, displayport, micro_hdmi): ")]
                attributes["length"] = float(input("Enter length: "))
                attributes["color"] = input("Enter color: ")
            elif part_class == "5":
                attributes["alpha_type"] = EthernetCableAlphaType[input("Enter alpha type (male, female): ")]
                attributes["beta_type"] = EthernetCableBetaType[input("Enter beta type (male, female): ")]
                attributes["ether_speed"] = EthernetCableSpeed[input("Enter speed (speed_10MBPS, speed_100MBPS, speed_1GBPS, speed_10GBPS): ")]
                attributes["length"] = float(input("Enter length: "))
            else:
                print("Invalid part class. Please try again.")

            results = inventory.search(part_class, **attributes)
            print("Search Results:")
            for result in results:
                print(result)

        elif choice == "6":            # Delete a part from the inventory
            sku = int(input("Enter SKU: "))
            inventory.delete_part(sku)
            print("Part deleted")

        elif choice == "8":            # Exit the program
            break

        elif choice == "7":             # Show graphs related to part usage and out-of-stock occurrences

            # Count the usage of each part
            usage_count = defaultdict(int)
            for sku, item in inventory.get_inventory():
                usage_count[type(item['part'])] += item['quantity']

            # Sort parts by usage count
            sorted_parts_by_usage = sorted(usage_count.items(), key=lambda x: x[1], reverse=True)

            # Plot the usage count of each part
            plt.figure(figsize=(12, 6))
            plt.bar(range(len(sorted_parts_by_usage)), [count for part, count in sorted_parts_by_usage], align='center', alpha=0.5)
            plt.xticks(range(len(sorted_parts_by_usage)), [part.__name__ for part, count in sorted_parts_by_usage], rotation=45)
            plt.xlabel('Parts')
            plt.ylabel('Usage Count')
            plt.title('Usage Count of Parts')
            plt.tight_layout()
            plt.show()

            # Check which parts commonly fall out of stock
            out_of_stock_parts = []
            for sku, item in inventory.get_inventory():
                if item['quantity'] == 0:
                    out_of_stock_parts.append(type(item['part']).__name__)

            # Count the occurrence of each out-of-stock part
            out_of_stock_count = defaultdict(int)
            for part_name in out_of_stock_parts:
                out_of_stock_count[part_name] += 1

            # Sort parts by the number of times they fall out of stock
            sorted_parts_by_out_of_stock = sorted(out_of_stock_count.items(), key=lambda x: x[1], reverse=True)

            # Plot the occurrence count of each out-of-stock part
            plt.figure(figsize=(12, 6))
            plt.bar(range(len(sorted_parts_by_out_of_stock)), [count for part, count in sorted_parts_by_out_of_stock], align='center', alpha=0.5)
            plt.xticks(range(len(sorted_parts_by_out_of_stock)), [part for part, count in sorted_parts_by_out_of_stock], rotation=45)
            plt.xlabel('Parts')
            plt.ylabel('Occurrence Count')
            plt.title('Number of Times Parts Fall Out of Stock')
            plt.tight_layout()
            plt.show()

        else:
            print("Invalid choice. Please try again.")
    