Location: autodl-5090:/root/gen-depth-fingerprint/

Scripts:
- finetune_downstream.py — HF Trainer CLM fine-tuning, supports --dry-run, --seed, --bf16
- run_downstream.sh — Orchestrator: runs all 5 variants x 3 seeds (42, 123, 456) on specified GPU
- prepare_downstream_data.py — Builds depth-stratified datasets from plan-002 data
- compute_binary_baseline.py — Computes NLL scores and creates binary-filtered variant

Model: OLMo-2-0425-1B at /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B (1485M params)

To launch training:
  cd /root/gen-depth-fingerprint && bash run_downstream.sh 3

Dry-run verified: loss=2.18 (1 step, depth0_only variant)