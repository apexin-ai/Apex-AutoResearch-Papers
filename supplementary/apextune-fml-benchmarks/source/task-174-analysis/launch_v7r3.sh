#!/bin/bash
source /root/miniconda/etc/profile.d/conda.sh
conda activate runner
export AGENT_ML_WORKSPACE=/root/apextune-workspace
cd /root/agent-ml-research
TS=$(date +%Y%m%d_%H%M%S)
RUNDIR="aif360-gpt56sol-qd-v7-r3-${TS}"
echo "RUN_ID=${RUNDIR}"
python -u -m core.research.llmloop.fml.cli \
  --task aif360 \
  --fml-root /root/fml-bench \
  --round 7 --seed 2 --max-new-steps 100 --max-llm-requests 300 \
  --model gpt-5.6-sol \
  --allow-model-override --allow-reconstructed --allow-noncomparable \
  --robustify \
  --final-accuracy-margin 0.02 \
  --mutation-timeout 600 \
  --run-id "${RUNDIR}" \
  > "${RUNDIR}.log" 2>&1
echo "EXIT=$?"
