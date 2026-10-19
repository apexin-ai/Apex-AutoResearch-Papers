# Status Check — Loop 6
**Timestamp**: 2026-05-14 23:01 CST

## GPU
- cuda:0: RTX PRO 6000 Blackwell 96GB, 100% util, 50481/97887 MiB, PID 337271 (Qwen s43 training)
- cuda:1: RTX PRO 6000 Blackwell 96GB, 100% util, 55407/97887 MiB, PID 76627 (StarCoder s42 training)

## m2_full_qwen (cuda:0)
- current run: random_s43 (seed=43, 2 epochs, early_stopping_patience=2)
- total steps: ~2810 (1405 batches/epoch × 2)
- current step: ~950 / 2810
- latest eval: eval@500 — val_loss=0.4476, R@1=0.5357, R@5=0.9699
- best checkpoint: val_loss=0.4476 & R@1=0.5357 (both at eval@500)
- status: **RUNNING** (PID 337271, started 19:24 CST)
- log: `/root/runs/m2_full_qwen/random_s43.log` (NOT the agent-ml path)
- note: running from `/root/structfuse-context/training/train.py`, launched via s43plus_all.log script
- previous run (random_s42, 3 epochs): **DONE** — best R@1=0.5527 at eval@1000, val_loss=0.4651

## m2_full_starcoder (cuda:1)
- current run: random_s42 (seed=42, 3 epochs)
- total steps: ~4242 (1414 batches/epoch × 3)
- current step: 3700 / 4242 (epoch 3)
- eval history:
  - eval@2000: val_loss=0.6698, R@1=0.4456
  - eval@2500: val_loss=0.6342, R@1=0.4604 ← best R@1
  - eval@3000: val_loss=0.6516, R@1=0.4544
  - eval@3500: val_loss=0.6588, R@1=0.4534
- best checkpoint: R@1=0.4604 at eval@2500 (saved to best_by_recall_at_1)
- val_loss not improved 5 consecutive evals (best was never saved — no early stopping configured for s42)
- status: **RUNNING** (PID 76627, started 02:30 CST)
- ETA: ~542 steps remaining, ~1-2 hours
- s43 auto-start: YES — `run_m2_full_starcoder.sh` runs in tmux, will start s43 after s42 finishes

## m1_reextract_v2
- total: 82 groups, 28,276 instances
- groups started: 71/82 (11 not yet started)
- currently active (4 workers): python-trio/trio (400/753), modin-project/modin (50/82), conan-io/conan, dask/dask
- all.jsonl lines: 44,173
- status: **RUNNING** (started 03:59 CST, ~19h elapsed)
- note: also running as m1_rerun (started 03:38), CodeQL queries actively processing

## Disk
- /root/autodl-tmp: 65GB available (186/250GB used, 75%)
- /root: 21GB available (9.8/30GB used, 33%)
