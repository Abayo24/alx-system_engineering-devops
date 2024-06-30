# 0x1B. Web Stack Debugging #4

## Overview
This project focuses on debugging and optimizing a web server setup that uses Nginx. We aim to test the server's performance under load and address issues to achieve zero failed requests.

## Requirements
- All files are interpreted on Ubuntu 14.04 LTS.
- Each file ends with a new line.
- The project root folder contains a `README.md` file.
- Puppet manifests pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests run without error.
- The first line of each Puppet manifest is a comment explaining the manifest.
- Puppet manifests have a `.pp` extension.
- Files are checked with Puppet v3.4.

## Setup Instructions

### Install `puppet-lint`
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

