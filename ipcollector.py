# CNIT-381 Fa2023
# Brennan Kocovsky // Alec Pennings

import requests

# Main function to contact API and return JSON
def ip_collector():
    url = "http://ip-api.com/json/"

    try:
        apiReturn = requests.get(url) # Define variable as the return of our API URL into the function
        ip_info = apiReturn.json() # Raw JSON of the IP info returned

        # If successful, start parsing raw JSON into human readable format
        if ip_info["status"] == "success":
            print("Public IP Address Information:")
            print(f"IP Address: {ip_info['query']}")
            print(f"City: {ip_info['city']}")
            print(f"Region: {ip_info['regionName']}")
            print(f"Country: {ip_info['country']}")
            print(f"ISP: {ip_info['isp']}")

        # If unsuccessful, print error message
        else:
            print("Failed to retrieve IP information.")

    # Except statement to print failure if overall "try" fails
    except requests.exceptions.RequestException as fail:
        print(f"Error: {fail}")

# High-level function call for overall script
if __name__ == "__main__":
    ip_collector()
