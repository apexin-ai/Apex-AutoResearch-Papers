# ops check unknown gpu processes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-unknown-gpu-processes_20260515T183629_result.json`
- **Structured JSON:** [`f69cccec394107009dbe.json`](../../sessions/f6/f69cccec394107009dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

## 3 个待确认 GPU 的身份

| 服务器 | GPU | PID | mode | norm | benchmark | seed | output_file |
|--------|-----|-----|------|------|-----------|------|-------------|
| bjb1-32546 | cuda:4 | 134103 | crm_obs_only | default (0.1) | object | 42 | `eval_object_obs_only_default_norm.json` |
| bjb2-28827 | cuda:2 | 117278 | crm_perdof | **0.3** | object | 42 | `eval_object_perdof_norm0p3.json` |
| bjb2-28827 | cuda:3 | 118886 | crm_perdof | **0.3** | object | 42 | `eval_object_perdof_norm03.json` |

### ⚠️ 确认重复

**bjb2-28827 cuda:2 和 cuda:3 是重复实验。** 两者参数完全相同（`--mode crm_perdof --benchmark object --seed 42 --max_correction_norm 0.3`），唯一区别是输出文件名（`norm0p3` vs `norm03`）。已按要求未 kill 任何进程。

---

## bjb1-32546 全部 GPU 进程

| GPU | PID | mode | norm | benchmark | seed | 进度 |
|-----|-----|------|------|-----------|------|------|
| cuda:0 | 121334 | crm_obs_only | 0.03 | object | 42 | 运行中 |
| cuda:1 | 111718 | vla_only (mean) | — | object | 43 | 2/10 tasks |
| cuda:2 | 114673 | crm_scalar | 0.1 | object | 43 | ~1.5/10 tasks |
| cuda:3 | 118214 | crm_obs_only | 0.2 | object | 43 | 1/10 tasks |
| cuda:4 | 134103 | crm_obs_only | default(0.1) | object | 42 | 运行中 |
| cuda:5 | 127741 | crm_perdof | 0.2 | object | 42 | 运行中 |

- **vla-only-object-seed43** 已完成：overall 12.0% (12/100)，结果在 `eval_object_vla_only_seed43.json`

---

## bjb1-18228 进程状态

| GPU | PID | mode | norm | benchmark | seed | 进度 |
|-----|-----|------|------|-----------|------|------|
| cuda:0 | 390936 | crm_perdof | default(0.1) | object | 42 | 运行中 |
| cuda:1 | 365930 | crm_perdof | 0.1 | object | 43 | ~3-4/10 tasks |
| cuda:2 | 356495 | crm_obs_only | 0.1 | object | 43 | 5/10 tasks |
| cuda:3 | 356701 | reconvla | — | object | 43 | 运行中 |

**无进程但有日志的 seed=43 实验（可能已崩溃）：**
- `argmin-object-seed43`: 停在 5/10 tasks，无对应 GPU 进程
- `obs-only-spatial-seed43`: 停在 2/10 tasks，无对应 GPU 进程

---
