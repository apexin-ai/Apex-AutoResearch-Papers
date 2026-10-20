# monitor scale 14b progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_scale_14b_progress_check_20260522T224823_result.json`
- **Structured JSON:** [`998a8ee4a61af3be06fa.json`](../../sessions/99/998a8ee4a61af3be06fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

## 1.4B Scale 实验进度汇总

### westd-17855 (6× RTX PRO 6000 Blackwell 98GB)

| GPU | exp_id | 进度 | 当前 Gen | 剩余 Gens | 预估剩余时间 |
|-----|--------|------|----------|-----------|-------------|
| cuda:0 | t15_a060_s42_fp32_v2 | 12/15 | gen_12 (training) | 3 | ~3h |
| cuda:1 | t15_a050_s42_fp32_v3 | 12/15 | gen_12 (training) | 3 | ~3h |
| cuda:2 | t10_a075_s43_fp32 | 2/10 | gen_2 (training) | 8 | ~9h |
| cuda:3 | t10_a060_s43_fp32 | 2/10 | gen_2 (training) | 8 | ~9h |
| cuda:4 | t10_a045_s42_fp32 | 9/10 | gen_9 (starting) | 1 | ~1h |
| cuda:5 | t15_a045_s42_fp32 | 10/15 | gen_10 (training) | 5 | ~6h |

**GPU 利用率:**

| GPU | Util | VRAM |
|-----|------|------|
| cuda:0 | 99% | 31.5/95.6 GB |
| cuda:1 | 99% | 31.5/95.6 GB |
| cuda:2 | 97% | 27.1/95.6 GB |
| cuda:3 | 97% | 27.1/95.6 GB |
| cuda:4 | 89% | 30.4/95.6 GB |
| cuda:5 | 99% | 31.5/95.6 GB |

**磁盘:** 319G/350G used (91%) — **剩余 32G，需关注**

---

### westd-19828 (2× RTX PRO 6000 Blackwell 98GB)

| GPU | exp_id | 进度 | 当前 Gen | 剩余 Gens | 预估剩余时间 |
|-----|--------|------|----------|-----------|-------------|
| cuda:0 | t15_a075_s42_fp32 | 9/15 | gen_9 (starting) | 6 | ~7h |
| cuda:1 | t10_a050_s43_fp32 | 2/10 | gen_2 (training) | 8 | ~9h |

**GPU 利用率:**

| GPU | Util | VRAM |
|-----|------|------|
| cuda:0 | 89% | 30.4/95.6 GB |
| cuda:1 | 96% | 27.1/95.6 GB |

**磁盘:** 141G/250G used (57%) — 剩余 110G，充足

---

**备注:**
- 每 gen 耗时约 ~67min（基于 gen 间时间戳差值估算）
- "training" = 已有 `synthetic_data` + `trainer` 但无 `metrics.json`；"starting" = gen 目录已创建但为空
- **17855 磁盘 91%**，8 个实验中 4 个还有 7-8 gens 要跑，可能不够用（C007 约束）

---
