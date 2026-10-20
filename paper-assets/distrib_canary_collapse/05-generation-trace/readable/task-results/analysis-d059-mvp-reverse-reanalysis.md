# analysis d059 mvp reverse reanalysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d059_mvp_reverse_reanalysis_20260518T033449_result.json`
- **Structured JSON:** [`7a6fc44826e3b4a322c2.json`](../../sessions/7a/7a6fc44826e3b4a322c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Seed 42 (D057 统一参数, n_perm=5000, max_lag=1, raw p<0.05):**

| 方向 | 结果 |
|------|------|
| token_entropy reverse | **0/4** (all p > 0.48) |
| ECE reverse | **3/4** (d1→ece p=0.0274, d2→ece p=0.0286, d3→ece p=0.0306; ppl→ece p=0.14) |
| **Total reverse** | **3/8** |
| Forward 对比 | 6/8 (F-stat 比 reverse 大 13-119 倍) |

**Seeds 43-45: 无法重分析。** α=1.0 的逐代数据已从服务器清除，registry 只保留了 gen0/gen10 摘要指标，无法运行 Granger 时序分析。

**"0/24" 来源解释:** 旧分析用 3 seeds × 8 pairs = 24，参数为 n_perm=1000 + BH FDR + mauve。Seed 42 的 ece←diversity raw p≈0.032-0.036 在 FDR 校正后变为不显著，故 0/24。D057 统一参数取消 FDR 且提升 n_perm 至 5000 后，这 3 个 pair 变为显著。

**论文建议:** Table 7 Baseline PG_rev 应写 3/8（仅 seed 42 可验证），Case Study 不能再写 "0/24"。

---
