# exp fpr coverage 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fpr_coverage_001_20260521T070655_result.json`
- **Structured JSON:** [`4f9dc0be4326233ef731.json`](../../sessions/4f/4f9dc0be4326233ef731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| τ | C4-5k FPR | C4-5k Cov | C4-10k FPR | C4-10k Cov | Ctrl d1-d3 bal_acc |
|---|-----------|-----------|------------|------------|-------------------|
| 0.50 | 17.5% | 94.7% | 32.4% | 96.1% | 77.0% |
| 0.60 | 9.8% | 84.5% | 24.0% | 83.7% | 82.0% |
| **0.65** | **4.7%** | **79.0%** | **12.8%** | **72.1%** | **84.0%** |
| **0.70** | **1.4%** | **75.2%** | **3.5%** | **64.5%** | **85.8%** |
| **0.75** | **0.4%** | **73.4%** | **0.4%** | **61.5%** | **86.9%** |
| 0.80 | 0.1% | 72.1% | 0.1% | 60.1% | 88.1% |
| 0.90 | 0.0% | 67.4% | 0.0% | 56.3% | 89.3% |
| 0.99 | 0.0% | 54.4% | 0.0% | 41.1% | 75.0% |

**推荐 operating point**: τ=0.70，C4 FPR 从 20.2%→1.4%（5k）/ 34.0%→3.5%（10k），保留 75%/65% coverage，controlled d1-d3 精度 85.8%。τ=0.75 可进一步降至 FPR≈0.4%，coverage 代价仅 ~2-3pp。

产出：
- CSV: `results/fpr_coverage/fpr_coverage_tradeoff.csv`
- 图: `results/fpr_coverage/fpr_coverage_curve.png`
- Registry: `fpr_coverage_001` → DONE (success)

---
