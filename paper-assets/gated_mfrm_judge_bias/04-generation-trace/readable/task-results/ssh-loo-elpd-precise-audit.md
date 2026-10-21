# ssh loo elpd precise audit

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_loo_elpd_precise_audit_20260523T111532_result.json`
- **Structured JSON:** [`cac9169666a65c301908.json`](../../sessions/ca/cac9169666a65c301908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到齐，差异根因已明确。

## 精确溯源结果

### ArviZ 1.1.0，数据：5661 observations

| 来源 | G-MFRM elpd | MFRM elpd | ΔELPD | dSE | \|Δ/dSE\| |
|------|------------|-----------|-------|-----|----------|
| **`az.compare()` DataFrame** | -2270.0 | -2330.0 | -60.0 | 9.4 | 6.38 |
| **`az.loo()` 分别计算** | -2272.5925 | -2328.2849 | **55.6924** | — | — |
| **Pointwise elpd_i 差异** | — | — | **55.6924** | **9.3945** | **5.9282** |
| **WAIC (manual)** | -2272.2656 | -2327.8529 | 55.5874 | — | — |

### 根因

**`az.compare()` 在 ArviZ 1.1.0 中对 DataFrame 做了有效位数截断。** 所有数值都被四舍五入：

- -2272.59 → **-2270.0**（约到十位）
- -2328.28 → **-2330.0**（约到十位）
- elpd_diff = -2330 - (-2270) = **-60.0**（从已截断值算出）
- dse = 9.3945 → **9.4**

论文中的 ΔELPD = -60.0 和 |Δ/dSE| = 6.4 都来自这个截断后的 DataFrame。它们**不是**真实的精确值。

### Pointwise 验证

`elpd_i` 逐观测差异的求和 = 55.6924，与分别 `az.loo()` 再相减完全一致。dSE = √N × std(diff) = 9.3945。

### 结论

| 指标 | 论文当前值 | 正确值 |
|------|----------|--------|
| ΔELPD | ±60.0 | **55.7** |
| \|Δ/dSE\| | 6.4 | **5.9** |

论文应写 **ΔELPD = 55.7, \|Δ/dSE\| = 5.9**。定性结论不变（\|Δ/dSE\| > 2 已属强证据），但数值需要更正。

### 附录：JSON 文件状态

- `waic_loo_summary.json` 的 `delta_elpd_loo = 0.0` 是 bug（`extract_loo()` 找 `elpd_loo` 属性但 ArviZ 1.x 是 `elpd`），其 `comparison` 节也是截断值
- `loo_comparison.json`（审计版）的 `delta_elpd_loo = 55.69` 是正确的，但其 `comparison` 节也从 az.compare() 复制了截断值

---
