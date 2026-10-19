# analysis p1 divergence timing

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p1-divergence-timing_20260512T232744_result.json`
- **Structured JSON:** [`8ee03a266b9f53abc3b9.json`](../../sessions/8e/8ee03a266b9f53abc3b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。完整结果如下：

---

## P1 Divergence Timing 分析结果 (N=276)

### 三组统计

| Group | d range | N | correction_span mean | median | std | expert_length mean |
|-------|---------|---|---------------------|--------|-----|-------------------|
| **early** | <0.33 | 262 | 10.14 | 7.0 | 7.20 | 11.26 |
| **mid** | 0.33–0.66 | 12 | 4.58 | 5.0 | 1.08 | 8.25 |
| **late** | >0.66 | 2 | 2.50 | 2.5 | 0.71 | 8.50 |

### 统计检验

- **Kruskal-Wallis**: H=20.76, **p=5e-06** (显著)
- **Ordinal**: early >= mid >= late **成立** (medians: 7.0 > 5.0 > 2.5)
- **Mann-Whitney U** (early > mid): U=2787.0, **p=3e-06**
- late 组仅 2 条样本（均来自 v6），无法做 mid>late 和 early>late 的 pairwise 检验

### d 值分布

```
0.0-0.1: ████ (85)    | 0.3-0.4: (7)
0.1-0.2: ████████ (146)| 0.4-0.5: (4)
0.2-0.3: ██ (29)       | 0.5-0.7: (4)
                        | 0.7-0.8: (1)
```

94.2% 的样本 d<0.33（early），数据**严重左偏**。

### 来源拆分

- v5 (251): early=243, mid=8, late=0
- v6 (25): early=19, mid=4, late=2

### 关键发现

1. 统计上显著（p=5e-06），ordinal 成立
2. **但分组极度不平衡**：early 占 95%，late 仅 2 条。这说明当前 failure trajectories 中绝大多数在 expert trajectory 前 1/3 就偏离了
3. correction_span = expert_length*(1-d)，ordinal 关系部分是代数必然。不过 early 组的 expert_length 均值（11.26）显著大于 mid（8.25），说明早偏离的任务本身也更长，effect size 不完全是代数产物
4. 三等分 (0.33/0.66) 的 binning 方案对此数据不理想，建议考虑**四分位数分组**或**连续回归** d→correction_span

### 产出文件

`outputs/p1_divergence_timing.json` 已保存，旧 p1 文件已有 `_pre_d026_backup` 后缀无需再改。

---
