# DevOps Automation Portfolio - Alvin Detoya

## About
Self-healing infrastructure automation scripts built as part of my transition from Infrastructure Reliability Engineer to DevOps Engineer.

## Projects

### 1. Disk Monitor (disk_monitor.yml)
- Monitors disk usage on Linux servers
- Automatically cleans up log files older than 30 days
- Rotates journal logs using journalctl
- Triggers alert when usage exceeds threshold

### 2. CPU Monitor (cpu_monitor.yml)
- Monitors CPU usage in real-time
- Automatically kills runaway processes consuming high CPU
- Sends Slack alert when threshold is exceeded

### 3. Memory Monitor (memory_monitor.yml)
- Monitors memory usage
- Automatically clears system cache when usage is high
- Triggers alert when threshold is exceeded

## Stack
- Ansible
- Linux (Ubuntu)
- Bash
- Cron (runs every 30 minutes automatically)
- Slack webhooks for alerting

## Status
Active development - adding Python scripts and Prometheus/Grafana monitoring next.
