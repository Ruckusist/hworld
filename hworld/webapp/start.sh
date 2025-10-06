#!/bin/bash
# hworld/webapp/start.sh
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

# Start both server and webapp
python -m hworld.server &
SERVER_PID=$!

python -m hworld.webapp &
WEBAPP_PID=$!

# Wait for both processes
wait $SERVER_PID
wait $WEBAPP_PID
