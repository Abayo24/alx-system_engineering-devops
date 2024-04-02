Project: 0x0F-load_balancer
Overview
This project focuses on setting up and configuring load balancers for redundancy and scalability in a web server environment. The main tasks involve configuring Nginx with custom HTTP response headers and setting up HAProxy to distribute traffic among multiple web servers.

Curriculum
Average: 96.12%
Project Deadline: Apr 3, 2024 6:00 AM
Tasks
Double the number of webservers

Configure Nginx to add a custom HTTP response header (X-Served-By) on web-01 and web-02.
Script: 0-custom_http_response_header
Install your load balancer

Install and configure HAProxy on lb-01 server to distribute traffic to web-01 and web-02 using a round-robin algorithm.
Ensure HAProxy can be managed via an init script.
Script: 1-install_load_balancer
Add a custom HTTP header with Puppet (Advanced)

Use Puppet to automate the creation of a custom HTTP header (X-Served-By) with the hostname of the Nginx server.
Script: 2-puppet_custom_http_response_header.pp
Resources
Introduction to load-balancing and HAproxy
HTTP header
Debian/Ubuntu HAProxy packages
General Requirements
Allowed editors: vi, vim, emacs
All files interpreted on Ubuntu 16.04 LTS
Files should end with a new line
Bash script files must be executable
Bash scripts must pass Shellcheck (version 0.3.7) without any error
First line of all Bash scripts: #!/usr/bin/env bash
Second line of all Bash scripts: comment explaining the script's purpose
Contact Information
For any inquiries or assistance regarding this project, please contact ALX.

License
© 2024 ALX. All rights reserved.
