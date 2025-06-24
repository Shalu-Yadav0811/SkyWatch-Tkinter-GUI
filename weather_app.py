from tkinter import *
from tkinter import ttk, messagebox
import requests
import datetime

API_KEY = "1e7404d83a6d0c51e8321e1aedae4fa8"

def detect_location():
    try:
        ip_data = requests.get("https://ipinfo.io").json()
        return ip_data.get('city', '')
    except Exception as e:
        print("Location detection failed:", e)
        return ""

def get_report():
    city = city_name.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please select or detect a city/state.")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("City Not Found", f"{data.get('message', 'Invalid city')}")
            return

        weather_main = data['weather'][0]['main']
        weather_desc = data['weather'][0]['description']
        temp = round(data['main']['temp'] - 273.15, 2)
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        time_now = datetime.datetime.now().strftime("%d %b %Y | %I:%M %p")

        weather_climate_label1.config(text=weather_main)
        weather_description_label1.config(text=weather_desc)
        temp_label1.config(text=f"{temp} °C")
        humidity_label1.config(text=f"{humidity}%")
        pressure_label1.config(text=f"{pressure} mb")
        time_label.config(text=f"Updated: {time_now}")

    except Exception as e:
        messagebox.showerror("Connection Error", f"Error: {str(e)}")

def toggle_dark_mode():
    is_dark = dark_mode.get()
    bg_color = "#2c3e50" if is_dark else "#3498db"
    fg_color = "#ecf0f1" if is_dark else "white"

    win.config(bg=bg_color)
    name_label.config(bg=bg_color, fg=fg_color)
    time_label.config(bg=bg_color, fg=fg_color)
    for widget in output_labels:
        widget.config(bg=bg_color, fg=fg_color)
    dark_mode_checkbox.config(bg=bg_color, fg=fg_color, activebackground=bg_color)

def setup_gui():
    global win, city_name, weather_climate_label1, weather_description_label1
    global temp_label1, humidity_label1, pressure_label1, time_label, name_label
    global output_labels, dark_mode, dark_mode_checkbox

    win = Tk()
    win.title("Weather Forecast App")
    win.config(background="#3498db")
    win.geometry('500x600')

    name_label = Label(win, text="Weather App", font=("Roboto", 26, "bold"), bg="#3498db", fg="white")
    name_label.place(x=25, y=20, height=50, width=450)

    time_label = Label(win, text="", font=("Roboto", 12), bg="#3498db", fg="white")
    time_label.place(x=150, y=70)

    city_name = StringVar()
    indian_states = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
        "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ]
    state_combobox = ttk.Combobox(win, values=indian_states, font=("Roboto", 20), textvariable=city_name, state="readonly")
    state_combobox.place(x=50, y=100, height=50, width=400)

    dark_mode = BooleanVar()
    dark_mode_checkbox = Checkbutton(win, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode,
                                     bg="#3498db", fg="white", font=("Roboto", 10), activebackground="#3498db")
    dark_mode_checkbox.place(x=380, y=10)

    auto_city = detect_location()
    if auto_city:
        city_name.set(auto_city)
        get_report()

    Button(win, text="Search", font=("Roboto", 18), bg="Red", fg="white", command=get_report).place(x=70, y=170, height=50, width=360)

    output_labels = []
    def create_label_pair(label_text, y_pos):
        label = Label(win, text=label_text, font=("Roboto", 16), bg="#3498db", fg="white")
        label.place(x=25, y=y_pos, height=40, width=210)
        value_label = Label(win, text="N/A", font=("Roboto", 16), bg="#3498db", fg="white")
        value_label.place(x=245, y=y_pos, height=40, width=210)
        output_labels.extend([label, value_label])
        return value_label

    weather_climate_label1 = create_label_pair("Weather Climate:", 250)
    weather_description_label1 = create_label_pair("Description:", 300)
    temp_label1 = create_label_pair("Temperature:", 350)
    humidity_label1 = create_label_pair("Humidity:", 400)
    pressure_label1 = create_label_pair("Pressure:", 450)

if __name__ == "__main__":
    setup_gui()
    win.mainloop()
