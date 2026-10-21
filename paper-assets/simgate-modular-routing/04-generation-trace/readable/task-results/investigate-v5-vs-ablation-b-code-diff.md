# investigate v5 vs ablation b code diff

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_v5-vs-ablation-b-code-diff_20260514T085814_result.json`
- **Structured JSON:** [`d21e69d56b42e8837691.json`](../../sessions/d2/d21e69d56b42e8837691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已经足够做出结论了。

---

## 调查结果

### 1. 代码确实有变更

`implicit_router_sft.py` 在 ablation-b（05:37 UTC）和 v5（08:03 UTC）之间被修改。`.bak` 文件保留了 ablation-b 使用的原始版本。修改时间 06:40 UTC。

### 2. 具体 diff（4 类关键变更）

| 变更 | ablation-b（.bak） | v5（当前） | 影响 |
|------|-------------------|-----------|------|
| **Trainer 类** | `UpsamplingTrainer` | `WeightedTrainer`（自定义 `compute_loss`） | **高** |
| **Gradient accumulation** | `max(1, 32 // batch_size)` = **8**（batch=4时） | `getattr(args, "ga", 1)` = **1** | **极高** |
| **Loss 计算** | HF 标准 CE（按 token 平均） | 自定义 per-sample mean → 再取 batch mean | **中** |
| **Data split** | task_type 分层 | episode-level (task_type, variation) 分层 | 低 |
| **wandb** | `"wandb"` | `"none"` | 无 |

### 3. 根因：Effective batch size 从 32 暴降到 4

训练日志对比：

| | ablation-b | v5 |
|---|---|---|
| per_device_batch | 4 | 4 |
| gradient_accumulation | **8** | **1** |
| effective batch | **32** | **4** |
| steps/epoch | 55 | 435 |
| epoch 2 train loss | ~0.35 | **0.09** |
| final eval loss | 0.361 | 0.263 |

v5 的 train loss 降到 0.09 — **严重过拟合**。模型记住了训练数据的 token 分布（logit accuracy 高达 74.5%），但丧失了 generation 泛化能力（internal_recall 仅 26.7%）。

### 4. 次要因素：compute_loss 语义变化

即使不传 `--class_weights`，`WeightedTrainer.compute_loss` 也改变了 loss 的加权方式：HF 默认按 token 数量加权每个样本，自定义版本给每个样本等权重。在 internal/deterministic 样本长度差异大时，这会改变训练动态。

### 5. 结论

**logit-generation gap 的根因是代码 bug，不是"episode-level labels 粒度限制"。**

重构 Trainer 时，`gradient_accumulation_steps` 的默认值从 `max(1, 32//batch_size)` 变成了硬编码的 `1`，导致 effective batch size 缩小 8 倍。这是一个非故意的行为变更（代码把 ga 暴露为命令行参数，但默认值不同于旧逻辑）。

要复现 ablation-b 的结果，v5 应该传 `--gradient_accumulation_steps 8`（或把默认值改回 `max(1, 32 // batch_size)`）。

---
