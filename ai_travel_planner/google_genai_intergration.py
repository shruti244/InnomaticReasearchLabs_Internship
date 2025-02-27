import requests

def fetch_travel_data(source, destination):
    # Mocking the call to Google GenAI API. Replace with actual API endpoint if available.
    api_url = f"https://api.genai.com/get_travel_options?source={source}&destination={destination}"
    
    # Example: Sending a request to Google GenAI API (you should replace this with real API endpoint)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()  # Assuming JSON response with travel options
        travel_options = data.get('travel_options', [])
        
        travel_info = ""
        for option in travel_options:
            travel_info += f"{option['mode']}: {option['price']} - {option['duration']}\n"
        
        return travel_info
    else:
        return "Error fetching travel data. Please try again later."
