# Snake oil mill

This software is meant to help with fulfilling the requirements of various IT Security certifications without introducing new attack vectors by introducing unsafe code or relying on third party software and services.
One example would be the Payment Card Industry Data Security Standard.

The software can run in two modes, client and server.
Clients report regularly important security metrics to a configured server.
The server receives the information, stores them and generates reports.

## Alternatives

This functionality could be achieved with various monitoring and configuration management tools.
Main drawbacks are complexity and review ability.
This software should be so small that every user can review and verify the code in an acceptable amount of time, in order to ensure supply chain security.

## Requirements

* Agent can be run on each client
* Reporting to central management
    * Hostname
    * Antivirus state
    * AV signature state
    * Firewall state
* Central reports are generated and stored

## Technical solution

* Small, reviewable script
* Managed via systemd and alternative containerized
* client / back end in one package
* Check freshclam log
* Check if iptables INPUT policy is DROP
* Report hostname
* Push, outgoing HTTPS Requests
  * after start
  * every x hours
* Simple REST back end creating an "Auditlog" of all update events

## Configuration

```yaml
---
# Available modes: client, server
mode: client

# API to host or connect to
api: snake-oil-mill.example.com

# Username and password to authenticate
user: myuser
pw: 59bcc3ad6775562f845953cf01624225

commands:
 # Hostname to report
 - hostname: "hostname"

 # AV status to report
 - av: "clamscan --version"

 # Command to check the firewall configuration
 - firewall: "sudo iptables --table filter --list INPUT | grep 'Chain INPUT (policy DROP)'"

# Main sleep loop time (seconds)
loop_time_s: 60*60*8

# Time to wait for retry (seconds)
retry_time_s: 60
```
