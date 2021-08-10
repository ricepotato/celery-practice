#!/bin/bash
source ./.venv/bin/activate
celery -A proj worker -l INFO