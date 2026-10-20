# analysis c4 5method full

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_5method_full_20260517T173731_result.json`
- **Structured JSON:** [`3a9c98d4d8546d5ad40c.json`](../../sessions/3a/3a9c98d4d8546d5ad40c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存。以下是完整汇总：

---

## Pythia-1B C4 α=1.0 — 8 Canonical Pairs

### Collapse Trajectory
```
              gen0        gen10       drift%
entropy     2.9559      1.2558      -57.5%
ece         0.0124      0.4555    +3562.9%
perplexity 20.5984   1682.6080    +8068.6%
d1          0.1143      0.0890      -22.2%
d2          0.5558      0.3942      -29.1%
d3          0.8361      0.6038      -27.8%
mauve       0.7299      0.2960      -59.4%
```

### Per-pair Detail (6 methods)

| Pair | Naive | Diff | Thresh | PG_fwd | PG_rev | TY | votes |
|------|-------|------|--------|--------|--------|-----|-------|
| entropy→d1 | Y | Y | Y | Y | N | N | 4/6 |
| entropy→d2 | Y | Y | Y | Y | N | N | 4/6 |
| entropy→d3 | Y | Y | Y | Y | N | N | 4/6 |
| entropy→mauve | Y | Y | Y | Y | N | N | 4/6 |
| ece→d1 | Y | Y | Y | Y | Y | Y | 6/6 |
| ece→d2 | Y | Y | Y | Y | Y | Y | 6/6 |
| ece→d3 | N | Y | Y | Y | Y | Y | 5/6 |
| ece→mauve | Y | Y | Y | Y | N | Y | 5/6 |

### Table 5 Row (Method Summary)

| Method | Sig/8 | Pairs |
|--------|-------|-------|
| Naive XCorr | 7/8 | all except ece→d3 |
| Diff XCorr (FDR) | 8/8 | all |
| Threshold Onset | 8/8 | all |
| PermG forward (FDR) | 8/8 | all |
| PermG reverse (FDR) | 3/8 | ece→d1, ece→d2, ece→d3 |
| TY Granger | 4/8 | ece→d1, ece→d2, ece→d3, ece→mauve |

### 5-method Consensus (excl. PermG_rev)

| Consensus | Count |
|-----------|-------|
| ≥3/5 | **8/8** |
| ≥4/5 | **8/8** |
| ≥5/5 | 3/8 |

---

### Key Answers

**1. K≥4/5 consensus = 8/8.** 远超 VERSION A 门槛 (≥4/8)。所有 8 pairs 至少 4 种方法一致显著。

**2. PermG counts:**
- Forward: **8/8** (所有 pairs FDR 显著)
- Reverse: **3/8** (仅 ece→d1/d2/d3，方向性确认: canary→downstream 因果强于反向)

**3. Domain robustness: 达标。** C4 结果甚至强于典型 WikiText baseline — 8/8 pairs 在 ≥4/5 consensus 下全部显著，PermG forward 8/8 全过，reverse 3/8 确认因果方向性。Pythia-1B + C4 域完全复现了 canary-leads-downstream 的核心结论。

注：ece→d3 的 Naive 标记 N 是因为最优 lag=-3（downstream 反领先），但 Diff/Thresh/PG_fwd/PG_rev/TY 全部 SIG，说明 naive pearson 对该 pair 被 spurious lag structure 误导。TY 在 ece pairs 显著（d_max=0, df_resid=7 → 足够 power），entropy pairs 不显著（d_max=1, df_resid=4 → power 不足），符合 C003 约束预期。

---
