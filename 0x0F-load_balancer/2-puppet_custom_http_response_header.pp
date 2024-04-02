# Puppet script to configure custom HTTP response header
class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "# Default server configuration\n
                \n
                server {\n
                        listen 80 default_server;\n
                        listen [::]:80 default_server;\n
                \n
                        # Add custom HTTP response header\n
                        add_header X-Served-By $::hostname;\n
                \n
                        root /var/www/html;\n
                \n
                        index index.html index.htm index.nginx-debian.html;\n
                \n
                        server_name _;\n
                \n
                        location / {\n
                                try_files $uri $uri/ =404;\n
                        }\n
                \n
                        location = /404.html {\n
                                root /usr/share/nginx/html;\n
                        }\n
                \n
                        location ~ \\.php$ {\n
                                include snippets/fastcgi-php.conf;\n
                                fastcgi_pass unix:/run/php/php7.4-fpm.sock;\n
                        }\n
                \n
                        location ~ /\\.ht {\n
                                deny all;\n
                        }\n
                }\n",
    notify  => Service['nginx'],
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_custom_header

