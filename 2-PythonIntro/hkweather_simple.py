import requests

def gen_report():
    print("Hong Kong Weather Report")
    print(forecast['updateTime'])
    print("[Forecast]")
    print(forecast['forecastDesc'])
    print("[Outlook]")
    print(forecast['outlook'])  

try:
    language = 'tc'    # 'en'
    response = requests.get(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang={language}")
    forecast = response.json()
    gen_report()
except Exception as e:
    print("Error", e)
    
# usage 
# python hkweather.py 