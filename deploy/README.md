# Deploying the Streamlit app behind your domain (/playground)

These steps host `distribution_playground.py` on a Linux server and serve it at `https://YOUR_DOMAIN/playground/` via Nginx, while your existing site stays unchanged.

## 1) Copy files to server

On your server (Ubuntu/Debian):

```bash
sudo mkdir -p /opt/distribution_playground
sudo chown $USER:$USER /opt/distribution_playground
rsync -av --exclude deploy/ . /opt/distribution_playground/
rsync -av deploy/ /opt/distribution_playground/deploy/
```

## 2) Python env + deps
```bash
sudo apt update && sudo apt install -y python3-venv
cd /opt/distribution_playground
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
```

## 3) Streamlit service (systemd)
Create the service:
```bash
sudo tee /etc/systemd/system/distribution-playground.service >/dev/null <<'SERVICE'
[Unit]
Description=Streamlit Distribution Playground
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/distribution_playground
ExecStart=/opt/distribution_playground/.venv/bin/streamlit run distribution_playground.py \
  --server.baseUrlPath=playground \
  --server.headless=true \
  --server.port=8501 \
  --server.address=127.0.0.1 \
  --browser.gatherUsageStats=false \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false
Restart=on-failure

[Install]
WantedBy=multi-user.target
SERVICE

sudo systemctl daemon-reload
sudo systemctl enable --now distribution-playground
sudo systemctl status distribution-playground
```

## 4) Nginx reverse proxy
Install Nginx:
```bash
sudo apt install -y nginx
```

Create site config (replace YOUR_DOMAIN):
```bash
sudo tee /etc/nginx/sites-available/playground.conf >/dev/null <<'NGINX'
server {
  listen 80;
  server_name YOUR_DOMAIN;

  # Root site may already be served elsewhere; we only proxy /playground/
  location /playground/ {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    # WebSocket support
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    proxy_pass http://127.0.0.1:8501/playground/;
  }
}
NGINX

sudo ln -sf /etc/nginx/sites-available/playground.conf /etc/nginx/sites-enabled/playground.conf
sudo nginx -t && sudo systemctl reload nginx
```

## 5) HTTPS
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d YOUR_DOMAIN
```

## 6) Verify
Open `https://YOUR_DOMAIN/playground/` — the app should load and stay at that path.

Notes & troubleshooting:
- If you get a white page at `/playground/`, ensure the service uses `--server.baseUrlPath=playground`.
- WebSocket 400/upgrade errors → confirm the `Upgrade` and `Connection` headers are set and `proxy_http_version 1.1` is present.
- Logs: `journalctl -u distribution-playground -f` and `/var/log/nginx/error.log`.
