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

   file { '/data/':
       ensure => directory,
   }

   file { '/data/web_static/':
       ensure => directory,
   }
 
   file { '/data/web_static/releases/':
       ensure => directory,
   }

   file { '/data/web_static/shared/':
       ensure => directory,
   }

   file { '/data/web_static/releases/test/':
       ensure => directory,
   }


   file { '/data/web_static/releases/test/index.html':
        content => 'Holberton School',
        require => Package['nginx']
   }

   
   exec { 'chown -R ubuntu /data/':
        path => '/usr/bin/:/usr/local/bin/:bin/'
   }
   exec { 'chgrp -R ubuntu /data/':
        path => '/usr/bin/:/usr/local/bin/:/bin/'
   }

   file { '/data/web_static/current':
       ensure => link,
       target => '/data/web_static/releases/test'
   }

  file { '/etc/nginx/sites-available/default':
      ensure  => 'present',
      content => "\
 server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    if (\$request_filename ~ redirect_me) {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
}",
    }
    exec { 'nginx restart':
        path => '/etc/init.d/'
    }


}

include nginx_server
  
