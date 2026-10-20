# analysis d073 oracle bug repro

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-oracle-bug-repro_20260516T041310_result.json`
- **Structured JSON:** [`8b05608bbf91f64a6d1f.json`](../../sessions/8b/8b05608bbf91f64a6d1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Oracle Bug Audit

**无 bug。** Identical oracle F1 是 window size=5 导致的数学恒等，不是变量泄漏。

### 根因分析

数据特征：几乎所有 window 恰好有 **5 个 action types**（min=3, max=5, mean=5.0）。这导致 n-gram ratio 极度量化：

| n-gram | 可能的 ratio 值 | 分布 |
|--------|----------------|------|
| 2-gram | 0, 0.50, 0.667*, 0.75, 1.0 | 5 个离散值 |
| 3-gram | 0, 0.667, 1.0 | 3 个离散值 |

*（来自极少数 length-4 window）

Oracle 搜索结果：
- **2-gram oracle**: threshold=0.70 → 实际选中 ratio≥0.75 的 window（16,265 + 20,786 = **37,051** 个）
- **3-gram oracle**: threshold=0.00 → 实际选中 ratio>0 的 window（25,183 + 11,868 = **37,051** 个）

**数学恒等**：对 length-5 序列，「存在重复 3-gram」⟺「2-gram repeat ratio ≥ 0.75」。证明：

- 有重复 3-gram → 前4元素全等（如 [a,a,a,a,e]）或后4全等 或 交替模式（[a,b,a,b,a]）→ 2-gram ratio ≥ 0.75 ✓
- 2-gram ratio ≥ 0.75 → 3个连续 bigram 相同 → 必然产生重复 trigram ✓

因此两个条件选中的是 **完全相同的 37,051 个 window**，所有指标自然一致。

### 修正后数字

原始代码结果就是正确的：

```
修正后 2-gram oracle: threshold=0.70, all_f1=0.5517, conf2_f1=0.6143
修正后 3-gram oracle: threshold=0.00, all_f1=0.5517, conf2_f1=0.6143
```

### 论文影响

分别报告 2-gram 和 3-gram oracle 是 misleading——在 window=5 的条件下它们数学等价。建议论文中：
1. 只报 "n-gram cycle detector (oracle)" 一行，注明 2/3-gram 退化为等价
2. 或添加脚注说明 window=5 导致的量化效应

完整 threshold-F1 表格已在服务器 `/tmp/oracle_verify.log` 中保存。

---
