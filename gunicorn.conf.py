# Gunicorn configuration file for production
import os
from dotenv import load_dotenv

load_dotenv()

# Server socket
bind = f"0.0.0.0:{os.getenv('FLASK_PORT', 5000)}"
backlog = 2048

# Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = 'rezervasyon_sistemi'

# Server mechanics
daemon = False
pidfile = 'logs/gunicorn.pid'
user = None
group = None
tmp_upload_dir = None

# SSL (for HTTPS)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'
