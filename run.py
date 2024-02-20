import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#sales = SHEET.worksheet('sales')
#data =sales.get_all_values()

#print(data)

def get_sales_data():
    """
    Function to get sales data input from the user
    """
    while True:
        print("Please enter sales date from the last market day.\n Data should be six numbers separated by commas\n Example 10, 20, 30, 40 , 50")

        data_str = input("Please enter your data here:\n")
        print(f'The data provided is {data_str}')

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break
    
    return sales_data

def validate_data(values):
    """
    Converts al string values into ints.
    Raises VlaueError if that can't done or if there aren't exactly 6 values
    """
    try:
        [int(values for value in values)]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required. You provided: {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data as {e}. Try again')
        return False
    
    return True

#def update_sales_worksheet(data):
    """
    Update sales worksheet by adding another row to it with the data entered by the user
    """
    print('Updating sales worksheet...')
    sales_worksheet = SHEET.worksheet('sales')
    sales_row = sales_worksheet.append_row(data)
    print('Sales worksheet has been successfully updated!')

def calculate_surplus(sales_data):
    """
    Calculate surplus stock after each trading day. 
    Positive values refer to left-over stock while negative values refer to stock that had to be made on the day 
    """
    global sales_row
    stock = SHEET.worksheet('stock').get_all_values
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data

def update_worksheet(data, worksheet):
    """
    Updates the respective worksheet every time data is entered and the function is called
    """
    print(f'Updating {worksheet} worksheet...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet has been successfully updated!')

#def update_surplus_worksheet(data):
    """
    Function to append the surplus data to the surplus tab on Google Sheets
    print('Updating surplus worksheet...')
    surplus_worksheet = SHEET.worksheet('surplus')
    new_stock_row = surplus_worksheet.append_row('surplus_data')
    print("Surplus data has been succesfully updated!")
    """

def get_last_sales_entries():
    """
    Gets sales data per market from the last 5 trading days
    """
    sales = SHEET.worksheet('sales')
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns

def average_stock(data):
    """
    Calculate average stock to define stock for the next trading day
    """
    print('Calculating stock data...')
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num - average * 1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data

def main():
    """
    Main function to run all other functions in the program
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus(sales_data)
    update_worksheet(new_surplus_data, 'surplus')
    sales_columns = get_last_sales_entries()
    stock_data = average_stock(sales_columns)
    update_worksheet(stock_data, 'stock')

main()




