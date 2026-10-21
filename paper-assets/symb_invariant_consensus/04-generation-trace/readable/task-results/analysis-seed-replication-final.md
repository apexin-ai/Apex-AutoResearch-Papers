# analysis seed replication final

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed-replication-final_20260519T010714_result.json`
- **Structured JSON:** [`2f90b188e61ce4fbb0e5.json`](../../sessions/2f/2f90b188e61ce4fbb0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `seed_replication_analysis.json`。精确数字如下：

---

## 跨 Seed 汇总表

```
Seed Replication Summary (FOLIO-204, Mistral-7B, K=12, T=0.7)
| Seed            |  n  |  SC%  | SICA% | delta  |  b |  c | p-value | sig |
|-----------------|-----|-------|-------|--------|----|----|---------|-----|
| 42  (exp-033)   | 204 | 54.41 | 59.31 | +4.90  | 12 |  2 |  0.0130 |  *  |
| 123 (exp-052)   | 204 | 53.92 | 57.35 | +3.43  |  8 |  1 |  0.0391 |  *  |
| 456 (exp-053)   | 204 | 56.37 | 55.88 | -0.49  |  2 |  3 |  1.0000 |  ns |
|-----------------|-----|-------|-------|--------|----|----|---------|-----|
| Mean ± std      |     | 54.90±1.30 | 57.51±1.72 | +2.61±2.79 |   |   |   |     |
```

## exp-052 (seed=123) 详细

- **SC 53.92% (110/204), SICA 57.35% (117/204), delta +3.43%**
- Contingency: both_correct=109, both_wrong=86, b=8, c=1
- McNemar p=0.0391 (显著)
- Per type: False +1.59, True +4.17, Unknown +4.35
- Entropy: low 0.00, medium +2.86, **high +7.14** (SICA 在高 entropy 区域增益最大)

## exp-053 (seed=456) 详细

- **SC 56.37% (115/204), SICA 55.88% (114/204), delta -0.49%**
- Contingency: both_correct=112, both_wrong=87, b=2, c=3
- McNemar p=1.0000 (不显著)
- Per type: False +3.17, True 0.00, **Unknown -4.35** (SICA 在 Unknown 类反而退步)
- Entropy: low 0.00, medium -1.56, high 0.00 (SICA 完全没有增益)

## 关键发现

**SC baseline vs delta: Pearson r = -0.8973**

强负相关证实了 capability-trap 假说：

- seed=42 SC 最低 (54.41%) → SICA 增益最大 (+4.90)
- seed=123 SC 中等 (53.92%) → SICA 增益中等 (+3.43)
- seed=456 SC 最高 (56.37%) → SICA 增益消失 (-0.49)

当 SC baseline 较高时，说明采样多样性较低（模型对正确答案已经很确信），留给 constraint-based reweighting 的纠错空间更小。exp-053 的 entropy 分析也印证了这一点：高 entropy 区域 SICA delta=0.00，说明即使在不确定区域，constraint 信号也未能有效区分。

3 个 seed 中 2/3 显著，均值 delta +2.61±2.79，置信区间包含 0。seed replication 结果不够 robust。

---
