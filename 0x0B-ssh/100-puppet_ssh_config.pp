#!/usr/bin/env bash
# using Puppet to make changes to our configuration file.

file { 'ect/ssh/ssh_config':
	ensure => present,

content =>"
		
	#SSH client config
	host*
	IdntityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
