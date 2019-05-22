import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("tabela").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
list_teste = sheet.get_all_values()
sheet.update_cell(3, 2, "I just wrote to a spreadsheet using Python!")
sheet.update_cell(3,4, "oi") 
sheet.print(3,4)