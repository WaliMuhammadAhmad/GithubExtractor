#!/bin/bash
echo "Building Docker image..."
docker build -t ihatenlp/junitextractor .
echo "Cleaning up old images..."
docker image prune -f  # -f skips confirmation
echo "Running container..."
docker run -p 5000:5000 ihatenlp/junitextractor flask run --host=0.0.0.0 --port=5000 --debug