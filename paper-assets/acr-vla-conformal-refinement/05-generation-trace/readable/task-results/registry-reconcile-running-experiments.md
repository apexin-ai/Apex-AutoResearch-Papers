# registry reconcile running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_reconcile-running-experiments_20260528T063228_result.json`
- **Structured JSON:** [`00a2b364458e47bd4285.json`](../../sessions/00/00a2b364458e47bd4285.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 确认 **20 个 RUNNING**。全部补登完成。

## 汇总

| 服务器 | 实验数 | GPU 分配 | exp_id 列表 |
|--------|--------|----------|-------------|
| **bjb1-18228** | 2 | GPU 0, 2 | `pi05-crm-always-on-long-s43` (PID 982389, cuda:0), `pi05-crm-always-on-long-s44` (PID 983106, cuda:2) |
| **bjb1-32546** | 6 | GPU 0-5 | `pi05-crm-always-on-goal-s43` (510343, cuda:0), `pi05-crm-always-on-goal-s44` (510709, cuda:1), `pi05-crm-always-on-object-s44` (511001, cuda:2), `eval-random-selection-object-seed43-v2` (550561, cuda:3), `eval-ksweep-k20-obs-object-s44` (550841, cuda:4), `eval-ksweep-k20-obs-obj-s43` (558360, cuda:5) |
| **bjb2-28827** | 6 | GPU 0-5 | `eval-k2-tau045-spatial-s42-bjb2` (120283, cuda:0), `eval-supp-adapt-tau025-spatial-s46` (121287, cuda:1), `eval-supp-long-vla-only-s42` (123017, cuda:2), `eval-supp-long-vla-only-s44` (124427, cuda:3), `smolvla-tau025-spatial-s42` (112969, cuda:4), `smolvla-tau020-spatial-s42` (113251, cuda:5) |
| **cqa1-32758** | 6 | GPU 0-5 | `smolvla-adapt-tau015-object-s42-cqa1` (276842, cuda:0), `smolvla-adapt-tau015-object-s43-cqa1` (277118, cuda:1), `smolvla-adapt-tau015-object-s44-cqa1` (278891, cuda:2), `eval-supp-spatial-adapt-tau025-s47` (280038, cuda:3), `eval-supp-spatial-k2mean-s47` (281459, cuda:4), `eval-supp-long-vla-only-s46` (295725, cuda:5) |

**合计 20 个实验 / 20 GPU RUNNING**。bjb1-18228 的 GPU 1 和 GPU 3 空闲（共 4 卡只用了 2 张）。11 个从 PREPARING 推进，9 个从 DONE 重置后推进。

---
