# This manifest updates the nofile limits in the /etc/security/limits.conf file

exec { 'replace-nofile-hard':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-nofile-soft'],
}

exec { 'replace-nofile-soft':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
