# Weather Project

A Flask web application and supporting scripts to fetch and display real-time weather data for a given city and country code using the OpenWeatherMap API.

## Features
- Enter a city and country code to get current weather information (climate and temperature in Celsius).
- Uses OpenWeatherMap Geocoding API to fetch latitude and longitude.
- Secure API key management using environment variables (`.env`).
- Includes standalone scripts for direct API data fetching and demonstration.

## Project Structure
```
Weather/
├── WEATHER/
│   ├── web/
│   │   ├── app.py            # Flask web application
│   │   └── templates/
│   │       └── weather.html  # HTML template for the web app
│   ├── weatherApiData.py     # Script: fetches weather by lat/lon
│   ├── geoApiData.py         # Script: fetches geo data by city/country
│   ├── combinedApiData.py    # Script: combines geo and weather fetch
│   └── ...
├── .env                      # Environment variables (not committed)
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

## Setup Instructions
1. **Clone the repository and navigate to the project directory.**
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your `.env` file in the root directory:**
   ```env
   OPENWEATHER_API_KEY=your_openweathermap_api_key_here
   ```

## Running the Web Application
Navigate to the `WEATHER/web` directory and run:
```bash
python app.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Using the Standalone Scripts
- **weatherApiData.py**: Fetches weather data for preset coordinates.
- **geoApiData.py**: Fetches latitude and longitude for a preset city/country.
- **combinedApiData.py**: Prompts for city/country, fetches geo and weather data.

Run any script with:
```bash
python <script_name.py>
```

## Security Notes
- **Never commit your `.env` file or API keys to version control.**
- The `.gitignore` is set up to exclude `.env` and other sensitive files.
- If you believe your API key has been exposed, regenerate it from the OpenWeatherMap dashboard.

## Requirements
See `requirements.txt` for all dependencies:
- flask
- requests
- python-dotenv

---
Feel free to extend the project or adapt the scripts for your own use!
