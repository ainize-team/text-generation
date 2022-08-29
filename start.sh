#!/bin/bash
redis-server --daemonize yes

uvicorn server:app --host=0.0.0.0