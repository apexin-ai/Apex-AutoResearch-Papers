# Experiment Status Check — 2026-05-23 09:45 UTC

## Server 1: bjb1-32546

### Direction Experiments (Spatial seed42 sanity check)

All 5 tmux sessions alive, all PIDs confirmed running (~25 min elapsed).

| Experiment | GPU | PID | Status | Tasks Done | Current Task | Completed Task SRs |
|-----------|-----|-----|--------|-----------|-------------|-------------------|
| dirA_norm03 (CRM norm=0.3) | cuda:0 | 548888 | **RUNNING** | 2/10 | T3 rollout 15/20 | T1=100%, T2=85% |
| dirA_norm01 (CRM norm=0.1) | cuda:1 | 549157 | **RUNNING** | 2/10 | T3 rollout 15/20 | T1=95%, T2=95% |
| dirA_norm005 (CRM norm=0.05) | cuda:2 | 549426 | **RUNNING** | 3/10 | starting T4 | T1=95%, T2=100%, T3=100% |
| dirB_adaptive (Adaptive K) | cuda:4 | 550037 | **RUNNING** | 2/10 | T3 rollout 15/20 | T1=95%, T2=100% |
| dirC_reconvla (Reconvla K=10) | cuda:5 | 550634 | **RUNNING** | 3/10 | starting T4 | T1=100%, T2=95%, T3=100% |

### CRM 4-Suite Training

| Item | Value |
|------|-------|
| GPU | cuda:3 (PID 548658) |
| Status | **RUNNING** |
| Progress | Epoch 34/50, batch 200/6316 |
| Last epoch result | Epoch 33: train_loss=0.0104, **val_loss=0.0060 (new best!)** |
| Learning rate | 2.87e-04 |

### GPU Usage

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 37% | 5249/24564 MiB |
| 1 | 34% | 5249/24564 MiB |
| 2 | 26% | 4719/24564 MiB |
| 3 | 10% | 544/24564 MiB |
| 4 | 22% | 5155/24564 MiB |
| 5 | 30% | 5211/24564 MiB |

---

## Server 2: bjb2-28827

### Object CRM Eval (crm_obs_only, n_action_steps=50)

All 3 tmux sessions alive. Each at task 8/10 (milk).

| Seed | GPU | Status | Tasks Done | Current Task | Per-task SRs so far |
|------|-----|--------|-----------|-------------|-------------------|
| 42 | cuda:0 | **RUNNING** | 7/10 | milk (5/20) | alphabet_soup=70%, cream_cheese=50%, salad_dressing=50%, bbq_sauce=30%, ketchup=40%, tomato_sauce=45%, butter=40% |
| 43 | cuda:1 | **RUNNING** | 7/10 | milk (10/20) | alphabet_soup=70%, cream_cheese=50%, salad_dressing=50%, bbq_sauce=35%, ketchup=35%, tomato_sauce=50%, butter=65% |
| 44 | cuda:2 | **RUNNING** | 7/10 | milk (10/20) | alphabet_soup=70%, cream_cheese=70%, salad_dressing=45%, bbq_sauce=35%, ketchup=35%, tomato_sauce=45%, butter=45% |

Running averages (7 tasks): seed42=46.4%, seed43=50.0%, seed44=49.3%

### Spatial VLA-only Wrapper — COMPLETED

All 3 seeds finished. GPUs 3-5 now idle.

| Seed | Overall SR |
|------|-----------|
| 42 | **78.5%** |
| 43 | **80.5%** |
| 44 | **80.5%** |
| **Mean** | **79.8%** |

### GPU Usage

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 25% | 2476/24564 MiB |
| 1 | 32% | 2477/24564 MiB |
| 2 | 30% | 2477/24564 MiB |
| 3 | 0% | 1/24564 MiB (idle) |
| 4 | 0% | 1/24564 MiB (idle) |
| 5 | 0% | 1/24564 MiB (idle) |

---

## Summary

| Server | Experiment | Status | ETA |
|--------|-----------|--------|-----|
| bjb1 | dirA_norm03 | Running (3/10) | ~1.5h |
| bjb1 | dirA_norm01 | Running (3/10) | ~1.5h |
| bjb1 | dirA_norm005 | Running (3/10) | ~1.5h |
| bjb1 | dirB_adaptive | Running (3/10) | ~1.5h |
| bjb1 | dirC_reconvla | Running (3/10) | ~1.5h |
| bjb1 | CRM 4-suite training | Running (epoch 34/50) | ~4h |
| bjb2 | Object CRM s42 | Running (8/10) | ~30min |
| bjb2 | Object CRM s43 | Running (8/10) | ~30min |
| bjb2 | Object CRM s44 | Running (8/10) | ~30min |
| bjb2 | Spatial VLA-only | **COMPLETED** | — |

### Anomalies
- **bjb2 GPUs 3-5 idle** — Spatial VLA-only finished, GPUs freed. Can be reused for new experiments.
- No errors or crashes detected on either server.
