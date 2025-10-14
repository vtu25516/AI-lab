def dfs_weather_forecast(transitions, current_weather, days, path, all_paths):
    if days == 0:
        all_paths.append(path[:])
        return

    for next_weather in transitions.get(current_weather, []):
        path.append(next_weather)
        dfs_weather_forecast(transitions, next_weather, days - 1, path, all_paths)
        path.pop()  # backtrack

# Define transition rules between weather conditions
weather_transitions = {
    "Sunny": ["Sunny", "Cloudy", "Rainy"],
    "Cloudy": ["Sunny", "Rainy"],
    "Rainy": ["Cloudy", "Sunny"]
}

# Forecast parameters
start_weather = "Sunny"
forecast_days = 3
all_forecasts = []

# DFS traversal
dfs_weather_forecast(weather_transitions, start_weather, forecast_days, [start_weather], all_forecasts)

# Print all possible forecast paths
print(f"All possible weather forecasts for {forecast_days} days starting from {start_weather}:")
for path in all_forecasts:
    print(" -> ".join(path))
