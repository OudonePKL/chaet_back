import multiprocessing

# Server socket
bind = "unix:/run/gunicorn.sock"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'channels.worker.Worker'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
loglevel = 'info'

# Process naming
proc_name = 'chat_backend'

# Server mechanics
daemon = False
pidfile = '/var/run/gunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None 