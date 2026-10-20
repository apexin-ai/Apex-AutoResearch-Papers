# analysis scierc per type lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_per_type_lp_20260517T045132_result.json`
- **Structured JSON:** [`d37594e36efaa25655e2.json`](../../sessions/d3/d37594e36efaa25655e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

```
Type                   N   Degen%  Greedy F1  LP Sel F1   Δ(pp)   LP ρ   Oracle F1  Headroom
─────────────────────────────────────────────────────────────────────────────────────────────
OtherScientificTerm  162    6.2%    0.6368     0.6311    -0.57   0.205    0.7617    12.49pp
Method               147   16.3%    0.6921     0.6919    -0.03   0.153    0.8093    11.72pp
Generic               90   10.0%    0.6056     0.6263    +2.07   0.145    0.7690    16.34pp
Task                  79   10.1%    0.6081     0.6339    +2.58   0.214    0.7552    14.71pp
Material              35   20.0%    0.6270     0.6362    +0.91   0.160    0.7351    10.81pp
Metric                16   12.5%    0.7027     0.7021    -0.06   0.195    0.8395    13.69pp
─────────────────────────────────────────────────────────────────────────────────────────────
OVERALL              529   11.3%    0.6439     0.6501    +0.61    ---     0.7758    13.19pp
```

**关键发现：**

1. **LP selection 分化明显**：Task (+2.58pp) 和 Generic (+2.07pp) 获益最大；OtherScientificTerm (-0.57pp) 和 Method (-0.03pp) 基本无效甚至略负。

2. **Degeneracy 不是主因**：Method 的 degen 最高 (16.3%) 但 LP delta 仅 -0.03pp（不是最差）；OtherScientificTerm degen 最低 (6.2%) 但 delta 反而为负。Spearman(degen, delta)=0.143, p=0.79，无显著相关。

3. **Headroom 才是关键驱动力**：Generic (16.34pp headroom) 和 Task (14.71pp) 是 headroom 最大的两类，也是 LP 获益最大的；Spearman(headroom, delta)=0.429 方向正确但样本太少未达显著。

4. **LP ρ 普遍较弱**（0.14-0.21），说明 logprob 作为 quality signal 在 SciERC 上 per-instance 区分度有限，但 type 间差异不大。

输出已保存：
- CSV: `output/exp_012_rerun_1024/per_type_lp_analysis.csv`
- LaTeX: `output/exp_012_rerun_1024/per_type_lp_table.tex`

---
