# GPU Status Report — Loop 18
**Timestamp:** 2026-05-17 03:02 UTC

## GPU Overview

| GPU | Mem Used | Util | Active PID | Task |
|-----|----------|------|-----------|------|
| 0 | 8081/24564 MiB | 82% | 825638 | eval d005_s42 |
| 1 | 8627/24564 MiB | 62% | 830115 (+829606,829849,830425) | signals d000 mmlu |
| 2 | 3/24564 MiB | 0% | — | **IDLE** |
| 3 | 8313/24564 MiB | 85% | 822390 (wrapper 822385) | eval d025_s42 |
| 4 | 579/24564 MiB | 0% | 831936 (rogue) | rogue gsm8k signals, minimal footprint |
| 5 | 8313/24564 MiB | 82% | 831033 | eval d100_s42 |

## Experiment Status

| exp_id | PID | GPU | Status | Details |
|--------|-----|-----|--------|---------|
| exp_001_eval_llama32_3B_d005_s42 | 825638 | cuda:0 | **ALIVE** | GSM8K 720/1319 (55%), ~5.8s/it, ETA ~58 min |
| exp_002_signals_llama32_3B_d000_mmlu | 830115 | cuda:1 | **ALIVE** | Running 40min, selfcritique mmlu in chunks (`_s4_chunks_mmlu/`) |
| exp_002_signals_llama32_3B_d000_gsm8k | 835978 | cuda:2 | **DEAD** | PID gone, GPU 2 idle. No exit file. Log shows HF timeouts (sentence-transformers). **However** gsm8k signals completed via unregistered PID 831936 on cuda:4 — output files exist: s1_embedding, s2_minkpp, s4_selfcritique, signals_merged (all timestamped 02:58–03:02) |
| exp_001_eval_llama32_3B_d025_s42 | 822385 | cuda:3 | **ALIVE** | GSM8K 487/1319 (37%), ~6.1s/it, ETA ~1h28m |
| exp_002_signals_15B_instruct_mmlu | 810809 | cuda:4 | **DEAD** | PID gone. **No log file exists.** No exit file. Experiment never started successfully or log path misconfigured. |
| exp_001_eval_llama32_3B_d100_s42 | 831033 | cuda:5 | **ALIVE** | Running 39min, actively evaluating |
| exp_006_mmlu_domain_gamma_n24_v3 | 827068 | CPU | **ALIVE** | Running 01:03:03. Child PID 837003 running stansummary at 99.8% CPU (MCMC summary phase) |

## exp_002_signals_llama32_3B_d000_arc

**Status: COMPLETED (no active process)**

Log shows successful completion at 2026-05-17 02:33:46 UTC. All 3 signals computed for arc_challenge (1172 items):
- `signal_s1_embedding_arc_challenge.json` (02:27)
- `signal_s2_minkpp_arc_challenge.json` (02:27)
- `signal_s4_selfcritique_arc_challenge.json` (02:33)
- `signals_merged_arc_challenge.json` (02:33)

Output dir: `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/`

## Rogue/Untracked Processes

| PID | GPU | Command | Notes |
|-----|-----|---------|-------|
| 831936 | cuda:4 (570MiB) | compute_signals.py --benchmark gsm8k | From wrapper 831935 (CUDA_VISIBLE_DEVICES=4). Completed gsm8k signals. |
| 835593 | none (1.1GB RAM) | compute_signals.py --benchmark gsm8k --batch-size 8 | Stuck on HF timeouts, not on GPU. Should be killed. |

## Summary

- **4 alive (GPU):** d005 eval (cuda:0), d000 mmlu signals (cuda:1), d025 eval (cuda:3), d100 eval (cuda:5)
- **1 alive (CPU):** exp_006 domain gamma v3 — in MCMC summary phase
- **2 dead:** gsm8k signals (PID 835978, but output completed via rogue 831936), 15B instruct mmlu (PID 810809, never started)
- **1 completed:** arc signals — all outputs present, process exited cleanly
- **GPU 2 free**, GPU 4 reclaimable after killing rogue PID 831936/835593
- **Action needed:** Mark gsm8k signals as completed (output exists), mark 15B instruct mmlu as failed (never ran), kill rogue PID 835593
