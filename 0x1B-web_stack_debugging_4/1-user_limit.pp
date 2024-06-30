# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

exec {'OS_security_config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
