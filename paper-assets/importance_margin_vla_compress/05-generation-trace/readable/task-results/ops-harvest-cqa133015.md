# ops harvest cqa133015

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-cqa133015_20260524T080035_result.json`
- **Structured JSON:** [`ad8dfa049958f2ad0f37.json`](../../sessions/ad/ad8dfa049958f2ad0f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete status report:

---

## cqa1-33015

### Currently Running

| GPU | Experiment | Progress | ETA |
|-----|-----------|----------|-----|
| 1 | `eval_pi05_random_k03_spatial_seed42_postfix` | T9/10, 450/500 eps (90%), interim SR=43.8% | ~15min |
| 2 | `eval_pi05_random_k095_spatial_seed42_postfix_v2` | T5/10, 250/500 eps (50%), interim SR=84.0% | ~60min |
| 3 | `eval_pi05_l2norm_k05_spatial_seed42_postfix` | T4/10, 200/500 eps (40%), interim SR=71.5% | ~75min |

GPU 0: IDLE

### Completed Results (harvested from eval_results/)

| Experiment | Suite | SR | Episodes |
|-----------|-------|-----|----------|
| pi05_random_k0.50_spatial_seed42 | spatial | **71.8%** | 500 |
| pi05_random_k0.70_spatial_seed42 | spatial | **73.8%** | 500 |
| pi05_random_k0.85_spatial_seed42 | spatial | **60.8%** | 500 |
| pi05_random_k0.90_spatial_seed42 | spatial | **53.4%** | 500 |
| pi05_l2norm_k0.85_spatial_seed42 | spatial | **88.4%** | 500 |
| pi05_l2norm_k0.95_spatial_seed43 | spatial | **98.0%** | 500 |
| pi05_random_k0.95_object_seed42 | object | **74.0%** | 500 |
| pi05_random_k0.90_object_seed42 | object | **9.0%** | 500 |
| pi05_random_k0.70_object_seed42 | object | **74.0%** | 500 |

---

## westd-38929

### Currently Running

| GPU | Experiment | Progress | ETA |
|-----|-----------|----------|-----|
| 0 | `eval_pi05_random_k09_goal_seed42_postfix` | T5/10, 250/500 eps (50%), interim SR=54.8% | ~45min |
| 1 | `eval_pi05_random_k085_goal_seed42_postfix` | T4/10, 200/500 eps (40%), interim SR=30.5% | ~60min |
| 2 | `eval_pi05_random_k07_goal_seed42_postfix` | T5/10, 250/500 eps (50%), interim SR=78.0% | ~40min |

GPU 3: IDLE

### Completed X-VLA Results (recently finished)

| Experiment | Suite | Mode | k | SR | Episodes |
|-----------|-------|------|---|-----|----------|
| xvla_prune_k0.3_goal | goal | l2_norm | 0.3 | **0.2%** | 500 |
| xvla_prune_k0.5_goal | goal | l2_norm | 0.5 | **59.0%** | 500 |
| xvla_prune_k0.7_goal | goal | l2_norm | 0.7 | **51.8%** | 500 |
| xvla_prune_k0.85_goal | goal | random | 0.85 | **60.4%** | 500 |
| xvla_prune_k0.3_spatial | spatial | l2_norm | 0.3 | **31.2%** | 500 |
| xvla_prune_k0.5_spatial | spatial | l2_norm | 0.5 | **58.8%** | 500 |
| xvla_prune_k0.7_spatial | spatial | l2_norm | 0.7 | **72.8%** | 500 |
| xvla_prune_k0.85_spatial | spatial | random | 0.85 | **68.2%** | 500 |
| xvla_prune_k0.5_10 | libero_10 | l2_norm | 0.5 | **44.6%** | 500 |
| xvla_prune_k0.85_10 | libero_10 | random | 0.85 | **35.0%** | 500 |
| xvla_random_k05_spatial_seed43 | spatial | random | 0.5 | **72.6%** | 500 |

---

**Key observations:**
- The GPU 2/3 experiments on cqa1 (random k=0.95 spatial, l2norm k=0.5 spatial) are **still running** (not completed as expected) — they were launched via nohup at ~15:12 today and are at 50%/40% progress respectively.
- Interim SR on GPU 2 (random k=0.95 spatial) is tracking high at **84.0%** after 5 tasks.
- The k=0.90 object result (9.0%) on cqa1 looks anomalous compared to k=0.70 (74%) and k=0.95 (74%).
- westd-38929 GPU 3 is idle — available for new work. The xvla_l2norm_k03_goal just finished (SR=0.2%, catastrophic).

---
