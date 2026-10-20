# GPU Diagnostic Report — 2026-05-27 04:45 (Beijing Time)

## Summary

| Metric | Count |
|--------|-------|
| Total GPUs | 14 |
| Active GPUs | 11 |
| **Idle GPUs** | **3** |
| Running experiments | 13 |
| Cron-tracked (all alive) | 5/5 |
| Registry zombie entries | 6/6 |

---

## Server 1: westd-27271 (2x RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PID | Experiment | Status |
|-----|-----|------|-----|------------|--------|
| 0 | 1 MiB | 0% | — | — | **IDLE** |
| 1 | 15942 MiB | 73% | 397225 | `eval_openvla_attn_k05_long_seed42` (attention_prune k=0.5, libero_10) | Active, log @04:37 |

---

## Server 2: cqa1-33015 (4x RTX 4090 D, 24GB)

| GPU | Mem | Util | PID | Experiment | Status |
|-----|-----|------|-----|------------|--------|
| 0 | 10228 MiB | 23% | 617566 | `eval_pi05_l2norm_k07_long_seed42` (l2norm k=0.7, libero_10) | Active, log @04:40 |
| 1 | 10817 MiB | 8% | 617728 | `eval_pi05_attention_k07_long_seed42` (attention k=0.7, libero_10) | Active, log @04:39 |
| 2 | 10562 MiB | 59% | 582964 | `eval_pi05_attention_k05_long_seed42_v3` (attention k=0.5, libero_10) | Active, log @04:40 |
| 3 | 1 MiB | 0% | — | — | **IDLE** |

Note: GPU 0 was previously expected idle but is active. GPU 3 is idle instead.

---

## Server 3: westd-41074 (4x RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PIDs | Experiments | Status |
|-----|-----|------|------|-------------|--------|
| 0 | 31957 MiB | 86% | 846246, 856148 | `eval_openvla_random_k07_object_seed42` + `eval_openvla_random_k075_object_seed42` | Active |
| 1 | 32165 MiB | 93% | 846317, 856656 | `eval_openvla_l2norm_k09_object_seed42` + `eval_openvla_random_k075_long_seed42` | Active |
| 2 | 15980 MiB | 70% | 755986 | `eval_openvla_attn_k075_object_seed42` | Active |
| 3 | 15780 MiB | 89% | 824210 | `eval_openvla_attn_k075_long_seed42` | Active |

All 4 GPUs active. GPU 0 and 1 each run 2 experiments (~32GB each, fits in 98GB).

---

## Server 4: westd-38929 (4x RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PID | Experiment | Status |
|-----|-----|------|-----|------------|--------|
| 0 | 16212 MiB | 64% | 623613 | `eval_openvla_l2norm_k05_long_seed42` | Active, log @04:33 |
| 1 | 15942 MiB | 69% | 668245 | `eval_openvla_random_k085_long_seed42_v3` | Active, log @04:37 |
| 2 | 15880 MiB | 62% | 732931 | `eval_openvla_l2norm_k075_long_seed42` | Active, log @04:42 |
| 3 | 1 MiB | 0% | — | — | **IDLE** |

Model path uses `models/` prefix: `/root/autodl-tmp/models/openvla-7b-finetuned-libero-10`

---

## Idle GPU Summary

| # | Server | GPU | Confirmed |
|---|--------|-----|-----------|
| 1 | westd-27271 | cuda:0 | 0% util, 1 MiB |
| 2 | cqa1-33015 | cuda:3 | 0% util, 1 MiB (NOT cuda:0 as previously expected) |
| 3 | westd-38929 | cuda:3 | 0% util, 1 MiB |

---

## Cron-tracked Experiments — All 5 ALIVE

| Experiment | Tracked PID | Actual PID | Server | GPU | Progress |
|------------|-------------|------------|--------|-----|----------|
| eval_openvla_l2norm_k05_long_seed42 | 623613 | 623613 | westd-38929 | 0 | Task 7/10 |
| eval_openvla_attn_k05_long_seed42 | 397225 | 397225 | westd-27271 | 1 | Task 6/10 |
| eval_openvla_random_k085_long_seed42_v3 | 668236 | 668245 | westd-38929 | 1 | Running |
| eval_openvla_attn_k075_object_seed42 | 755977 | 755986 | westd-41074 | 2 | Task 3/10 |
| eval_openvla_l2norm_k075_long_seed42 | 732922 | 732931 | westd-38929 | 2 | Task 4/10 |

---

## Registry RUNNING but NOT in Cron — ALL 6 are ZOMBIES

None of these have matching GPU processes on any server:

| Experiment | Verdict |
|------------|---------|
| eval_pi05_l2norm_k075_long_seed42 | ZOMBIE |
| eval_pi05_random_k085_long_seed43_postfix | ZOMBIE |
| eval_pi05_random_k09_long_seed43_postfix | ZOMBIE |
| eval_pi05_l2norm_k05_spatial_seed42_postfix | ZOMBIE |
| eval_pi05_l2norm_k03_long_seed42_postfix | ZOMBIE |
| eval_xvla_random_k05_spatial_seed43 | ZOMBIE |

---

## Complete Experiment Inventory (13 active)

| # | Model | Method | k | Suite | Seed | Server | GPU |
|---|-------|--------|---|-------|------|--------|-----|
| 1 | OpenVLA | attention | 0.50 | libero_10 | 42 | westd-27271 | 1 |
| 2 | Pi0.5 | l2norm | 0.70 | libero_10 | 42 | cqa1-33015 | 0 |
| 3 | Pi0.5 | attention | 0.70 | libero_10 | 42 | cqa1-33015 | 1 |
| 4 | Pi0.5 | attention | 0.50 | libero_10 | 42 | cqa1-33015 | 2 |
| 5 | OpenVLA | random | 0.70 | object | 42 | westd-41074 | 0 |
| 6 | OpenVLA | random | 0.75 | object | 42 | westd-41074 | 0 |
| 7 | OpenVLA | l2norm | 0.90 | object | 42 | westd-41074 | 1 |
| 8 | OpenVLA | random | 0.75 | libero_10 | 42 | westd-41074 | 1 |
| 9 | OpenVLA | attention | 0.75 | object | 42 | westd-41074 | 2 |
| 10 | OpenVLA | attention | 0.75 | libero_10 | 42 | westd-41074 | 3 |
| 11 | OpenVLA | l2norm | 0.50 | libero_10 | 42 | westd-38929 | 0 |
| 12 | OpenVLA | random | 0.85 | libero_10 | 42 | westd-38929 | 1 |
| 13 | OpenVLA | l2norm | 0.75 | libero_10 | 42 | westd-38929 | 2 |
