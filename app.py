import csv
import tkinter as tk
from tkinter import messagebox

def remove_square_brackets(row):
    return [cell.strip('[]') for cell in row]

def print_formatted_row(row, headers):
    return ' | '.join([f"{cell:<15}" for cell in row])

def table():
    try:
        with open('Premteamtable.csv', 'r', newline='') as f:
            readng = csv.reader(f)
            rows = [remove_square_brackets(row) for row in readng]

        headers = rows[0]
        rows = rows[1:]

        formatted_rows = [print_formatted_row(row, headers) for row in rows]
        return '\n'.join(formatted_rows)

    except IOError:
        return 'Sorry, the app is down for maintenance'

def team(team_choice):
    team_files = {
        1: 'manchestercity.csv',
        # ... (other team files)
        20: 'south.csv'
    }

    file_path = team_files.get(team_choice)

    if file_path is None:
        return "Invalid team choice."

    try:
        with open(file_path, 'r', newline='') as f:
            readng = csv.reader(f)
            rows = [remove_square_brackets(row) for row in readng]

        headers = rows[0]
        rows = rows[1:]

        formatted_rows = [print_formatted_row(row, headers) for row in rows]
        return '\n'.join(formatted_rows)

    except IOError:
        return 'Sorry, the app is down for maintenance'

def ols():
    try:
        with open('Premteamtable.csv', 'r', newline='') as f:
            readng = csv.reader(f)
            rows = [remove_square_brackets(row) for row in readng]

        headers = rows[0]
        rows = rows[1:]

        formatted_rows = [print_formatted_row(row, headers) for row in rows]
        return '\n'.join(formatted_rows)

    except IOError:
        return 'Sorry, the app is down for maintenance'

def show_table():
    result_text.set(table())
    
def show_team_stats():
    team_choice = int(team_choice_var.get())
    result_text.set(team(team_choice))
    
def show_ols():
    result_text.set(ols())

def main_menu():
    root = tk.Tk()
    root.title("Football Stats App")

    global result_text, team_choice_var  # Declare global variables

    team_choice_var = tk.StringVar()

    main_label = tk.Label(root, text="Choose from the following:")
    main_label.pack()

    button_table = tk.Button(root, text="Table", command=show_table)
    button_table.pack()

    button_team_stats = tk.Button(root, text="Team Statistics", command=show_team_stats)
    button_team_stats.pack()

    button_ols = tk.Button(root, text="Overall League Statistics", command=show_ols)
    button_ols.pack()

    team_choice_label = tk.Label(root, text="Enter team choice:")
    team_choice_label.pack()

    entry_team_choice = tk.Entry(root, textvariable=team_choice_var)
    entry_team_choice.pack()

    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main_menu()
