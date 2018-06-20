#Written by Michael Hernandez
#http://www.github.com/aonbyte

import requests
from sys import exit
url = 'https://sellercentral.amazon.com/fba/profitabilitycalculator/productmatches?searchKey='

def request_dimensions(ASIN, url= url):
    try:
        url = url + ASIN
        response = requests.get(url)
        response = response.json()['data'][0]
        weight = response['weight']
        width = response['width']
        height = response['height']
        length = response['length']
        volume = (length * width * height) / 1728
        volume = round(volume,3)
        storage_fee = 0.64 * volume
        data = {'height': height, 'width': width, 'length': length, 'weight': weight, 'volume': volume, 'storage_fee': storage_fee}
    except:
        data = {'height': 'error', 'width': 'error', 'length': 'error', 'weight': 'error'}
    return data

while True:
    entry = input("ASIN: ")
    if entry[0] != 'B':
        exit()
    data = request_dimensions(entry)
    print('Weight : ' + str(data['weight']) + ' Pounds / ' + ("%.2f" % (data['weight'] / 16)) + ' Ounces,  Length: ' + str(data['length']) + ' in., Width: ' + str(data['width']) + ' in., Height: ' + str(data['height']) + ' in.')
    print('Volume: ' + str(data['volume']) + ' Cubic Feet')
    print('Storage Fee: $' + str(data['storage_fee']))
