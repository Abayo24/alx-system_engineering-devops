# Project: 0x0A-configuration_management

## Description
This project focuses on configuration management using Puppet. Puppet is a powerful tool for automating infrastructure management and ensuring consistency across systems. Through a series of tasks, we will use Puppet to create files, install packages, and execute commands on target systems.

## Background Context
During my time at SlideShare, I worked on an auto-remediation tool called Skynet, which monitored, scaled, and fixed Cloud infrastructure. I used Puppet to restore our infrastructure after a critical issue occurred, demonstrating the importance of configuration management tools in maintaining system reliability and efficiency.

## Resources
- [Intro to Configuration Management](https://www.ibm.com/cloud/learn/configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/latest/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/docs/puppet/latest/lang_intro.html)
- [Puppet lint](https://puppet.com/docs/puppet/latest/style_guide.html)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Requirements
- Ubuntu 20.04 LTS
- Puppet 5.5 preinstalled
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests files must end with the extension .pp

## Installation Instructions
To install Puppet, follow these steps:
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
Tasks
Create a file: Create a file in /tmp with specific permissions, ownership, and content.
Path: /tmp/school
Permission: 0744
Owner: www-data
Group: www-data
Content: "I love Puppet"
Example:
bash
Copy code
$ puppet apply 0-create_a_file.pp
Install a package: Install flask from pip3 with a specific version.
Package: flask
Version: 2.1.0
Example:
bash
Copy code
$ puppet apply 1-install_a_package.pp
Execute a command: Create a manifest that kills a process named 'killmenow' using the exec Puppet resource and pkill.
Example:
bash
Copy code
$ puppet apply 2-execute_a_command.pp
Author
[Abayo Akinyi]
