import tkinter as tk
from pjo import (
    calculate_full_exchange,
    calculate_buy_proportions_only
)


def on_submit():
    try:
        text_output.delete("1.0", tk.END)
        if var_only_proportions.get():
            data = calculate_buy_proportions_only(
                float(entry_buy_item1.get()),
                float(entry_buy_item2.get()),
                float(entry_total_item1.get())
            )
            text_output.insert(tk.END, "BUY\n")
            for d in data:
                text_output.insert(
                    tk.END, 
                    f"Ratio: {d['ratio']}, Item1 count: {d['x1']}, Item2 count: {d['x2']}\n"
                )
        else:
            buy, sell, profit = calculate_full_exchange(
                float(entry_buy_item1.get()),
                float(entry_buy_item2.get()),
                float(entry_sell_item1.get()),
                float(entry_sell_item2.get()),
                float(entry_total_item1.get())
            )
            text_output.insert(tk.END, "BUY\n")
            for b in buy:
                text_output.insert(
                    tk.END, 
                    f"Ratio: {b['ratio']}, Item1 count: {b['x1']}, Item2 count: {b['x2']}\n"
                )
            text_output.insert(tk.END, "\nSELL\n")
            for s in sell:
                text_output.insert(
                    tk.END,
                    f"Ratio: {s['ratio']}, Item1 count: {s['x1']}, Item2 count: {s['x2']}\n"
                )
            text_output.insert(tk.END, f"\nTotal profit (in item1): {profit}\n")

    except Exception as e:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, str(e))


root = tk.Tk()
root.title("Currency Exchange Ratio Calculator")

label_buy_item1 = tk.Label(root, text="Buy ratio for item1")
label_buy_item1.grid(row=0, column=0, sticky="w", padx=4, pady=0)
entry_buy_item1 = tk.Entry(root)
entry_buy_item1.grid(row=0, column=1, padx=4, pady=0)

label_buy_item2 = tk.Label(root, text="Buy ratio for item2")
label_buy_item2.grid(row=1, column=0, sticky="w", padx=4, pady=0)
entry_buy_item2 = tk.Entry(root)
entry_buy_item2.grid(row=1, column=1, padx=4, pady=0)
entry_buy_item2.insert(0, "1")

label_sell_item1 = tk.Label(root, text="Sell ratio for item1")
label_sell_item1.grid(row=2, column=0, sticky="w", padx=4, pady=0)
entry_sell_item1 = tk.Entry(root)
entry_sell_item1.grid(row=2, column=1, padx=4, pady=0)

label_sell_item2 = tk.Label(root, text="Sell ratio for item2")
label_sell_item2.grid(row=3, column=0, sticky="w", padx=4, pady=0)
entry_sell_item2 = tk.Entry(root)
entry_sell_item2.grid(row=3, column=1, padx=4, pady=0)
entry_sell_item2.insert(0, "1")

label_total_item1 = tk.Label(root, text="Total amount of item1")
label_total_item1.grid(row=4, column=0, sticky="w", padx=4, pady=0)
entry_total_item1 = tk.Entry(root)
entry_total_item1.grid(row=4, column=1, padx=4, pady=0)

var_only_proportions = tk.BooleanVar()
check_proportions = tk.Checkbutton(root, text="Only proportions", variable=var_only_proportions)
check_proportions.grid(row=5, column=0, padx=4, pady=0, sticky="w")

button_submit = tk.Button(root, text="Calculate", command=on_submit)
button_submit.grid(row=5, column=1, padx=4, pady=0)

text_output = tk.Text(root, height=15, width=50)
text_output.grid(row=0, column=2, rowspan=6, padx=4, pady=0)

root.mainloop()