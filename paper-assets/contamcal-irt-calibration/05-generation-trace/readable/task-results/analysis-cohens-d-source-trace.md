# analysis cohens d source trace

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cohens-d-source-trace_20260522T041515_result.json`
- **Structured JSON:** [`90bac4ea411ad3f7b6a3.json`](../../sessions/90/90bac4ea411ad3f7b6a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是结论。

## 结果

### d = −1.98 (d100) — **可复现** ✓

来源：0.5B (Qwen2.5-0.5B) MinK++ paired Cohen's d (d100 vs d000)，取三个 benchmark 均值。

| Benchmark | Paired Cohen's d |
|-----------|-----------------|
| MMLU | −1.2203 |
| GSM8K | −2.6660 |
| ARC | −2.0480 |
| **Mean** | **−1.9781 ≈ −1.98** |

原始数据来自 `exp008_v4_results.json` 的 `cross_model_d100_vs_d000` → `S2_MinKPP` → `cohens_d` 字段（每个 benchmark 一个值），由 `/root/contamcal-irt-calibration/exp008/signal_survival_v4.py` 生成，使用 `Qwen2.5-0.5B_d{000,100}_s42` 的 merged signal 文件。

计算方法：paired Cohen's d = `mean(d100_score - d000_score) / std(d100_score - d000_score, ddof=1)`，逐 item 配对。

---

### d = −1.55 (d005) — **无法复现** ❌

穷尽了以下所有计算路径，无一产出 −1.55：

| 方法 | MMLU | GSM8K | ARC | Mean | Pooled |
|------|------|-------|-----|------|--------|
| Paired (d005 vs d000) | −1.386 | −1.816 | −1.962 | −1.721 | −1.433 |
| Unpaired (d005 vs d000) | −1.665 | −1.783 | −2.299 | −1.916 | — |
| Contam-only paired | −1.617 | −1.714 | −1.801 | −1.710 | — |
| N-weighted paired | — | — | — | −1.461 | — |

最接近的值是 **MMLU unpaired d100 = −1.5775**，但它是 d100 而非 d005。

`signal_survival_v4.py` 对 d005 仅计算 within-model AUC（不计算 cross-model Cohen's d），因此 `exp008_v4_results.json` 中不含 d005 的 Cohen's d。

---

### 建议

1. **d100 = −1.98**：保留，可注明为 "mean across three benchmarks"
2. **d005 = −1.55**：两个选择：
   - **替换为可复现值**：用 paired pooled d005 = −1.43 或 mean per-benchmark = −1.72
   - **改用定性描述**：如 "large negative effect sizes (|d| > 1.2 across all benchmarks at both d005 and d100)"

---
