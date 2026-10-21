# verify w2 seed grouping logic

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_w2_seed_grouping_logic_20260515T194029_result.json`
- **Structured JSON:** [`4160aedf491776b6be72.json`](../../sessions/41/4160aedf491776b6be72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析完成。

## 结果

### 1. seed group 分配的具体代码逻辑

`get_seed_ids()` 直接返回 `sample_id` 列。`extract_features.py` 中 `sample_id` 是**全局递增计数器**（不是 per-depth），结果：
- depth 0: sample_id 0–4999
- depth 1: sample_id 5000–9999
- depth 2: sample_id 10000–14999
- depth 3: sample_id 15000–19999

`assign_groups()` 将 15000 个唯一 sample_id（depth 1–3）按顺序切 10 块，每块 1500 个。导致：
- Group 0–2: **纯 depth 1**
- Group 3, 6: depth 交界混合
- Group 7–9: **纯 depth 3**

### 2. features.jsonl 字段

`{"depth": int, "sample_id": int(全局), mean_ppl, var_ppl, ...}` — 19 个统计特征。

### 3. 数据生成是无条件的

`generate_next_depth.py` 文档注释明确写道：**"seed_id 为独立递增编号（0..num_samples-1），不与上一代数据对应。"** 生成从 BOS token 开始，无 seed 文章输入。depth 0 是 Wikipedia 原文，depth 1+ 是 LoRA 模型无条件生成。不存在跨 depth 的 seed 文章对应关系。

### 4. 结论：LOGO 逻辑有 bug

**有两层问题：**

- **Bug（技术层）**：`sample_id` 是全局计数器，LOGO groups 严重偏向特定 depth。留出 group 0 = 测试集全是 depth 1；留出 group 9 = 测试集全是 depth 3。这不是 seed-stratified LOGO，而是 depth-correlated block split。
- **语义层**：由于生成是无条件的，"同一 seed 跨 depth"的假设本就不成立。即使修复了 bug，LOGO 测试的也是"不同随机子集间的分类稳定性"，不是"跨 seed article 的泛化"。

**结果可能碰巧还行**（因为 RF 在每个 fold 仍能见到所有 depth 的训练样本），但 fold 间 variance 会偏高，且含义与论文声称的不符。

### 5. 修复建议

**代码修复**（最小改动，改 `get_seed_ids`）：

```python
def get_seed_ids(df_syn):
    # 始终使用 per-depth sequential assignment
    # 因为生成是无条件的，sample_id 无跨 depth 语义
    seed_ids = np.zeros(len(df_syn), dtype=int)
    for d in sorted(df_syn["depth"].unique()):
        mask = (df_syn["depth"] == d).values
        seed_ids[mask] = np.arange(mask.sum())
    return seed_ids
```

这样每个 depth 内 seed_id 0–4999，groups 会 depth-balanced（每组在每个 depth 各有 ~500 样本）。

**论文需澄清**：由于数据是无条件生成的，LOGO 验证的是"分类器在不同随机子集间的稳定性"，而非"跨 seed domain 的泛化能力"。建议将 "seed-stratified LOGO" 改为 "block-stratified LOGO" 或类似表述。

---
