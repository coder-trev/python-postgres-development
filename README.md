### _!! Current Ansible build only works on Manjaro Linux. !!_

## Overview of Role

* Install Miniconda
* Create python environment
* Install docker and docker-compose
* Install docker images

## Install

```
# pacman -S ansible
# git clone https://github.com/coder-trev/python-postgres-development.git
# cd python-postgres-development
# ansible-playbook --ask-pass --ask-become-pass play.yml
```

## Configuration

Edit `file/docker-compose.yml` to modify the containers.

Override the variables in `defaults/main.yml` using `vars/main.yml`.

The postgres database volume will live at `/var/lib/docker/volumes/compose_pgdb` unless changed.

The pgAdmin database volume will live at `/var/lib/docker/volumes/compose_pgadmin` unless changed.

## Database Guide

Use the **Start** commands below and navigate to http://localhost:80 in a browser to get to pgAdmin. Use the login user:`admin@domain.com` pass:`adminpass`. (Defined in `files/docker-compose-pg.yml`). 

Use the **List containers** commands below to the get the running image name of the database, should be `compose-db-1`. In pgAdmin, use the 'Create Server' button and put in:

* Server Name: this can be whatever you like
* Host Name: what we found from **List containers**, `compose-db-1`
* Username: postgres
* Password: abc123 (Defined in `files/docker-compose-pg.yml`)

There's some python scripts to test the database connection in `tests/`

## Python Guide

**NOTE:** If `conda` isn't on your path and won't run, log out and log back in or open a new bash terminal.

Using Python, the install directory for conda is defined in `defaults/main.yml`. Just use the python executable inside the environment in there.

Use the absolute path

```
$ /usr/local/miniconda3/envs/postgres-3.6/bin/python myscript.py
```

Or activate the environment

```
$ conda activate postgres-3.6
$ python myscript.py
$ deactivate
```

## Docker Guide

Start service and containers

```
# systemctl start docker
# docker-compose -f /usr/local/docker-compose/docker-compose-pg.yml up -d
```

List containers

```
# docker-compose -f /usr/local/docker-compose/docker-compose-pg.yml ps
```

Login to database on command line. Password defined in `files/docker-compose-pg.yml`.

```
# docker-compose -f /usr/local/docker-compose/docker-compose-pg.yml psql -U postgres
```

## Stop

```
# docker-compose -f /usr/local/docker-compose/docker-compose-pg.yml down
# systemctl stop docker
```
