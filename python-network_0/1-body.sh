#!/bin/bash
# sends a GET request and displays the body only if the status is 200
curl -s -o /tmp/body_output -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body_output
