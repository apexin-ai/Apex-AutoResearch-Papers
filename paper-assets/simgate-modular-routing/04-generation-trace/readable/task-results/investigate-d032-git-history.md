# investigate d032 git history

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d032-git-history_20260514T092259_result.json`
- **Structured JSON:** [`89ffe1b3fd1719b930e5.json`](../../sessions/89/89ffe1b3fd1719b930e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部证据已收集。以下是结论。

---

## 验证结论

### 核心事实

| 版本 | Trainer 类 | class_weights | ga | upsample_minority |
|------|-----------|-------------|-----|-------------------|
| plan-004-implicit (原始) | `UpsamplingTrainer` (.bak 脚本) | N/A (无此参数) | 8 (硬编码 `32//batch_size`) | true |
| **plan-004-v2 (ablation-b)** | `WeightedTrainer` (当前脚本) | **"auto"** | **8** | false |
| plan-004-v3 | `WeightedTrainer` | null | 8 | false |
| plan-004-v4 | `WeightedTrainer` | null | 8 | false |
| **plan-004-v5** | **`WeightedTrainer`** (当前脚本) | **null** | **1** | **true** |

### 关键发现

**1. v5 确实使用了 `WeightedTrainer`，不是标准 HF Trainer。**

v5 的 `train_config.json` 包含 `class_weights` 和 `gradient_accumulation_steps` 字段，这两个参数只存在于当前脚本（有 `WeightedTrainer`），不存在于 .bak 脚本（有 `UpsamplingTrainer`）。因此 v5 使用的是当前脚本的 `WeightedTrainer`。

**2. 但 v5 和 ablation-b 的 `compute_loss` 行为确实不同。**

`WeightedTrainer.compute_loss()` 的逻辑（当前脚本 199-237 行）：

```python
if self._class_weights is not None and sample_indices is not None:
    # 加权路径 — ablation-b (class_weights="auto") 走这里
    weights = [class_weights[route_label] for idx in sample_indices]
    loss = (per_sample_loss * weights).mean()
else:
    # 非加权路径 — v5 (class_weights=null) 走这里
    loss = per_sample_loss.mean()
```

- **v5**：`class_weights=null` → 走 else 分支，各样本等权平均
- **ablation-b (v2)**：`class_weights="auto"` → 走 if 分支，逆频率加权平均（minority class loss 被放大）

**3. v5 与 ablation-b 有三个差异，不是一个：**

| 差异 | v5 | ablation-b (v2) |
|------|-----|-----------------|
| Loss 加权 | 等权 `per_sample_loss.mean()` | 逆频率加权 `(per_sample_loss * weights).mean()` |
| 数据采样 | `WeightedRandomSampler`（过采样少数类）| 默认顺序采样 |
| GA | 1 | 8 |

**4. 即使 v5 不用 class_weights，其 `compute_loss` 也不等于标准 HF Trainer。**

标准 Trainer 用 `CrossEntropyLoss(reduction="mean")`，对所有 token 做全局平均（长序列贡献更多）。WeightedTrainer 先对每个样本内的 token 取平均得到 `per_sample_loss`，再对样本取平均 → 每个样本等权贡献，与序列长度无关。

---

### D032 准确性评估

**D032 的核心声明"v5 用标准 HF Trainer"是不准确的。** v5 和 ablation-b 用的是同一个 `WeightedTrainer` 类，只是参数不同（`class_weights=null` vs `"auto"`）。

**但 D032 说"loss 计算方式不同"这一点是对的** — ablation-b 的逆频率加权确实改变了 loss 的计算方式。

**Reviewer 说"唯一差异是 ga=1 vs ga=8"也不对** — 实际有三个差异（loss 加权、数据采样策略、GA）。

### 需要修正的内容

D032 应改为：
> v5 和 ablation-b 都使用 `WeightedTrainer`（自定义 Trainer 子类），但配置不同：v5 的 `class_weights=null`（等权 loss）+ `upsample_minority=true`（过采样少数类）+ `ga=1`；ablation-b 的 `class_weights="auto"`（逆频率加权 loss）+ `upsample_minority=false` + `ga=8`。三者的组合效应决定了训练差异，而非单一因素。

---
