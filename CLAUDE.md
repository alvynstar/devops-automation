# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Playbooks

```bash
# Run a specific monitor playbook (vars.yml is loaded automatically via vars_files)
ansible-playbook cpu_monitor.yml
ansible-playbook disk_monitor.yml
ansible-playbook memory_monitor.yml

# Run with privilege escalation prompt (for become: yes tasks)
ansible-playbook cpu_monitor.yml --ask-become-pass

# Dry-run to check syntax and task flow without executing
ansible-playbook cpu_monitor.yml --check
```

## Variables

Sensitive values are stored in `vars.yml` (not committed to git) and referenced in playbooks via `{{ variable_name }}`.

| Variable | Description |
|---|---|
| `slack_webhook_url` | Slack incoming webhook URL for alert notifications |

Copy `vars.yml.example` to `vars.yml` and fill in your values before running any playbook.

## Architecture

All three playbooks share the same pattern: **check → log → remediate → notify**.

| Playbook | Metric command | Threshold | Remediation |
|---|---|---|---|
| `cpu_monitor.yml` | `top -bn1` | `> 5%` | `kill -9` top CPU process |
| `disk_monitor.yml` | `df /` | `> 10%` | Delete `/var/log` files older than 30d + vacuum journald |
| `memory_monitor.yml` | `free` | `> 20%` | Drop kernel page/slab caches via `/proc/sys/vm/drop_caches` |

Remediation and Slack notification tasks are gated by the same `when:` condition, so no alert fires and no cleanup runs unless the threshold is crossed.

The Slack webhook URL is no longer hardcoded — it is sourced from `vars.yml` via the `slack_webhook_url` variable. To rotate the webhook, update `vars.yml` only (one place).
