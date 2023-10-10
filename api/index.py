import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            ip_info = self.get_public_ip_info()
            json_info = self.get_public_ip_info_json()
            response = self.create_box(ip_info) + "\n\nRaw JSON:\n" + json_info
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode())

    def get_public_ip_info(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ip_info = response.json()

            if ip_info["status"] == "success":
                result = "Public IP Address Information:\n"
                result += f"IP Address: {ip_info['query']}\n"
                result += f"City: {ip_info['city']}\n"
                result += f"Region: {ip_info['regionName']}\n"
                result += f"Country: {ip_info['country']}\n"
                result += f"ISP: {ip_info['isp']}\n"
                return result
            else:
                return "Failed to retrieve IP information."

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def get_public_ip_info_json(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ip_info = response.json()

            if ip_info["status"] == "success":
                return json.dumps(ip_info, indent=2)
            else:
                return json.dumps({"error": "Failed to retrieve IP information."}, indent=2)

        except requests.exceptions.RequestException as e:
            return json.dumps({"error": f"Error: {e}"}, indent=2)

    def create_box(self, text):
        lines = text.split('\n')
        max_len = max(len(line) for line in lines)
        box = f'/' * (max_len + 4) + '\n'
        for line in lines:
            box += f'// {line} //\n'
        box += f'/' * (max_len + 4)
        return box

def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, handler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_vercel_server()
