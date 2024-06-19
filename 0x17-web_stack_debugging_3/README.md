# 0x17. Web Stack Debugging #3

## Description
This repository contains solutions and Puppet manifests for debugging Apache HTTP Server issues on a WordPress site running on a LAMP stack. The main goal is to resolve a recurring 500 Internal Server Error using `strace` for diagnostics and Puppet for automation.

## Concepts
- Web Server
- Web stack debugging

## Requirements
### General
- All files are interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests' first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

### More Info
- Install puppet-lint:
  ```bash
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
