from dotenv import load_dotenv, dotenv_values
from langchain_groq import ChatGroq
from tools import battery_check, weather_check, no_fly_zone_check
from memory import save_mission, show_history
import os
config = dotenv_values('.env')
api_key = config.get('GROQ_API_KEY')
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=api_key
)
def plan_mission_cli():
    print("UAV Mission Planner")
    print("===================")
    mission_type = input("Mission Type: ")
    source = input("Source: ")
    destination = input("Destination: ")
    distance_km = float(input("Distance (km): "))
    battery_percent = float(input("Battery (%): "))
    weather_condition = input("Weather Condition: ")
    wind_speed = float(input("Wind Speed (km/h): "))
    no_fly_zone = input("No Fly Zone (yes/no): ").lower() == 'yes'
    data = {
        'mission_type': mission_type,
        'source': source,
        'destination': destination,
        'distance_km': distance_km,
        'battery_percent': battery_percent,
        'weather_condition': weather_condition,
        'wind_speed': wind_speed,
        'no_fly_zone': no_fly_zone
    }
    battery_result = battery_check(distance_km, battery_percent)
    weather_result = weather_check(weather_condition, wind_speed)
    zone_result = no_fly_zone_check(no_fly_zone)
    prompt = f"""
    You are a UAV Mission Planner.
    Analyze this mission and give:
    1. Mission Summary
    2. Tool Results
    3. Final Decision
    4. Reason
    5. Recommendation
    Mission Details:
    Mission Type: {mission_type}
    Source: {source}
    Destination: {destination}
    Distance: {distance_km} km
    Battery: {battery_percent}%
    Weather: {weather_condition}
    Wind Speed: {wind_speed} km/h
    No Fly Zone: {no_fly_zone}
    Tool Results:
    - {battery_result}
    - {weather_result}
    - {zone_result}
    """
    try:
        response = llm.invoke(prompt)
        text_response = response.content
        save_mission(data, text_response)
        print("\nMission Analysis:")
        print(text_response)
    except Exception as e:
        print(f"Error: {str(e)}")
def show_history_cli():
    history = show_history()
    if history:
        print("Mission History:")
        for i, mission in enumerate(history, 1):
            print(f"\nMission {i}:")
            print(mission)
    else:
        print("No mission history found.")
if __name__ == '__main__':
    while True:
        print("\nOptions:")
        print("1. Plan a new mission")
        print("2. Show mission history")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            plan_mission_cli()
        elif choice == '2':
            show_history_cli()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
