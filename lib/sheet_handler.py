import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
# use creds to create a client to interact with the Google Drive API
class sheetHandler():
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('secrets/claves.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(settings.spread_sheet)


    def load_sheet(self, sheet_name):
        return self.sheet.worksheet(sheet_name).get_all_records()
    
    def load_last_sheet(self):
        last_sheet = self.sheet.worksheets()[-1]
        return last_sheet.get_all_records()
    


#for sheet in spreed_sheet:
#    print(sheet.title)


# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)S
