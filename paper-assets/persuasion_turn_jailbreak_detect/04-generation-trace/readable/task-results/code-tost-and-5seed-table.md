# code tost and 5seed table

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tost-and-5seed-table_20260521T093920_result.json`
- **Structured JSON:** [`ab3fe9c70800d36f4a3d.json`](../../sessions/ab/ab3fe9c70800d36f4a3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 5-seed F1 列表 (seeds: 42, 123, 456, 789, 1000)

```
DD    9-class [1.0000, 1.0000, 0.9904, 1.0000, 1.0000]  scrambled [0.9904, 1.0000, 1.0000, 1.0000, 1.0000]
AA    9-class [0.9904, 0.9350, 0.9904, 0.9715, 0.9715]  scrambled [0.8913, 0.9904, 0.9715, 0.9904, 0.9904]
FITD  9-class [1.0000, 1.0000, 1.0000, 1.0000, 0.9904]  scrambled [1.0000, 1.0000, 1.0000, 1.0000, 0.9904]
```

### TOST 等价性检验 (paired, ε=0.05)

| Condition | mean_diff | SE | p_TOST | Cohen's d | Equivalent? |
|-----------|-----------|------|--------|-----------|-------------|
| DD | −0.0000 | 0.0030 | 0.0000 | −0.0011 | **YES** |
| AA | +0.0050 | 0.0263 | 0.0810 | 0.0843 | **NO** |
| FITD | 0.0000 | 0.0000 | 0.0000 | 0.0000 | **YES** |

**DD 和 FITD** 统计等价（p < 0.05）。**AA** 未通过 TOST（p=0.081），主要受 seed 42 的 scrambled 低值（0.891）拖累——方差大导致 SE 较大，n=5 下检验力不足以在 ε=0.05 下拒绝。不过 Cohen's d=0.084 属于 negligible effect size。

结果已保存到 `results/exp39_tost_analysis.json`。

---
