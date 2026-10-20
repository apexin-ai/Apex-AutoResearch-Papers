# code bugfix deploy

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bugfix-deploy_20260512T113728_result.json`
- **Structured JSON:** [`68c7420ec583ee9fa350.json`](../../sessions/68/68c7420ec583ee9fa350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 1. Sanity Check 输出

```
=== Sanity Check: Greedy Diversity Selection ===
Total points: 100, Selected: 20
Cluster distribution of selected points: {0: 5, 1: 5, 2: 5, 3: 5}
All clusters covered: True
Balance ratio (max/min): 1.0 (want < 3.0)
Mean dist to centroid — selected: 8.29, random: 7.15
✅ PASS: Selection covers all clusters with reasonable balance
```

4 个 cluster 各选 5 个点，完美均衡（ratio=1.0）。选中点的平均距质心距离 8.29 > 随机 7.15，说明选择偏向外围（覆盖更广）。

### 2. meta.json

```json
{
  "tokenizer": "/root/models/Qwen/Qwen3-1.7B",
  "seq_len": 512,
  "num_train": 242666,
  "num_ref": 5000,
  "num_test": 583,
  "num_rare_positive": 4962,
  "seed": 42
}
```

### 3. Rare n-gram labels 分布

- **4962/5000 positive (99.2%)**，38 negative
- 不再是 5000/5000 全正，bug 已修复
- 正比例高是因为 512-token 的 chunk 很长，几乎每段都会包含至少一个 rare trigram — 这是符合预期的

### 4. 数据文件

| 文件 | 大小 |
|------|------|
| train_chunks.pt | 342M (237,666 chunks，扣除 5000 ref) |
| ref_chunks.pt | 7.2M (5,000 chunks) |
| ref_rare_labels.pt | 6.2K |
| test_chunks.pt | 861K (583 chunks) |
| meta.json | 171B |

无错误。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "tokenizer": "/root/models/Qwen/Qwen3-1.7B",
    "seq_len": 512,
    "num_train": 242666,
    "num_ref": 5000,
    "num_test": 583,
    "num_rare_positive": 4962,
    "seed": 42
  }
}
```

</details>

---
