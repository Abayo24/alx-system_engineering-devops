# Puppet manifest to kill a process named killmenow

# Define the exec resource to kill the process
exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],  # Add appropriate paths if needed
  refreshonly => true,  # Run only when triggered
}

