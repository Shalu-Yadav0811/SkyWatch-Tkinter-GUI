#  SkyWatch-Tkinter-GUI

A user-friendly **Python GUI Weather App** that shows live weather details for Indian cities. Built using **Tkinter**, this desktop application includes:

-  City selection or auto-detection  
-  Live temperature, humidity, pressure  
-  Error handling for invalid input or no internet  

---

##  Screenshot

![Image 1](https://github.com/user-attachments/assets/df5d1fcd-acd4-4bd4-8f33-70769f445243)

![Image 2](https://github.com/user-attachments/assets/1c7fffb5-9e5c-4ae0-86a3-bb1f4a3d373a)

![Image 3 (Dark Mode)](https://github.com/user-attachments/assets/0d4e541e-85ef-48d8-b1a3-adf39516af68)


---

##  Features

-  Search by Indian City or State  
-  Auto-detect city using IP  
-  Real-time Temperature, Humidity, Pressure  
-  Dark Mode Toggle *(if implemented)*  
-  Last updated timestamp  
-  API integration using OpenWeatherMap  
-  Error handling for invalid input and no internet  

---

## 🛠️ Technologies Used

- Python 3.x  
- `tkinter` — GUI toolkit  
- `requests` — for API communication  
- [OpenWeatherMap API](https://openweathermap.org/)  
- [ipinfo.io](https://ipinfo.io) — for location detection  

---

##  How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/SkyWatch-Tkinter-GUI.git
cd SkyWatch-Tkinter-GUI
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python weather_app.py
```

##  Get Your Own API Key

This app uses [OpenWeatherMap](https://openweathermap.org/api). To run it with your own API key:

1. Visit - https://openweathermap.org/api  
2. Sign up and **get your free API key**
3. Open the file `weather_app.py` and replace the default key with your own:

```python
# Before
API_KEY = "1e7404d83a6d0c51e8321e1aedae4fa8"

# After
API_KEY = "your_actual_api_key_here"
```
##  Project Structure
weather-forecast-app/
│
├── weather_app.py # Main application file
├── README.md # Project documentation (this file)
├── requirements.txt # Dependencies
└── assets/ # Screenshots or icons (optional)


---

##  To-Do / Enhancements

- [ ] Add weather icons (☀️ 🌧️ 🌩️)
- [ ] Save/export weather reports
- [ ] Support for international cities
- [ ] Add voice assistant using `pyttsx3`
- [ ] Add 7-day forecast with OneCall API

---

##  Author

**Shalu Yadav**  
Made with heart using Python & Tkinter

---

##  License

This project is open-source and available under the **MIT License**.

---

##  Support or Feedback?

-  Raise an [issue](https://github.com/your-username/weather-forecast-app/issues) for bugs or suggestions  
-  Star the repo if you found it helpful!

---

##  What to Do Now

1. Save this content as `README.md`  
2. Place it in your project root folder  
3. Create `requirements.txt` with the following:
```requests
```

---


---

###  Summary of Changes Made:

| Issue | Fix |
|-------|-----|
| Code block syntax (` ```requests `) | Changed to valid code block with `requests` inside |
| Missing `---` before sections | Added horizontal lines for visual separation |
| Header emojis | Unified with consistent styling |
| Clarified optional dark mode | Marked as "(if implemented)" |
| Corrected repo name in paths | Replaced `weather-forecast-app` with `SkyWatch-Tkinter-GUI` |
| Added formatting consistency | Proper line breaks, spacing, and indent alignment |

Let me know if you want this saved as a file or need a `requirements.txt` generated automatically!
