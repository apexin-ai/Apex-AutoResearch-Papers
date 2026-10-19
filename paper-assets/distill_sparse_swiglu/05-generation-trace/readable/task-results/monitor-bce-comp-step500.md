# monitor bce comp step500

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bce_comp_step500_20260515T181059_result.json`
- **Structured JSON:** [`3fc1e95b58eed0818d01.json`](../../sessions/3f/3fc1e95b58eed0818d01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

⚠️ **SPARSITY_HIGH: 0.557，建议调 reg_weight 重跑**

Step 500 关键指标：
- `sparsity=0.557`，`total_loss=0.6508`，`bce_loss=0.6417`，`comp_loss=0.0035`，`reg=0.0056`
- Phase 2（joint training）已在 step 201 启动，运行正常

Sparsity 趋势：

| Step | Sparsity |
|------|----------|
| 250  | 0.561    |
| 300  | 0.557    |
| 400  | 0.555    |
| 500  | 0.557    |

下降速度极慢，step 300→500 之间基本停滞在 0.555-0.557，未能有效收敛到 target 0.5。当前 reg_weight 的正则化力度不足以继续压低 sparsity。

---
