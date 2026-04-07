`log-generator/README.md`
```md
# Log Generator and Live Log Reader

A small Python project for simulating application logs and monitoring them in real time.

This project was created as part of my DevOps learning path. It focuses on log generation, live log reading, error detection, and basic alerting logic.

## Overview

The project contains two scripts:

- `log-generator-to-file.py`
Creates fake application log entries and saves them continuously to a log file.

- `live-log-reader.py`
Reads the log file in real time, detects `ERROR` events, and prints an alert when the number of errors crosses a chosen threshold within a time window.

Additionally, detected error events are written to `errors.json` for later inspection.

## Features

- generates fake log messages with timestamps
- uses multiple log levels: `INFO`, `WARNING`, `ERROR`
- writes logs continuously to `system.log`
- tails the log file live
- counts recent `ERROR` events in a rolling 60-second window
- triggers an alert when the threshold is reached
- stores error events in JSON format

## Why This Project Matters for DevOps

This project is a small simulation of real operational tasks such as:
- monitoring logs
- detecting abnormal error rates
- building simple alerting logic
- exporting events for later analysis
- working with continuously growing log files

These are common patterns in infrastructure, support, SRE, and DevOps-oriented automation.

## Files

- `log-generator-to-file.py` - generates and appends logs to file
- `live-log-reader.py` - monitors log file and alerts on high error frequency
- `system.log` - generated log output
- `errors.json` - exported error events

## Requirements

Install dependencies from the root of the repository:

```bash
pip install -r requirements.txt

## Usage

python log-generator-to-file.py
python live-log-reader.py system.log <Alert THRESHOLD>
