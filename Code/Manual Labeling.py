import pandas as pd
import tkinter as tk
from tkinter import scrolledtext



class ManualLabelingApp:
    def __init__(self, master, df):
        self.labeled_row_history = []
        self.master = master
        self.df = df
        self.index = self.get_next_unlabeled_row_index()
        self.edit_mode = False

        self.master.title("Manual Labeling App")

        self.label_options = tk.Label(master, text="Does this statement imply an intention to share individual participant data from this study? ", font=("Arial", 12, "bold"))
        self.label_options.pack(anchor="w")

        self.text_row = scrolledtext.ScrolledText(master, height=12, font=("Arial", 14), wrap=tk.WORD)
        self.text_row.pack(anchor="w")

        self.create_label_button("Yes", "green", self.label_as_yes)
        self.create_label_button("No", "red", self.label_as_no)
        self.create_label_button("Undecided", "yellow", self.label_as_undecided)

        self.button_undo = tk.Button(master, text="Undo", command=self.undo_label, bg="yellow")
        self.button_undo.pack(side="left", padx=5, pady=5)
        self.button_undo.pack_forget()

        self.button_save_exit = tk.Button(master, text="Save and exit", command=self.save_and_exit, bg="blue", fg="white")
        self.button_save_exit.pack(side="left", padx=5, pady=5)

        self.button_edit_text = tk.Button(master, text="Edit the text in the row", command=self.toggle_edit_mode, bg="purple", fg="white")
        self.button_edit_text.pack(side="left", padx=5, pady=5)

        self.button_update = tk.Button(master, text="Update", command=self.update_text, bg="orange")
        self.button_update.pack(side="left", padx=5, pady=5)
        self.button_update.pack_forget()

        self.button_drop_row = tk.Button(master, text="Drop Row", command=self.drop_row, bg="brown", fg="white")
        self.button_drop_row.pack(side="left", padx=5, pady=5)

        self.label_info = tk.Label(master, text="", font=("Arial", 12, "italic"), fg="blue")
        self.label_info.pack(anchor="w", padx=10, pady=5)

        self.label_count_info = tk.Label(master, text="", font=("Arial", 12, "italic"), fg="green")
        self.label_count_info.pack(anchor="w", padx=10, pady=5)

        self.save_button = tk.Button(master, text="Save", command=self.save_and_exit, bg="green", fg="white")
        self.save_button.pack(side="left", padx=5, pady=5)
        self.save_button.pack_forget()

        self.update_display()

    def create_label_button(self, label, color, command):
        button = tk.Button(self.master, text=f"Label as '{label}'", command=command, bg=color)
        button.pack(side="left", padx=5, pady=5)

    def update_display(self):
        labeled_count = self.df['M_Label'].notna().sum()
        total_count = len(self.df)
        self.label_count_info.config(text=f"Labeled Rows: {labeled_count} out of {total_count}")

        if labeled_count == total_count:
            self.label_info.config(text="Thank you for labeling. Please press the save button to save the dataset.")
            self.hide_elements_except_save_button()
        elif self.index is not None:
            row_info = f"Row {self.index + 1} - IPD Check: {self.df.at[self.index, 'IPD Check']} \n NCT: {self.df.at[self.index, 'NCT number']}"
            ipd_description = self.df.at[self.index, 'IPD Description']

            self.label_info.config(text=row_info)

            self.text_row.config(state=tk.NORMAL)
            self.text_row.delete(1.0, tk.END)
            self.text_row.insert(tk.END, ipd_description)
            self.text_row.config(state=tk.DISABLED)
        else:
            self.label_info.config(text="No row available for labeling.")
            self.hide_elements_except_save_button()
        if self.labeled_row_history:
            self.button_undo.pack(side="left", padx=5, pady=5)
        else:
            self.button_undo.pack_forget()

    def get_next_unlabeled_row_index(self):
        return self.df[self.df['M_Label'].isnull()].index[0] if self.df['M_Label'].isnull().any() else None

    def label_row(self, label):
        if self.index is not None:
            self.df['M_Label'] = self.df['M_Label'].astype(object)
            self.df.at[self.index, 'M_Label'] = label
            self.index = self.get_next_unlabeled_row_index()
            if self.index is not None:
                self.update_display()
        else:
            self.label_info.config(text="No row available for labeling.")
            self.hide_elements_except_save_button()

    def label_as_yes(self):
        self.labeled_row_history.append(self.index)
        self.label_row('Yes')

    def label_as_no(self):
        self.labeled_row_history.append(self.index)
        self.label_row('No')

    def label_as_undecided(self):
        self.labeled_row_history.append(self.index)
        self.label_row('Undecided')

    def undo_label(self):
        if self.labeled_row_history:
            last_index = self.labeled_row_history.pop()
            self.df.at[last_index, 'M_Label'] = None
            self.index = last_index
            self.update_display()
    def save_and_exit(self):
        #Dennis

        #Saber's first pc
        self.df.to_csv(r'G:\.....\df_finalized.csv', index=False)

        self.master.destroy()

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        if self.edit_mode:
            self.text_row.config(state=tk.NORMAL)
            self.button_update.pack(side="left", padx=5, pady=5)
            self.button_edit_text.config(bg="gray")
        else:
            self.text_row.config(state=tk.DISABLED)
            self.button_update.pack_forget()
            self.button_edit_text.config(bg="purple")

    def update_text(self):
        new_text = self.text_row.get(1.0, tk.END)
        new_ipd_description = new_text.strip()
        self.df.at[self.index, 'IPD Description'] = new_ipd_description
        self.toggle_edit_mode()

    def drop_row(self):
        if self.index is not None:
            self.df.drop(self.index, inplace=True)
            self.index = self.get_next_unlabeled_row_index()
            if self.index is not None:
                self.update_display()
        else:
            self.label_info.config(text="No row available for dropping.")
            self.hide_elements_except_save_button()

    def hide_elements_except_save_button(self):
        elements_to_hide = [
            self.label_options, self.text_row, self.button_undo, self.button_edit_text,
            self.button_update, self.button_drop_row, self.label_info
        ]
        for element in elements_to_hide:
            element.pack_forget()
        self.save_button.pack(side="left", padx=5, pady=5)

if __name__ == "__main__":


    #Saber's first pc
    file_path = r'G:\.....\df_finalized.csv'
    df = pd.read_csv(file_path)

    root = tk.Tk()
    app = ManualLabelingApp(root, df)
    root.mainloop()
