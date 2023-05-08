# sets up your web servers for the deployment of web_static
class nginx_server {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
        ensure => running,
        enable => true,
        require => Package['nginx'],
    }

    exec { 'create /data/':
        command => '/usr/bin/sudo /bin/mkdir -p /data/',
        creates => '/data/',
    }

    exec { 'create /data/web_static/':
        command => '/usr/bin/sudo /bin/mkdir -p /data/web_static/',
        creates => '/data/web_static/',
    }

    exec { 'creates /data/web_static/releases/':
        command => '/usr/bin/sudo /bin/mkdir -p /data/web_static/releases/',        creates => '/data/web_static/releases/',
    }

    exec { 'creates /data/web_static/shared/':
        command => '/usr/bin/sudo /bin/mkdir -p /data/web_static/shared/',
        creates => '/data/web_static/shared/',
    }

    exec { 'creates /data/web_static/releases/test':
        command => '/usr/bin/sudo /bin/mkdir -p /data/web_static/releases/test/',
        creates => '/data/web_static/releases/test/',
    }

    file { '/data/web_static/releases/test/index.html':
        content => 'Holberton School',
        require => Package['nginx'],
    }
    exec { 'create symbolic link':
        command => '/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
        creates => '/data/web_static/current',
    }

    exec { 'change ownership of /data directory':
       command => '/usr/bin/chown -R ubuntu /data/',
       path => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
    }

   exec { 'change ownership group of /data directory':
      command => '/usr/bin/chgrp -R ubuntu /data/',
      path => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
   }

    file { '/etc/nginx/sites-available/default':
        content => "\
server{
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static{
                alias /data/web_static/current;
                index index.html index.htm;
        }

        location /redirect_me{
                return 301 https://github.com/vinnywalker96;
        }

        error_page 404 /404.html;
        location = /404.hmtl{
                internal;
        }
}",
        require => Package['nginx'],
        notify => Service['nginx'],
    }
}


