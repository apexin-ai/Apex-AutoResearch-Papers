# code analyze mvp results

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze_mvp_results_20260512T213040_result.json`
- **Structured JSON:** [`995d2f00f818e995c265.json`](../../sessions/99/995d2f00f818e995c265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，dry-run 验证通过。

**功能列表：**

| # | 功能 | 说明 |
|---|------|------|
| 1 | 数据加载 | 自动检测 `cache_&lt;method>.json`（flat）、`cache/&lt;model>/&lt;task>/&lt;method>_*.json`（structured）、`mvp_results.json` |
| 2 | Binarization | EAP-IG/IFR → top-N, Edge Pruning → threshold 0.5, ACDC → `abs(s) > τ` |
| 3 | Pairwise Jaccard | 每对方法的 Jaccard similarity |
| 4 | 2^K cross-tabulation | 全部 cell 计数 + off-diagonal 比率 |
| 5 | CIRCUS tiers | config-bagging → core/contingent/noise |
| 6 | CIRCUS×CSS cross-table | stable_core / method_specific / cross_unstable / noise |
| 7 | ACDC threshold sensitivity | τ ∈ {0.01, 0.03, 0.05, 0.1, 0.3} 逐个扫描 off-diagonal |
| 8 | Gate 判定 | ≥10% PASS_MAIN / 5-10% PASS_FINDINGS / 2-5% MARGINAL / <2% KILL |
| 9 | 可视化 | CSS heatmap (PNG) + Venn diagram（fallback 为 bar chart） |
| 10 | JSON 输出 | `analysis_results.json` 含全部数字 |
| 11 | `--dry-run` | mock 500 edges × 3 methods 验证流程 |

**依赖：** `numpy`（必需）、`matplotlib`（可视化，缺失时跳过）、`matplotlib_venn`（可选，缺失时 fallback 为 bar chart）

**CLI：**
```bash
python analyze_mvp_results.py --results-dir /root/min_necessary_circuit_css --output-dir ./analysis
python analyze_mvp_results.py --dry-run
```

---
