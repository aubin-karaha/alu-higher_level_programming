#!/bin/bash
# sends a GET request, follows redirects, and displays the body only if final status is 200
curl -s -L -o /tmp/body_output -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body_output
