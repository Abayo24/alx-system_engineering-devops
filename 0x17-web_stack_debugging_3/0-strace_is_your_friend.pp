# 0-strace_is_your_friend.pp
# Puppet manifest to install Apache, PHP, and WordPress

class { 'apache': }

class { 'apache::mod::php': }

package { 'wordpress':
  ensure => present,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html>
<head>
    <title>Holberton &#8211; Just another WordPress site</title>
</head>
<body>
    <h1>Holberton</h1>
    <p>Yet another bug by a Holberton student</p>
</body>
</html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

