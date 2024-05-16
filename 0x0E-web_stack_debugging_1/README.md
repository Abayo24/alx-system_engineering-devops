# 0x0E. Web stack debugging #1

## Description
This repository contains a Bash script named `0-nginx_likes_port_80` that fixes an issue with an Nginx installation on an Ubuntu container not listening on port 80. The script ensures that Nginx is running and listening on port 80 of all the server’s active IPv4 IPs.

## Tasks
- **0. Nginx likes port 80:** The script configures the server to have Nginx running and listening on port 80 of all active IPv4 IPs.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 20.04 LTS
- All files ending with a new line
- Mandatory `README.md` file at the root of the folder
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- First line of all Bash scripts should be `#!/usr/bin/env bash`
- Second line of all Bash scripts should be a comment explaining the script's purpose
- Not allowed to use `wget`

## Usage
To use the script `0-nginx_likes_port_80`, execute it as follows:
./0-nginx_likes_port_80

## Author
Written by Abayo

Project Structure
Copy code
0x0E-web_stack_debugging_1/
│
├── 0-nginx_likes_port_80
└── README.md
References
For further information on Nginx and web stack debugging, refer to:

Nginx Documentation
Web Stack Debugging
