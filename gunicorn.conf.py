import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
keepalive = 2
daemon = True
certfile = '/etc/letsencrypt/live/dbc.my.to/fullchain.pem'
keyfile = '/etc/letsencrypt/live/dbc.my.to/privkey.pem'
pidfile = 'pidfile'
errorlog = 'errorlog'
loglevel = 'info'
accesslog = 'accesslog'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'