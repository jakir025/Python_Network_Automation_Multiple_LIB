import socket

# Set a short timeout so the scan moves quickly
socket.setdefaulttimeout(0.5)

# 1. Define your target hosts (can be IPs or domain names)
hosts = [
    '192.168.184.140',
    '192.168.184.141',
    '192.168.0.10'
]

# 2. Define the port range
start_port = 20
end_port = 85

print(f"\n{'#'*50}\n Starting Multi-Host Port Scan\n{'#'*50}")

# Outer loop: Iterate through each host
for ip in hosts:
    print(f"\nScanning Host: {ip}")
    print("-" * 30)

    open_ports = 0

    # Inner loop: Iterate through the port range for the current host
    for port in range(start_port, end_port + 1):
        try:
            # Create a fresh socket for every single attempt
            DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result_of_check = DEVICE_SOCKET.connect_ex((ip, port))

            if result_of_check == 0:
                print(f"  [+] Port {port}: OPEN")
                open_ports += 1

            DEVICE_SOCKET.close()

        except socket.error:
            # Silently skip network glitches to keep output clean
            continue

    if open_ports == 0:
        print("  [-] No open ports found in this range.")

print(f"\n{'#'*50}\n Scan Complete\n{'#'*50}\n")
