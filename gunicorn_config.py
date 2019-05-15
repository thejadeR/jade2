import psycogreen.gevent
psycogreen.gevent.patch_psycopg()

bind = "0.0.0.0:8000"
backlog = 256
workers = 4
worker_class = "gevent"
worker_connections = 1000
max_requests = 300
keepalive = 300
timeout = 30
graceful_timeout = 30
pidfile = "/var/log/project/project.pid"
errorlog = "/var/log/project/project.log"

