import csv
import mysql.connector

logged_in = False

def remove_square_brackets(row):
    return [cell.strip('[]') for cell in row]

# Function to print a formatted table
def print_formatted_table(rows):
    max_widths = [max(len(cell) for cell in col) for col in zip(*rows)]

    for row in rows:
        formatted_row = [cell.ljust(width) for cell, width in zip(row, max_widths)]
        print(' | '.join(formatted_row))

# Function to display team statistics
def team(team_choice):
    team_files = {
       1: 'manchestercity.csv',
       2: 'arsenal.csv',
       3: 'newcastle.csv',
       4: 'manunited.csv',
       5: 'liverpool.csv',
       6: 'brighton.csv',
       7: 'astonvilla.csv',
       8: 'tottenham.csv',
       9: 'brentford.csv',
       10: 'fulham.csv',
       11: 'crystalpalace.csv',
       12: 'chelsea.csv',
       13: 'wolves.csv',
       14: 'westham.csv',
       15: 'bournemouth.csv',
       16: 'nott_forest.csv',
       17: 'everton.csv',
       18: 'leicester.csv',
       19: 'leeds_updated.csv',
       20: 'south.csv'
    }


    file_path = team_files.get(team_choice)

    if file_path is None:
        print("Invalid team choice.")
        return

    try:
        with open(file_path, 'r', newline='') as f:
            rows = [remove_square_brackets(row) for row in csv.reader(f)]

        print_formatted_table(rows)

    except IOError:
        print('Sorry, the app is down for maintenance')

# Function to handle user sign-up
def sign_up():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devil2006",
            database="futproject"
        )

        cursor = connection.cursor()

        print("Sign Up")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        team_files = {
            1: 'manchestercity.csv',
            2: 'arsenal.csv',
            3: 'newcastle.csv',
            4: 'manunited.csv',
            5: 'liverpool.csv',
            6: 'brighton.csv',
            7: 'astonvilla.csv',
            8: 'tottenham.csv',
            9: 'brentford.csv',
            10: 'fulham.csv',
            11: 'crystalpalace.csv',
            12: 'chelsea.csv',
            13: 'wolves.csv',
            14: 'westham.csv',
            15: 'bournemouth.csv',
            16: 'nott_forest.csv',
            17: 'everton.csv',
            18: 'leicester.csv',
            19: 'leeds_updated.csv',
            20: 'south.csv'
        }

        print("Available Teams:")
        for team_num, team_name in team_files.items():
            print(f"{team_num}. {team_name.replace('.csv', '').title()}")

        fav_team = int(input("Choose your favorite team (enter the team number): "))

        # Insert user information into the database
        query = "INSERT INTO users (username, password, favorite_team) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, fav_team))
        connection.commit()

        print("Sign up successful!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle user login
def login():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devil2006",
            database="futproject"
        )

        cursor = connection.cursor()

        print("Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password match in the database
        query = "SELECT favorite_team FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            fav_team = result[0]
            print(f"Login successful! Welcome, {username}!")
            team(fav_team)
        else:
            print("Invalid username or password.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main menu function
def menu():
    global logged_in

    while True:
        if not logged_in:
            print("Please sign up or log in to access the features.")
            choice = int(input("1. Sign Up\n2. Log In\n3. Exit\nEnter a choice: "))
            
            if choice == 1:
                sign_up()
            elif choice == 2:
                logged_in = login()  # Update logged_in status based on the login function
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print('''Choose from the following: 
                1. Table 
                2. Team Statistics 
                3. Overall League Statistics 
                4. Sign Up 
                5. Login 
                6. Exit''')

            main_choice = int(input('Enter a choice: '))

            if main_choice == 1:
                with open('Premteamtable.csv', 'r', newline='') as f:
                    rows = [remove_square_brackets(row) for row in csv.reader(f)]
                    print_formatted_table(rows)

            elif main_choice == 2:
                print('''Choose which team you want to see the statistics of:- 
    1. Man City
    2. Arsenal
    3. Newcastle
    4. Man United
    5. Liverpool
    6. Brighton 
    7. Aston Villa 
    8. Tottenham
    9. Brentford
    10. Fulham
    11. Crystal Palace
    12. Chelsea
    13. Wolves
    14. West Ham
    15. Bournemouth
    16. Nottm Forest
    17. Everton 
    18. Leicester City
    19. Leeds United
    20. Southampton''')
                team_choice = int(input('Enter team choice: '))
                team(team_choice)

            elif main_choice == 3:
                choice1 = int(input('''Choose which overall rankings 
                    1. Goals
                    2. Assists
                    3. Golden Glove: '''))
                try:
                    if choice1 == 1:
                        with open('mostgoals.csv', 'r', newline='') as f:
                            rows = [remove_square_brackets(row) for row in csv.reader(f)]
                            print_formatted_table(rows)
                    elif choice1 == 2:
                        with open('mostassists.csv', 'r', newline='') as f:
                            rows = [remove_square_brackets(row) for row in csv.reader(f)]
                            print_formatted_table(rows)
                    elif choice1 == 3:
                        with open('goldenglove.csv', 'r', newline='') as f:
                            rows = [remove_square_brackets(row) for row in csv.reader(f)]
                            print_formatted_table(rows)
                except IOError:
                    print('Sorry, the app is down for maintenance')

            elif main_choice == 4:
                sign_up()

            elif main_choice == 5:
                login()

            elif main_choice == 6:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

menu()
