import requests
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(prog='python hkweather.py',
    description='Hong Kong Weather Forecast香港天氣預報',
    formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument("-l", "--language", help="Language (en, tc)")

args = vars(parser.parse_args())

def gen_report():
    print("Hong Kong Weather Report")
    print(forecast['updateTime'])
    print("[Forecast]")
    print(forecast['forecastDesc'])
    print("[Outlook]")
    print(forecast['outlook'])  

try:
    language = args["language"]    
    response = requests.get(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang={language}")
    forecast = response.json()
    gen_report()
except:
    print("usage: python hkweather.py [-h] [-l LANGUAGE]")
    
# usage 
# python hkweather.py -l tc
# python hkweather.py -l en