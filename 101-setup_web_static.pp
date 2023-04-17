# Configures a web server for deployment of web_static

class nginx_server {
   package { 'nginx':
       ensure => installed,
   }

   service { 'nginx':
       ensure => running,
       enable => true,
       require => Package['nginx'],
   }

   file { '/data':
       ensure => directory,
   }
}

include nginx_server
  
