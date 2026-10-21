#!/bin/bash
# One-liner for submit_training_job
# Usage: bash scripts/submit_exp012.sh
nohup bash /root/schema-dag-extraction/scripts/run_exp012_llama.sh > /root/schema-dag-extraction/logs/exp012_llama.log 2>&1 &
echo "exp-012 launched, PID=$!"
echo "Log: /root/schema-dag-extraction/logs/exp012_llama.log"
