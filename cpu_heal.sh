#!/bin/bash

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

echo "CPU usage: $CPU"

if (( $(echo "$CPU > 80" | bc -l) )); then
    echo "High CPU detected - restarting service"
    systemctl restart node_exporter
fi
