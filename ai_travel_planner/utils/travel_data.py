# Mock function to simulate fetching data for travel modes
def get_mocked_travel_data(source, destination):
    # This is just a mock response, replace with actual API call if needed
    travel_data = [
        {"mode": "Cab", "price": "$50", "duration": "1 hour"},
        {"mode": "Train", "price": "$20", "duration": "3 hours"},
        {"mode": "Bus", "price": "$15", "duration": "4 hours"},
        {"mode": "Flight", "price": "$200", "duration": "1.5 hours"},
    ]
    
    return travel_data
