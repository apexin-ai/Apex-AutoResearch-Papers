# ops exp70 status check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp70_status_check_20260524T025119_result.json`
- **Structured JSON:** [`5c58abbf44386efbafb7.json`](../../sessions/5c/5c58abbf44386efbafb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## 诊断结果

**状态：已正常完成**（08:30 结束，GPU 已释放，cuda:0 利用率 0% 属正常）

### DD OOD Macro F1 (full, 3 seeds)

| Model | Vanilla | 9-class |
|-------|---------|---------|
| **DeBERTa-v3-large** | 0.898 ± 0.033 | **0.997 ± 0.005** |
| RoBERTa-large (baseline) | 0.927 ± 0.036 | 0.987 ± 0.004 |

### AA OOD Macro F1 (full, 3 seeds)

| Model | Vanilla | 9-class |
|-------|---------|---------|
| **DeBERTa-v3-large** | 0.870 ± 0.022 | **1.000 ± 0.000** |
| RoBERTa-large (baseline) | 1.000 ± 0.000 | 0.946 ± 0.057 |

### 关键发现

假设被**否定**：DeBERTa-v3-large 的 9-class AA (1.000) **高于** vanilla AA (0.870)，与 RoBERTa-large 的模式（9-class AA < vanilla AA）完全相反。这证实 AA OOD 退化是 **RoBERTa-specific** 的，而非大模型的通用 scale 效应。

---
