# exp cross task transfer 116

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-task-transfer-116_20260523T073531_result.json`
- **Structured JSON:** [`e95be166540294887c2b.json`](../../sessions/e9/e95be166540294887c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。完整结果汇总：

## 结果

### Llama-3.1 (32 layers)
| 指标 | 值 |
|------|-----|
| Same-task baseline | ~1.0 所有层 |
| Peak C→XNLI | **1.0** (大多数层), 最低 **0.8725** (layer 11) |
| Peak X→Conf | **1.0** (大多数层), 最低 **0.9945** (layers 24-27) |
| Transfer 几乎完美，微小 dip 在 layer 11 |

### Qwen3 (36 layers)
| 指标 | 值 |
|------|-----|
| Same-task baseline | ~1.0 所有层 |
| C→XNLI 最低点 | **0.5625** (layer 23) |
| C→XNLI dip 区间 | layers 18-24 (0.56-0.98) |
| X→Conf | **~1.0** 所有层（不对称！）|

### Gemma2 (42 layers)
| 指标 | 值 |
|------|-----|
| Same-task baseline | ~1.0 所有层 |
| C→XNLI 最低点 | **0.5325** (layer 15) |
| C→XNLI dip 区间 | layers 14-22 (0.53-0.76) |
| X→Conf 最低点 | **0.8145** (layer 13) |
| X→Conf dip 区间 | layers 13-21 (0.81-0.98) |

## 结论

**强烈支持 piggyback 假说，但有重要 nuance：**

1. **早期层和晚期层：跨任务迁移近乎完美（~1.0）** — 两个任务共享同一个跨语言子空间
2. **中间层出现迁移断裂** — 特别是 Gemma2 (layers 14-22) 和 Qwen3 (layer 23)，Conflict→XNLI 准确率跌至接近 chance level (0.53)
3. **显著不对称**：XNLI→Conflict 迁移始终优于 Conflict→XNLI，说明 conflict 任务的语言表征在中间层发生了更大的变形（任务特异性加工）
4. **Llama 最稳定**，迁移几乎不受影响（最低 0.87）

解读：冲突信号确实搭载在通用跨语言子空间上（大部分层完美迁移），但在中间处理层，conflict 任务对语言表征做了局部变形——这恰恰可能是 conflict detection 发生的层。探针权重已保存至 `data/{model}/probe_weights/`，可供 Exp 2 使用。

---
