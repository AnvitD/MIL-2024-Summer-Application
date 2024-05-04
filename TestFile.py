from datetime import datetime
from MIL_Summer_App import Inventory, Resistor, Solder, Wire, DisplayCable, EthernetCable, SolderType, DisplayCableType, EthernetCableAlphaType, EthernetCableBetaType, EthernetCableSpeed
import matplotlib.pyplot as plt
from collections import defaultdict

inventory = Inventory()

# Add a few parts
inventory.add_part(1001, Resistor(datetime.now(), 100, 5))
inventory.add_part(1002, Solder(datetime.now(), SolderType.lead, 50))
inventory.add_part(1003, Wire(datetime.now(), 24, 100))
inventory.add_part(1004, DisplayCable(datetime.now(), DisplayCableType.hdmi, 10, 'black'))
inventory.add_part(1005, EthernetCable(datetime.now(), EthernetCableAlphaType.male, EthernetCableBetaType.female, EthernetCableSpeed.speed_1GBPS, 50))

# Add more parts
inventory.add_part(1006, Resistor(datetime.now(), 220, 10))
inventory.add_part(1007, Solder(datetime.now(), SolderType.lead_free, 100))
inventory.add_part(1008, Wire(datetime.now(), 26, 50))
inventory.add_part(1009, DisplayCable(datetime.now(), DisplayCableType.vga, 6, 'blue'))
inventory.add_part(1010, EthernetCable(datetime.now(), EthernetCableAlphaType.female, EthernetCableBetaType.male, EthernetCableSpeed.speed_100MBPS, 25))

# Add inventory
inventory.add_inventory(1001, 10)
inventory.add_inventory(1002, 20)
inventory.add_inventory(1003, 30)
inventory.add_inventory(1004, 5)
inventory.add_inventory(1005, 15)
inventory.add_inventory(1006, 0)  # Set quantity to 0 to simulate out-of-stock
inventory.add_inventory(1007, 0)
inventory.add_inventory(1008, 0)
inventory.add_inventory(1009, 0)
inventory.add_inventory(1010, 0)

# Show the final inventory
print("\nFinal Inventory:")
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

# Display the usage count graph
usage_count = defaultdict(int)
for sku, item in inventory.get_inventory():
    usage_count[type(item['part'])] += item['quantity']

sorted_parts_by_usage = sorted(usage_count.items(), key=lambda x: x[1], reverse=True)

plt.figure(figsize=(12, 6))
plt.bar(range(len(sorted_parts_by_usage)), [count for part, count in sorted_parts_by_usage], align='center', alpha=0.5)
plt.xticks(range(len(sorted_parts_by_usage)), [part.__name__ for part, count in sorted_parts_by_usage], rotation=45)
plt.xlabel('Parts')
plt.ylabel('Usage Count')
plt.title('Usage Count of Parts')
plt.tight_layout()
plt.show()

# Display the out-of-stock count graph
out_of_stock_parts = []
for sku, item in inventory.get_inventory():
    if item['quantity'] == 0:
        out_of_stock_parts.append(type(item['part']).__name__)

out_of_stock_count = defaultdict(int)
for part_name in out_of_stock_parts:
    out_of_stock_count[part_name] += 1

sorted_parts_by_out_of_stock = sorted(out_of_stock_count.items(), key=lambda x: x[1], reverse=True)

plt.figure(figsize=(12, 6))
plt.bar(range(len(sorted_parts_by_out_of_stock)), [count for part, count in sorted_parts_by_out_of_stock], align='center', alpha=0.5)
plt.xticks(range(len(sorted_parts_by_out_of_stock)), [part for part, count in sorted_parts_by_out_of_stock], rotation=45)
plt.xlabel('Parts')
plt.ylabel('Occurrence Count')
plt.title('Number of Times Parts Fall Out of Stock')
plt.tight_layout()
plt.show()
