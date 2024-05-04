# MIL-2024-Summer-Application

To test the functionality of the Inventory Management System, you have two options:

1.MIL_Summer_app: Run MIL_Summer_app.py, which provides a user-friendly menu interface with eight options:
Add Part
Add Inventory
Get Quantity
Get Inventory
Search
Delete Part
Show Graph
Exit

I recommend to run MIL_Summer_app.py first to see the main code. However, this may be tedious as you have to add parts before you
can call some functions such as get_inventory or search. 

2.Testfile.py: Run Testfile.py for a more detailed test of each function. 
This file will execute each function separately and also provide graphs for better visualization.The functions you can test include:
Adding parts and inventory
Checking quantity
Displaying the entire inventory
Searching for specific parts
Deleting parts
You can use these options to thoroughly test the Inventory Management System and ensure its functionality meets your requirements.

The Inventory Management System is designed to efficiently manage and track various electronic parts and cables. 
The system utilizes object-oriented programming principles, with each part type represented by a class that inherits from a base Part class. 
This design allows for easy extension and modification of part types in the future. The Inventory class serves as the central component, 
storing parts in a dictionary with their SKUs as keys.

The system's API is designed to be user-friendly, offering a menu-driven interface (MIL_Summer_app.py) for easy interaction. 
Users can add new parts, update inventory quantities, check part quantities, search for specific parts, and delete parts as needed. 
Additionally, the system provides visualizations of part usage and out-of-stock occurrences through matplotlib graphs, aiding in inventory management decisions.

Overall, the system's design prioritizes flexibility, scalability, and ease of use, making it suitable for managing inventories of electronic components in various settings.


Expected output to check for inventory 
![image](https://github.com/AnvitD/MIL-2024-Summer-Application/assets/145631952/ce2de943-e913-4ab5-b2c5-eb331f011364)

Expected grpahs. 
Inventory stock - ![image](https://github.com/AnvitD/MIL-2024-Summer-Application/assets/145631952/37d15e33-82ce-4979-bc29-bf6a7949ca93)
Out of stock - ![image](https://github.com/AnvitD/MIL-2024-Summer-Application/assets/145631952/114403c8-fd32-4b91-8be9-3ad264fb1253)

These only show some of the outputs of the code. Please run MIL_Summer_App.py to see the best abilities of the code. 

Thankyou for your time and consideration. 















