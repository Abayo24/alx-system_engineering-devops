# Increase the ULIMIT of the default file

exec { 'fix_nginx':
  command => 'sed -i "s/15/1000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
