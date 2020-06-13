from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")

def search():
     
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=10&API_KEY=FF07A34C-6362-4EFC-9638-29E28461A87D")
        api = json.loads(api_request.content)

        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealty":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        text = Label(root, text = city +" Air Quality:" + str(quality) +" " + category, background=weather_color)
        text.grid(row=2, column=0, columnspan= 2, pady=10, padx=10)
        root.configure(background=weather_color)
        

    except Exception as e:
        api = "Error..."

mylabel = Label(root, text="Zipcode")
mylabel.grid(row=0, column=0, pady=(10,0))

zip = Entry(root)
zip.grid(row=0, column=1, padx=10, pady=(10,0), stick=W+E+N+S)

mybtn = Button(root, text = "Search", command=search)
mybtn.grid(row=1, column=0, columnspan= 2, pady=10, padx=10, ipadx=100,stick=W+E+N+S)


root.mainloop()