# Production Deployment
This project is running on a DigitalOcean droplet running Ubuntu 16.04. This
project should be cloned to a local user who is part of docker group. The
application is served by uWSGI with Nginx to proxy requests.

Copy `quicktry.service` to `/etc/systemd/system/quicktry.service`.
Enable the uWSGI service and enable it on boot.

```
$ sudo systemctl start quicktry
$ sudo systemctl enable quicktry
```

Copy `quicktry` to `/etc/nginx/sites-available/quicktry`. Modify the `server
.server_name` attribute. Enable the server block configuration by linking
this to sites-enabled.

```
$ sudo ln -s /etc/nginx/sites-available/quicktry /etc/nginx/sites-enabled
```

Restart nginx.
```
$ sudo systemctl restart nginx
```

## Related links
* [DigitalOcean - How To Serve Flask Applications with uWSGI and Nginx on
Ubuntu 16.04](https://www.digitalocean
.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)