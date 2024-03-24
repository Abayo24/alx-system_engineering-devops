# Project: 0x0B-SSH

## Table of Contents
- [Description](#description)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Use a private key](#0-use-a-private-key)
  - [1. Create an SSH key pair](#1-create-an-ssh-key-pair)
  - [2. Client configuration file](#2-client-configuration-file)
  - [3. Let me in!](#3-let-me-in!)
- [Copyright](#copyright)

## Description
This project focuses on understanding SSH (Secure Shell) and its application in connecting to remote servers securely using RSA key pairs. It involves creating SSH key pairs, configuring SSH client, and connecting to remote servers using private keys.

## Background Context
This project involves connecting to a remote server via SSH using RSA key pairs instead of passwords. The project includes tasks such as creating SSH keys, configuring the SSH client, and granting access to the server.

## Resources
- [What is a (physical) server - text](#)
- [What is a (physical) server - video](#)
- [SSH essentials](#)
- [SSH Config File](#)
- [Public Key Authentication for SSH](#)
- [How Secure Shell Works](#)
- [SSH Crash Course](#)
- [Understanding the SSH Encryption and Connection Process](#)
- [Secure Shell Wiki](#)
- [IETF RFC 4251 (Description of the SSH Protocol)](#)
- [Internet Engineering Task Force](#)
- [Request for Comments](#)
- `man` or `help`:
  - ssh
  - ssh-keygen
  - env

## Learning Objectives
Upon completing this project, you should be able to explain:
- What is a server?
- Where servers usually live?
- What is SSH?
- How to create an SSH RSA key pair?
- How to connect to a remote host using an SSH RSA key pair?
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 20.04 LTS
- All files must end with a new line
- A `README.md` file is mandatory
- Bash scripts must be executable
- The first line of all Bash scripts must be `#!/usr/bin/env bash`
- The second line of all Bash scripts must be a comment explaining the script's purpose

## Tasks

### 0. Use a private key
Write a Bash script to connect to the server using SSH and the private key `~/.ssh/school` with the user `ubuntu`.

- Requirements:
  - Use only ssh single-character flags
  - Cannot use `-l`

### 1. Create an SSH key pair
Write a Bash script to create an RSA key pair.

- Requirements:
  - Private key must be named `school`
  - Number of bits in the key must be 4096
  - Key must be protected by the passphrase `betty`

### 2. Client configuration file
Configure the SSH client configuration file to use the private key `~/.ssh/school` and refuse password authentication.

### 3. Let me in!
Add the provided SSH public key to the server to allow connection using the `ubuntu` user.

## Copyright
© 2024 ALX, All rights reserved.

