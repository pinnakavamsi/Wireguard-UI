
# WireGuard Web GUI - Complete Package

## ⭐ Features
- Web-based WireGuard management
- Add/Delete/Pause/Resume clients
- Auto-generate client configs
- QR code onboarding
- Real-time connection status
- Change subnet and DNS
- Automatic IP reassignment
- Download .conf files
- Admin password change
- REST API with Swagger
- Production installer script
- Dockerfile + docker-compose support

## 🖥 System Requirements
- Ubuntu 20.04 or 22.04 LTS
- 1 CPU, 1GB RAM minimum
- Root access
- Public IP address
- Domain name for HTTPS
- Ports: 443/tcp, 51820/udp

## 🚀 Installation Procedure

### 1. SSH into your server
```
ssh root@server_ip
```

### 2. Install dependencies
Provided in installer.

### 3. Run installer
```
sudo bash install.sh
```

### 4. Enter:
- Domain name for GUI
- Email for Let's Encrypt

### 5. Access dashboard
```
https://your-domain
```

Default login:
```
admin / admin
```

You may replace app.py and install.sh placeholders with full versions.
