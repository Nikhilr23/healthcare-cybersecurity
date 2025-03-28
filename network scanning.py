import os
import subprocess

def scan_network(target_ip):
    print(f"Scanning {target_ip} for open ports...")
    try:
        result = subprocess.run(["nmap", "-sV", target_ip], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Error: Nmap is not installed. Please install it and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = os.getenv("TARGET_IP", "127.0.0.1")  # Use environment variable or default to localhost
    scan_network(target)
