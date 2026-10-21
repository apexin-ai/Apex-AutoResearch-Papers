# diagnose plan 002 v3 completion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-v3-completion_20260514T060508_result.json`
- **Structured JSON:** [`9a4f79b90ca42d0c7d6d.json`](../../sessions/9a/9a4f79b90ca42d0c7d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan-002-formal-v3 验收

### 训练状态
- 完成/崩溃: **COMPLETE** (156/156 steps, ~16 min)
- Sentinel: **存在** (2026-05-14T14:01:17)
- Epochs 完成: **3**
- Early stopping counter: **2/2** (patience exhausted, `should_training_stop=true`)

### Loss 曲线

| Epoch | train_loss (avg) | eval_loss |
|-------|-----------------|-----------|
| 1 | ~4.49 | 1.7793 |
| 2 | ~3.92 | 1.9957 |
| 3 | ~3.82 | 1.5083 |

train_loss 全程在 3.5–5.2 波动，极高，模型基本未学到任务格式。eval_loss 虽有下降但对分类指标无帮助。

### 分类指标（关键）
- Overall accuracy: **0.0000**
- Balanced accuracy: **0.0000**
- F1 macro: **0.0000**

Per-class:
| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| deterministic | 0.0 | 0.0 | 0.0 |
| internal | 0.0 | 0.0 | 0.0 |

### Confusion Matrix
```
labels: [internal, deterministic]
[[  0,   0],    ← true=internal (0 samples in eval)
 [390,   0]]   ← true=deterministic (390 samples, ALL predicted as internal)
```

### Per-task Accuracy
所有 11 个 task 均为 **0.000**（30 samples each, find-non-living-thing 90 samples）

### 关键判断
- **internal recall > 0?** **NO** — eval set 中 internal 样本数为 0，无法评估
- **退化问题解决?** **NO** — 比 dryrun 更严重，完全崩溃
- **与 dryrun 对比:** 全面恶化。模型将所有 390 个 deterministic 样本预测为 internal，0% 准确率

### 根因分析
1. **eval set 只包含 deterministic 样本**（390 个），无 internal 样本 → eval 数据分割有问题
2. **模型将所有样本预测为同一类 (internal)** → 模型没有学到分类边界
3. **train_loss ~4.0 持续居高** → 模型可能在拟合错误的 token 位置（label format/template 问题），或 class_weights 导致 loss scale 异常
4. Adapter 文件已保存（~25MB），但模型本身无分类能力

---
