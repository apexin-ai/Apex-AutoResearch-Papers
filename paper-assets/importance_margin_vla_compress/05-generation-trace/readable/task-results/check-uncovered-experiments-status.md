# check uncovered experiments status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_uncovered-experiments-status_20260521T175243_result.json`
- **Structured JSON:** [`099847cf68442fc7d651.json`](../../sessions/09/099847cf68442fc7d651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

## 实验状态汇总

| 服务器 | 实验 | 状态 | SR | 进度/备注 |
|--------|------|------|-----|-----------|
| **westd-38929** GPU0 | smolvla baseline seed43 | **COMPLETED** | **59.6%** (298/500) | 结果已保存 |
| **westd-38929** GPU1 | smolvla random k=0.95 seed43 | **RUNNING** | ~0.2% | Task 9/10, ep 12/50 (Task 0-7完成, 仅Task3有1/50) |
| **westd-38929** GPU2 | smolvla random k=0.50 seed43 | **RUNNING** | 0% | Task 8/10, ep 39/50 (Task 0-6全0%) |
| **cqa1-33015** GPU0 | smolvla baseline seed42 | **COMPLETED** | **57.2%** (286/500) | 文件: official_libero_object_baseline.json |
| **cqa1-33015** GPU1 | smolvla random k=0.95 seed42 | **COMPLETED** | **0.0%** (0/500) | 文件: smolvla_official_random_k095_object_seed42.json |
| **cqa1-33015** GPU2 | smolvla l2norm k=0.50 seed42 | **COMPLETED** | **0.0%** (0/500) | 文件: smolvla_official_l2norm_k050_object_seed42.json |
| **westd-27271** GPU0 | openvla l2norm k=0.5 seed43 | **COMPLETED** | **39.2%** (196/500) | 文件: openvla_l2norm_prune_k05_object_seed43.json |

### 额外发现

- **cqa1-33015** 当前 4 个 GPU 正在跑 registry 未列出的实验：random k=0.9/k=0.5 + l2norm k=0.7/k=0.9 (均 seed42)
- **westd-27271** GPU1 当前在跑 **训练** 任务 (`train_openvla_smart_compress_m32`)，不是 eval
- **westd-38929** GPU1/GPU2 的两个 RUNNING 实验预计再 ~1-2 小时完成（每 task ~5min，剩余 ~3 tasks）
- pruning 实验 SR≈0% 符合预期（pixel-shuffle cliff-edge）

---
