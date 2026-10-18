# deploy westd41074 gpu01 next batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu01_next_batch_20260525T101837_result.json`
- **Structured JSON:** [`b6530973ccff1190bdb7.json`](../../sessions/b6/b6530973ccff1190bdb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments confirmed running and producing output:

**Completed results collected:**
| Experiment | SR | Episodes |
|---|---|---|
| Random k=0.9 Goal | **79.6%** (398/500) | 500 |
| Random k=0.9 Spatial | **79.8%** (399/500) | 500 |

**New experiments deployed on westd-41074:**
| GPU | Experiment | Status |
|---|---|---|
| GPU 0 | `eval_openvla_attn_k09_object_seed42` — Attention pruning 256→230 tokens | Running, Task 1/10 started |
| GPU 1 | `eval_openvla_l2norm_k05_goal_seed42` — L2norm pruning 256→128 tokens | Running, Task 1/10 started |

Estimated runtime ~4h each (based on prior runs at ~2.5 eps/min). The Attention k=0.9 Object result fills the last missing cell in the crossover table. The L2norm k=0.5 Goal fills a degradation curve midpoint.

---
