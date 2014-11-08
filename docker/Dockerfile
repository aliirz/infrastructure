FROM dockerfile/ubuntu
MAINTAINER Ashar Rizqi <asharrizqi@gmail.com>

#add to repo list
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list
run apt-get update

#change working directory
WORKDIR /usr/local/
RUN git clone https://github.com/codeforpakistan/infrastructure.git

#setup tools and python
RUN \
  apt-get install -y tar \
                     git \
                     curl \
                     wget \
                     net-tools \
                     build-essential

RUN \
  apt-get install -y python \
                     python-dev \
                     python-distribute \
                     python-pip

#install flask
RUN \
  pip install flask

#instal uwsgi
RUN \
  pip install uwsgi

# Install Nginx.
RUN \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/* 

# symlink conf dir
RUN ln -s /usr/local/infrastructure/conf/nginx/nginx.conf /etc/nginx/sites-enabled/
RUN unlink /etc/nginx/sites-enabled/default

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN mkdir -p /var/log/uwsgi/
RUN touch /var/log/uwsgi/uwsgi.log

RUN touch /usr/local/run.sh
RUN chmod 755 /usr/local/run.sh
#RUN echo "#!/bin/bash\nuwsgi --socket 127.0.0.1:8080 --chdir /usr/local/infrastructure/apps/example/ --module app --callable app --processes 1 --daemonize /var/log/uwsgi/uwsgi.log;nginx;" >> /usr/local/run.sh

RUN echo "#!/bin/bash\nuwsgi --ini /usr/local/infrastructure/conf/uwsgi/uwsgi.ini;nginx;" >> /usr/local/run.sh

CMD ["/usr/local/run.sh"]

