# ops ug progress and base gar

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ug_progress_and_base_gar_20260519T025947_result.json`
- **Structured JSON:** [`90bf527054032f8aef8f.json`](../../sessions/90/90bf527054032f8aef8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Part 1: UG 训练进度

| 指标 | 值 |
|---|---|
| 当前位置 | Epoch 1, micro-step 900 |
| Global step | ~1113 / 3000 |
| 进度 | **~37%** |
| 已运行 | ~2h 20min（08:43 开始） |
| 预估速率 | ~8 global steps/min |
| 剩余 global steps | ~1887 |
| **预估剩余时间** | **~3h 55min（约 15:00 完成）** |

训练状态正常：
- Gate 均值从 epoch 0 的 ~0.97 缓降至 epoch 1 的 ~0.96
- 最低 gate 层：L3=0.793, L5=0.809（一直是最低的两层）
- 最高 gate 层：L27=1.000, L2/L4/L26=0.996
- L_GAR 很小（0.000-0.007），L_DIV 几乎为零
- 显存稳定在 53.1GB

### Part 2: Base model GAR on ultrachat

**无法在当前条件下完成。**

- GPU：UG 训练占用 70GB/98GB，尝试 GPU 推理 OOM
- CPU：7B 模型 forward pass（含 output_attentions=True）× 50 组对话，预估需 50-150 分钟，远超 10 分钟限制，已终止

**建议**：等 UG 训练完成（预计 ~15:00 北京时间）后用 GPU 跑，几分钟即可完成。

---
