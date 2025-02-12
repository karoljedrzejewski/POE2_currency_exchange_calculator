README - How to use this application

Simply use **divined_informator.exe**, otherwise:

1. Requirements:
   - Python 3.x
   - Tkinter installed (usually available by default in most Python installations)

2. Project files:
   - logic.py: Contains the calculation logic (functions for computing ratios and profit).
   - gui.py: Contains the code to launch the Tkinter graphical interface, which uses functions from logic.py.

3. How to run:
   - Make sure both logic.py and gui.py are in the same directory.
   - Open your terminal/command prompt and navigate to that directory.
   - Run:
     ```
     python gui.py
     ```
   - A window will appear shortly.

4. How to use the application:
   - Fill in the text fields:
     - Buy ratio for item1 (empty by default, enter correct ratio for buying)
     - Buy ratio for item2 (default is 1)
     - Sell ratio for item1 (empty by default, enter correct ratio for selling)
     - Sell ratio for item2 (default is 1)
     - Total amount of item1 (total quantity of your buying resource)
   - Check the "Only proportions" checkbox if you only want to get a list of possible ratio pairs to buy, without extended calculation.
   - If the checkbox is unchecked, the app will also calculate the potential selling scenario and profit.
   - Click the "Calculate" button.
   - The results will appear in the text field on the right.

5. Results explanation:
   - "BUY" – List of pairs (Item1 count, Item2 count) matching the chosen buy ratio.
   - "SELL" – List of pairs matching the sell ratio (if the checkbox was unchecked).
   - "Total profit (in item1)" – Estimated profit in the units of the first item.

6. Contact and notes:
   - If any errors occur during startup, make sure you are using the correct Python version and that Tkinter is installed.
   - The code is split into a logic part (logic.py) and a GUI part (gui.py) for easier modification and maintenance.
