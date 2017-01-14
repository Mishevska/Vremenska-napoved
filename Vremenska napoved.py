import datetime
import json
import urllib.request
import tkinter as tk


class Example(tk.Frame):
    city_name = ""
    city_temp = ""
    city_sky = ""
    city_temp_min = ""
    city_temp_max = ""
    city_wind_speed = ""
    city_wind_deg = ""
    city_humidity = ""
    city_pressure = ""
    city_cloudiness = ""

    def close_window(gumb):
        root.destroy()

    def __init__(gumb, parent):
        tk.Frame.__init__(gumb, parent)

         # create a prompt, an input box, an output label,
         # and a button to do the computation
        gumb.prompt = tk.Label(gumb, text="Ime mesta:", anchor="w")
        gumb.entry = tk.Entry(gumb)
        gumb.submit = tk.Button(gumb, text="Potrdi", command = gumb.dataoutput)
        gumb.cancel = tk.Button(gumb, text="Izhod", command=gumb.close_window)
        gumb.temperature_label = tk.Label(gumb, text="Temperatura: [\xb0C]")
        gumb.data_output = tk.Label(gumb, text="")
        gumb.sky_label = tk.Label(gumb, text="Napovedovanje: ")
        gumb.sky_output = tk.Label(gumb, text="")
        gumb.temp_min_label = tk.Label(gumb, text="Minimalna temperatura [\xb0C]: ")
        gumb.temp_min_output = tk.Label(gumb, text="")
        gumb.temp_max_label = tk.Label(gumb, text="Maksimalna temperatura [\xb0C]: ")
        gumb.temp_max_output = tk.Label(gumb, text="")
        gumb.wind_speed_label = tk.Label(gumb, text="Hitrost vetra [m/s]: ")
        gumb.wind_speed_output = tk.Label(gumb, text="")
        gumb.humidity_label = tk.Label(gumb, text="Vlažnost [%]: ")
        gumb.humidity_output = tk.Label(gumb, text="")
        gumb.pressure_label = tk.Label(gumb, text="Zračni tlak [hPa]: ")
        gumb.pressure_output = tk.Label(gumb, text="")
        gumb.cloudiness_label = tk.Label(gumb, text="Oblačnost [%]: ")
        gumb.cloudiness_output = tk.Label(gumb, text="")


    #   lay the widgets out on the screen.

        gumb.prompt.grid(row=0, column=0)
        gumb.entry.grid(row=0, column=1, padx=20)

        gumb.submit.grid(row=2, column=0)
        gumb.cancel.grid(row=2, column=1)

        gumb.temperature_label.grid(row=3, column=0)
        gumb.sky_label.grid(row=4, column=0)
        gumb.temp_min_label.grid(row=5, column=0)
        gumb.temp_max_label.grid(row=6, column=0)
        gumb.wind_speed_label.grid(row=7, column=0)
        gumb.humidity_label.grid(row=8, column=0)
        gumb.pressure_label.grid(row=9, column=0)
        gumb.cloudiness_label.grid(row=10, column=0)

        gumb.data_output.grid(row=3, column=1)
        gumb.sky_output.grid(row=4, column=1)
        gumb.temp_min_output.grid(row=5, column=1)
        gumb.temp_max_output.grid(row=6, column=1)
        gumb.wind_speed_output.grid(row=7, column=1)
        gumb.humidity_output.grid(row=8, column=1)
        gumb.pressure_output.grid(row=9, column=1)
        gumb.cloudiness_output.grid(row=10, column=1)

    def url_builder(city_name):
        user_api = 'a3e3369becb16ffd2d52f59d3ace024c'  # Obtain yours form: http://openweathermap.org/
        unit = 'metric'
        api = 'http://api.openweathermap.org/data/2.5/weather?q='  # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

        full_api_url = api + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + user_api
        return full_api_url

    def data_fetch(full_api_url):
        url = urllib.request.urlopen(full_api_url)
        output = url.read().decode('utf-8')
        raw_api_dict = json.loads(output)
        url.close()
        return raw_api_dict

    def data_organizer(raw_data):
        main = raw_data.get('main')
        sys = raw_data.get('sys')
        data = dict(
            city=raw_data.get('name'),
            country=sys.get('country'),
            temp=main.get('temp'),
            temp_max=main.get('temp_max'),
            temp_min=main.get('temp_min'),
            humidity=main.get('humidity'),
            pressure=main.get('pressure'),
            sky=raw_data['weather'][0]['main'],
            wind=raw_data.get('wind').get('speed'),
            wind_deg=raw_data.get('deg'),
            cloudiness=raw_data.get('clouds').get('all')
        )
        return data

    def data_output(data):
        #m_symbol = '\xb0' + 'C'
        global city_temp
        global city_sky
        global city_temp_min
        global city_temp_max
        global city_wind_speed
        global city_wind_deg
        global city_humidity
        global city_pressure
        global city_cloudiness

        city_temp=data['temp']
        city_sky = data['sky']
        city_temp_min = data['temp_min']
        city_temp_max = data['temp_max']
        city_wind_speed = data['wind']
        city_wind_deg = data['wind_deg']
        city_humidity = data['humidity']
        city_pressure = data['pressure']
        city_cloudiness = data['cloudiness']

    def dataoutput(gumb):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            city_name = gumb.entry.get()

            Example.data_output(Example.data_organizer(Example.data_fetch(Example.url_builder(city_name))))
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        gumb.data_output.configure(text=city_temp, fg="blue")
        gumb.sky_output.configure(text=city_sky, fg="blue")
        gumb.temp_min_output.configure(text=city_temp_min, fg="blue")
        gumb.temp_max_output.configure(text=city_temp_max, fg="blue")
        gumb.wind_speed_output.configure(text=city_wind_speed, fg="blue")
        gumb.humidity_output.configure(text=city_humidity, fg="blue")
        gumb.pressure_output.configure(text=city_pressure, fg="blue")
        gumb.cloudiness_output.configure(text=city_cloudiness, fg="blue")

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    #Example(root).pack(fill="both", expand=True)
    Example(root).grid(rowspan = 11, columnspan=2, sticky='SE')

    root.mainloop()