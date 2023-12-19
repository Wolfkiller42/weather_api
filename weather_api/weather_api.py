import requests  # Importing the requests library to perform HTTP requests

API_KEY = '7f4cf7ecce5beacbc914f6f8d87f90af'  # API key used for accessing OpenWeatherMap API

# Function to get weather information using ZIP code
def get_weather_by_zip():
    while True:
        zip_code = input("Enter the ZIP code for the location you want weather information about: ")  # User input for ZIP code
        zip_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}'  # API URL with the entered ZIP code
        location_info = requests.get(zip_url).json()  # Sending a request to obtain location info based on ZIP code

        if 'lat' in location_info:  # If latitude info exists in the response
            latitude, longitude = location_info['lat'], location_info['lon']  # Extracting latitude and longitude
            weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial').json()  # Getting weather info based on latitude and longitude
            display_weather_info(weather_data)  # Displaying weather info
            break  # Exit the loop
        else:
            print("Invalid ZIP code. Please try again.")  # Prompting for a valid ZIP code

# Function to get weather information using city name
def get_weather_by_city():
    while True:
        city_name = input("Enter Valid City Location: ")  # User input for city name
        state_code = input("Enter State Code(Abbreviation for state): ")  # User input for state code
        city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={API_KEY}'  # API URL with the entered city and state info
        location_info = requests.get(city_url).json()  # Sending a request to obtain location info based on city and state

        if location_info:  # If location info exists
            latitude, longitude = location_info[0]['lat'], location_info[0]['lon']  # Extracting latitude and longitude
            weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial').json()  # Getting weather info based on latitude and longitude
            display_weather_info(weather_data)  # Displaying weather info
            break  # Exit the loop
        else:
            print("City or State code not found... Please Try Again")  # Prompting for valid city or state code

# Function to display weather information
def display_weather_info(weather_data):
    if 'name' in weather_data:  # If 'name' info exists in the weather data
        print(f"\nLocation: {weather_data['name']}")  # Printing location name
        print(f"Today's max temperature: {weather_data['main']['temp_max']}°F, Feels like: {weather_data['main']['feels_like']}°F")  # Printing temperature info
        print(f"Weather: {weather_data['weather'][0]['description']}")  # Printing weather description
    else:
        print("Weather Information For Location Not Found :(")  # If weather data not found

# Function to display welcome message
def welcome_message():
    print("Welcome, This is a Weather Checker")  # Displaying a welcome message
    print("This Program is to Help Check The Weather For Various places in the US")  # Describing the program's purpose
    print('______________________________________________________________________')  # Separating lines
    print('                                                                       ')  # Adding some space

# Function to select search mode (ZIP code or city name)
def search_mode_selection():
    return input("Please Input '1' to search by ZIP code or '2' to search by City name: ").lower()  # Getting user input for search mode and converting it to lowercase

# Main function to run the program
def main():
    welcome_message()  # Displaying the welcome message
    while True:
        search_mode = search_mode_selection()  # Getting user's search mode choice

        if search_mode == "1":  # If user chooses search by ZIP code
            get_weather_by_zip()  # Calling function to get weather by ZIP code
            break  # Exit the loop
        elif search_mode == "2":  # If user chooses search by city name
            get_weather_by_city()  # Calling function to get weather by city name
            break  # Exit the loop
        else:
            print("Invalid input. Please enter 'zip' or 'name', or press q to exit")  # Prompting for valid input
            if search_mode == "q":  # If user wants to exit
                print("Now exiting program. Goodbye :)")  # Displaying exit message
                break  # Exit the loop

if __name__ == "__main__":
    main()  # Starting the main function