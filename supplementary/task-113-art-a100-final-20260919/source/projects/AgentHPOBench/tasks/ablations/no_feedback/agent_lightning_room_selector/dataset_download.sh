#!/usr/bin/env bash
set -euo pipefail

cd .
test -f repositories/agent-lightning/examples/apo/room_tasks.jsonl
mkdir -p data/paper_exact/agent_lightning_room_selector
cp repositories/agent-lightning/examples/apo/room_tasks.jsonl data/paper_exact/agent_lightning_room_selector/room_tasks.jsonl
echo "room selector dataset is checked into agent-lightning and copied to data/paper_exact/agent_lightning_room_selector"
