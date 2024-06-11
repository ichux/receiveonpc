wsgi_app = "runner:app"
bind = "0.0.0.0:5000"

max_requests = 10000
max_requests_jitter = 1000
timeout = 30
graceful_timeout = 30

workers = 4
