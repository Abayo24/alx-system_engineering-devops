# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure python3-pip is installed
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
  }
