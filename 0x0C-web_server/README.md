# ALX System Engineering & DevOps - Web Server

## Introduction
This repository contains scripts and configurations for setting up a web server using Nginx on Ubuntu 16.04 LTS. The project covers various tasks related to configuring the web server, transferring files, setting up domain names, redirection, and custom error pages.

## Background Context
In this project, tasks are aimed at configuring a web server and automating tasks using Bash scripting. The project emphasizes understanding web server concepts, automating configurations, and adhering to best practices.

## Learning Objectives
By completing this project, you will gain knowledge about:
- The main role of a web server
- Child processes and their significance
- HTTP requests and their types
- DNS fundamentals and record types
- Automating server configurations using Bash scripting

## Tasks
1. **Transfer a file to your server**
    - Write a Bash script to transfer a file using `scp`.
    - The script accepts parameters for file path, server IP, username, and SSH private key.

2. **Install Nginx web server**
    - Write a Bash script to install Nginx on a server.
    - Nginx should listen on port 80 and return "Hello World!" when queried at the root.

3. **Setup a domain name**
    - Configure DNS records with an A entry to point the domain to the server's IP address.
    - Provide the domain name obtained from .TECH Domains.

4. **Redirection**
    - Configure Nginx to redirect `/redirect_me` to another page with a "301 Moved Permanently" status.

5. **Not found page 404**
    - Configure Nginx to have a custom 404 page containing the string "Ceci n'est pas une page".

## Requirements
- Scripts are written in Bash and executed on Ubuntu 16.04 LTS.
- Scripts should pass Shellcheck without any errors.
- Use `#!/usr/bin/env bash` as the first line in all Bash scripts.
- Ensure all files end with a new line.
- Use proper comments to explain the purpose of each script.

## Additional Resources
- [How the web works](#)
- [Nginx Documentation](#)
- [DNS Fundamentals](#)

## Author
This repository is authored by ALX.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

