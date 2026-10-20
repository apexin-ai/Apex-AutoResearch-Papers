# code exp27 mean pooling

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp27-mean-pooling_20260520T150040_result.json`
- **Structured JSON:** [`f1bd1be98e6f0a824c24.json`](../../sessions/f1/f1bd1be98e6f0a824c24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp27 完成。

## 结果

**假设被拒绝。** Mean pooling E2E 在所有指标、所有 seed 上均获得 **1.0 F1**，零方差。

| 方法 | IID | DD OOD full | AA OOD full | FITD |
|------|-----|-------------|-------------|------|
| **exp27 MeanPool E2E** | **1.000** | **1.000** | **1.000** | **1.000** |
| exp18 BiGRU E2E | 1.000 | 1.000 | 0.997 | - |
| exp26 BiGRU Frozen | 1.000 | 0.997 | 0.972 | 1.000 |
| exp13 MeanPool Frozen | - | 0.990 | 0.962 | - |

**关键发现**：Temporal modeling（BiGRU）在 E2E 设置下不是必要的。End-to-end fine-tuning 才是决定性因素——解冻 encoder 后，即使最简单的 mean pooling 也能在所有当前 OOD 基准上达到满分。BiGRU 在 E2E 设置中相比 mean pooling 没有任何增益。

产出：
- 结果文件：`results/exp27_mean_pooling.json`（服务器端）
- Checkpoints：`checkpoints/exp27_mean_pooling/seed{42,123,456}/`
- Registry：`exp27_mean_pooling` → DONE (negative)

---
