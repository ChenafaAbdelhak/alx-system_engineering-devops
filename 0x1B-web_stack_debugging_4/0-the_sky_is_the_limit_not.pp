# manifest to change ulimit so the nginx can handle appropriate amount of requests

exec { 'update_ulimit':
  provider => shell,
  command  => "sudo sed -i 's/^ULIMIT=.*/ULIMIT=-n 4096/' /etc/default/nginx",
  before   =>  Exec['restart_nginx'],
}

exec { 'restart_nginx':
  provider  => shell,
  command   => 'sudo service nginx restart',
  subscribe => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
