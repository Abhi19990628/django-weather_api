from django.shortcuts import render
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=718bfb40fec2a75aee7767677f367613').read()
                                        #https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        


        # data for variable list_of_data
        temp_celsius = int(list_of_data['main']['temp']) - 273.15
        data = {
    'city': city,
    "country_code": str(list_of_data['sys']['country']),
    "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
    "temp": str(round(temp_celsius, 2)) + '°C',  # Formatting temperature to 2 decimal places and appending '°C'
    "pressure": str(list_of_data['main']['pressure']),
    "humidity": str(list_of_data['main']['humidity']),
}
        # data = {
        #     'city': city,
        #     "country_code": str(list_of_data['sys']['country']),
        #     "coordinate": str(list_of_data['coord']['lon']) + ' '
        #                 + str(list_of_data['coord']['lat']),
        #     "temp": ((int(list_of_data['main']['temp'])-273)+str('C')),
            

        #     "pressure" : str(list_of_data['main']['pressure']),
        #     "humidity": str(list_of_data['main']['humidity']),
        # }
        print(data)
    else:
        data ={}
    return render(request, "index.html", data)