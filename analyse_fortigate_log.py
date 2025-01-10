import re
from collections import Counter

# Path to the log file
log_file_path = "PATH_TO_LOG_FILE.log"

# regex to match IP addresses
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Read the log file and count unique IPs
def count_ip_addresses(file_path):
    with open(file_path, 'r', errors="ignore") as file:
        content = file.read()
        ip_addresses = re.findall(ip_regex, content)
        ip_count = Counter(ip_addresses)
    return ip_count

# Function to write results to a text file
def write_ip_counts_to_file(ip_count, output_path="ip_counts.txt"):
    with open(output_path, 'w') as output_file:
        for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
            output_file.write(f"{ip}: {count} mentions\n")
    print(f"Results saved to {output_path}")

# Main function
if __name__ == "__main__":
    ip_counts = count_ip_addresses(log_file_path)
    print(f"Total hitcount: {ip_counts.total()}")
    write_ip_counts_to_file(ip_counts, "OUTPUT_FILE_TO_SAVE.TXT")
