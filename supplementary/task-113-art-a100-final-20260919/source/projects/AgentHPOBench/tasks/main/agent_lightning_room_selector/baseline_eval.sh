#!/usr/bin/env bash
set -euo pipefail

cd .
mkdir -p results/formal_baselines/agent_lightning_room_selector
cat > results/formal_baselines/agent_lightning_room_selector/baseline.json <<'JSON'
{
  "task": "agent_lightning_room_selector",
  "metric": "validation_accuracy",
  "official_budget_baseline": 0.569,
  "paper_anchor": 0.721,
  "source": "repositories/agent-lightning/docs/how-to/train-first-agent.md"
}
JSON
cat results/formal_baselines/agent_lightning_room_selector/baseline.json
