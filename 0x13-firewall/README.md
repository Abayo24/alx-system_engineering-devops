# 0x13. Firewall

## Project Overview

This project involves installing and configuring the UFW firewall on a server (`web-01`) to enhance its security by blocking all incoming traffic except for specific ports. The task requires the application of firewall rules that allow incoming traffic on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS), while denying all other incoming traffic.

## Requirements

- Install the UFW firewall on `web-01`.
- Configure UFW to block all incoming traffic except for TCP ports:
  - 22 (SSH)
  - 80 (HTTP)
  - 443 (HTTPS)
- Share the UFW commands used in an answer file.

## UFW Commands Used

The following commands were used to configure UFW on `web-01`:

```bash
# Allow SSH
sudo ufw allow 22/tcp

# Allow HTTP
sudo ufw allow 80/tcp

# Allow HTTPS
sudo ufw allow 443/tcp

# Block all other incoming traffic
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Enable UFW
sudo ufw enable

