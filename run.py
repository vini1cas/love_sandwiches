import gspread
from google.oauth2.service_account import Credentials
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
            print(Data is valid!)
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
                f'Exactly 6 values required. You provided: {len(values})'
            )
    except ValueErroras e:
        print(f'Invalid data as {e}. Try again')
        return False
    
    return True

def update_sales_worksheet(data):
    """
    Upodate sales worksheet by adding another row to it with the data entered by the user
    """
    print('Updating sales worksheet...')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet has been successfully updated!')

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)



