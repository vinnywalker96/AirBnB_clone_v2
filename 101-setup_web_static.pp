# sets up web servers for the deployment of web_static

# Check if Nginx in installed
if ! package{'nginx':
    ensure => installed,
} {
    service {'nginx':
        ensure => running,
        enable => true,
    }
}

# Checks if directory path exist and creates
file {'/data/web_static/releases/test/':
    ensure => directory,
}
file {'/data/web_static/shared/':
    ensure => directory,
}
file {'/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '<html>\n    <head>\n    </head>\n    <body>\n         Holberton School\n    </body>\n</html>\n',
}

$SOURCE_DIR = '/data/web_static/current'
$TARGET_DIR = '/data/web_static/releases/test/'

# Creates a new link
file {'$SOURCE_DIR':
    ensure => link,
    target => "$TARGET_DIR",
}

# Give ownership to ubuntu user
file {'/data/':
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => true,
}

file {'/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server{\n 	listen 80 default_server;\n	listen [::]:80 default_server;\n	add_header X-Served-By $HOSTNAME;\n	server_name vestec.tech;\n	root /var/www/html;\n	index index.html index.htm;\n\n	location /hbnb_static {\n		alias  /data/web_static/current/;\n		index index.html index.htm;\n		\n	}\n\n	location /redirect_me {\n		return 301 https://github.com/vinnywalker96;\n	}\n	error_page 404 /404.html;\n        location = /404.html{\n             internal;\n         }\n}",
}

service {'nginx':
    ensure => running,
    enable => true,
    subscribe => File['/etc/nginx/sites-available/default'],
}


