# code v3 check now

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v3-check-now_20260513T011141_result.json`
- **Structured JSON:** [`c8e1d002fec98d6d3ea7.json`](../../sessions/c8/c8e1d002fec98d6d3ea7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总报告：

---

## StructFuse MVP 分析报告 — IOI (GPT-2 Small, K=3)

### 1. K=3 Cross-tabulation 2×2 矩阵

|                | CSS ≥ 0.67 | CSS < 0.67 |
|----------------|-----------|-----------|
| **CIRCUS-core**  | 13 edges  | 2 edges   |
| **CIRCUS-other** | 39 edges  | 101 edges |

Total: 155 edges (binarized union) | Core: 15

### 2. Off-diagonal 百分比
**13.3%** (95% CI: [1.7%, 40.5%])

### 3. CIRCUS-core 绝对边数
**15 edges** — **< 30 → 触发 D002，需追加 Arithmetic task**

### 4. CSS-core 绝对边数
- CSS ≥ 0.67: **52 edges**
- CSS = 1.0 (3-way consensus): **7 edges**

### 5. Pairwise Jaccard

| Pair | Jaccard | Overlap |
|------|---------|---------|
| EAP-IG × EP | 0.3072 | 47 |
| EAP-IG × ACDC | 0.0962 | 10 |
| EP × ACDC | 0.0857 | 9 |

### 6. 3-way ratio
**0.0452** (intersection: 7 edges, union: 155 edges)

3-way edges: `a10.h0->logits, a11.h2->logits, a9.h6->logits, a9.h9->logits, input->m0, m0->a5.h5.q, m0->a9.h9.v`

### 7. 各方法 Circuit size

| Method | Edges |
|--------|-------|
| EAP-IG | 100 (top-100) |
| Edge Pruning | 100 (top-100) |
| ACDC | 14 (survived all τ) |

### 8. Faithfulness (vs Known IOI 12-edge reference)

| Circuit | Size | IOI Recall | IOI Precision |
|---------|------|-----------|--------------|
| EAP-IG | 100 | 0.917 | 0.110 |
| Edge Pruning | 100 | 0.833 | 0.100 |
| ACDC | 14 | 0.833 | 0.714 |
| CSS ≥ 0.67 | 52 | **1.000** | 0.231 |
| CSS = 1.0 | 7 | 0.583 | **1.000** |
| CIRCUS-core | 15 | 0.167 | 0.133 |
| Stable core | 13 | 0.167 | 0.154 |

### Gate 判定
**PASS_MAIN** (13.3% ≥ 10%)

**D002 触发**: CIRCUS-core = 15 < 30，需追加 Arithmetic task 验证。

### 关键发现
- CSS ≥ 0.67 完美覆盖了已知 IOI 参考电路（recall=1.0），验证了 cross-method consensus 的有效性
- CSS = 1.0 的 7 条边全部是已知 IOI 边（precision=1.0），3-way consensus 极度保守但精准
- ACDC 最紧凑（14 edges），且 precision 最高（0.714），说明 ACDC 选边质量很高
- EAP-IG 与 EP 的 Jaccard=0.31 显示中等一致性；两者与 ACDC 的 Jaccard 极低（~0.09），体现了方法间真实分歧
- CIRCUS-core 和 stable core 对已知 IOI 边的 recall 很低（0.167），说明 CIRCUS 稳定性分析捕获的是不同维度的信息

---
