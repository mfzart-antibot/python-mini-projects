# Python Mini Projects for DevOps Practice

A small collection of Python scripts focused on automation, monitoring, API checks, and log processing.

This repository reflects my practical learning path toward a junior DevOps role. The projects here are built to practice tasks that are common in operations and platform work: checking service availability, reading logs, detecting errors, and working with external APIs.

## Projects

### Log Generator and Live Log Reader
Location: `log-generator/`

A small log simulation and monitoring project.

What it does:
- generates fake application logs
- writes logs continuously to a file
- tails the log file in real time
- detects bursts of `ERROR` events in a time window
- saves detected error events to JSON for later inspection

Why it is relevant to DevOps:
- log analysis
- alert threshold logic
- real-time monitoring simulation
- structured event export

Run:
```bash
python log-generator/log-generator-to-file.py
python log-generator/live-log-reader.py log-generator/system.log 3

### Website Status Checker
Location: website-status/

Reads a list of URLs from a text file, checks whether they respond successfully, and saves working addresses to an output file.

What it does:
- normalizes URLs
- performs HTTP checks with timeout handling
- filters working pages based on response status
- writes successful URLs to a file

Why it is relevant to DevOps:
- endpoint validation
- basic health-check automation
- file-based batch processing

Run: python website-status/website-status-checker.py

### API Tools
Location: API-tools/

A set of small scripts for practicing HTTP requests and consuming public APIs.

Examples:
- Stack Overflow API request
- Rest Countries API request
- simple API status check

Why it is relevant to DevOps:
- API integration
- automation against external services
- parsing JSON responses
- working with HTTP status and response content

### Tech Used
Python 3
requests
JSON
file I/O
command-line scripts

### Setup

Create and activate a virtual environment, then install dependencies:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## Goals of This Repository

This repo is part of my learning process toward junior DevOps work. I use it to improve in:
- Python automation
- operational scripting
- log handling
- API usage
- writing small tools for monitoring-style tasks
- Future Improvements

### Planned next steps:

- add argument parsing with argparse
- improve error handling and exit codes
- add tests for key logic
- add GitHub Actions for linting
- make scripts easier to run in CI or cron-like **environments**

Author
Michał