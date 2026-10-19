#!/bin/bash
# AIDE @ gpt-5.6-sol on the aif360 protocol, 3 rounds x 100 steps.
# Parity note: FML_REASONING_EFFORT=high matches the ApexTune kernel's
# reasoning_effort="high" (see agents/llm.py parity patch, 2026-09-18).
set -u
source /root/miniconda/etc/profile.d/conda.sh
conda activate runner
export AGENT_ML_WORKSPACE=/root/apextune-workspace
export OPENAI_API_KEY=[REDACTED] python -c "
import sys; sys.path.insert(0,'/root/agent-ml-research')
from pathlib import Path
from core.crypto import load_secret
print(load_secret(Path('/root/apextune-workspace/config/secrets/apextune-fml/apexin_api_key.enc')))
")
export OPENAI_BASE_URL="https://api.apexin.ai/v1"
export FML_REASONING_EFFORT=high
cd /root/fml-bench

MODE="${1:-full}"

if [ "$MODE" = "smoke" ]; then
  echo "=== SMOKE: 5 steps ==="
  python -u run_agent_benchmark.py \
    --agent-config configs/agents/aide.yaml \
    --task-config configs/tasks/fairness_and_bias_aif360.yaml \
    --model gpt-5.6-sol --provider OpenAI \
    --workspace-label aide-smoke-5steps \
    agent.aide.max_steps=5 2>&1
  echo "SMOKE EXIT=$?"
  exit $?
fi

if [ "$MODE" = "round3" ]; then
  echo "=== AIDE round 3 (100 steps) start: $(date -u +%H:%M:%S) ==="
  python -u run_agent_benchmark.py \
    --agent-config configs/agents/aide.yaml \
    --task-config configs/tasks/fairness_and_bias_aif360.yaml \
    --model gpt-5.6-sol --provider OpenAI \
    --workspace-label "aide-gpt56sol-aif360-r3" \
    agent.aide.max_steps=100 2>&1
  echo "=== AIDE round 3 EXIT=$? at $(date -u +%H:%M:%S) ==="
  echo "ROUND3_DONE"
  exit 0
fi

for R in 1 2 3; do
  echo "=== AIDE round ${R}/3 (100 steps) start: $(date -u +%H:%M:%S) ==="
  python -u run_agent_benchmark.py \
    --agent-config configs/agents/aide.yaml \
    --task-config configs/tasks/fairness_and_bias_aif360.yaml \
    --model gpt-5.6-sol --provider OpenAI \
    --workspace-label "aide-gpt56sol-aif360-r${R}" \
    agent.aide.max_steps=100 2>&1
  echo "=== AIDE round ${R}/3 EXIT=$? at $(date -u +%H:%M:%S) ==="
done
echo "ALL_AIDE_ROUNDS_DONE"
