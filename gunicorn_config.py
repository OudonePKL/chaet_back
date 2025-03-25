import multiprocessing
import os

# Ensure directories exist
os.makedirs('/var/log/gunicorn', exist_ok=True)
os.makedirs('/run/gunicorn', exist_ok=True)

# Server socket
bind = 'unix:/run/gunicorn/gunicorn.sock'
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'daphne.workers.GunicornWorker'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
loglevel = 'debug'

# Process naming
proc_name = 'chat_backend'

# Server mechanics
daemon = False
pidfile = '/run/gunicorn/gunicorn.pid'
umask = 0o002  # More permissive umask
user = 'www-data'
group = 'www-data'
tmp_upload_dir = None

# Capture output
capture_output = True
enable_stdio_inheritance = True 