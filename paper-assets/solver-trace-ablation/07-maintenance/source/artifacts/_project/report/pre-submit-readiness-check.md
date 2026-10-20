# Pre-Submit Readiness Check (2026-05-15)

## Environment
- torch=2.10.0+cu128, transformers=4.57.6, trl=1.1.0
- Base model: /root/autodl-tmp/models/Qwen3-4B (exists)
- Disk: root 21GB free, data 204GB free

## Running Jobs
- PID 363692: plan001-exec-only-s43-1000-r2, GPU0, elapsed ~2h
- PID 363840: plan001-exec-only-s44-1000-r2, GPU1, elapsed ~2h

## Experiment 1: plan002-additive-b01-s43-r2
- **ready: FALSE**
- **BLOCKER**: configs/grpo_additive_b01.yaml does NOT exist
  - Actual file: configs/grpo_additive_bonus_b01.yaml (reward_mode: additive_bonus)
  - Fix: use --config configs/grpo_additive_bonus_b01.yaml --reward_mode additive_bonus
- data/train_500_seed42.jsonl: 500 lines OK
- scripts/train_grpo.py: exists OK
- Output dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2: does not exist (no conflict)

## Experiment 2: plan018-additive-random-b01-s44-r2
- **ready: TRUE**
- configs/grpo_additive_random_b01.yaml: exists OK (reward_mode: additive_random, beta: 0.1)
- data/train_500_seed42.jsonl: 500 lines OK
- scripts/train_grpo.py: exists OK
- Output dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2: does not exist (no conflict)

## Experiment 3: plan018-additive-random-b01-s43-r3
- **ready: TRUE**
- configs/grpo_additive_random_b01.yaml: exists OK
- data/train_500_seed42.jsonl: 500 lines OK
- scripts/train_grpo.py: exists OK
- Output dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r3: does not exist (no conflict)