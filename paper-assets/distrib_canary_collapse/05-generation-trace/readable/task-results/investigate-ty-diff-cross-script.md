# investigate ty diff cross script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_ty_diff_cross_script_20260520T044639_result.json`
- **Structured JSON:** [`8788089de9c25a0b45a0.json`](../../sessions/87/8788089de9c25a0b45a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用。报告已写入 artifacts 目录。

调查完成。以下是核心发现：

---

## Root Cause 总结

**3 个关键 root cause 导致 TY/diff 跨脚本不一致：**

### RC-1: DOWNSTREAMS 列表不同
- `run_5method_s43.py` 用 `perplexity`，`batch_analysis.py` 用 `mauve`
- 8 pair 中 2 pair 在完全不同的数据上计算

### RC-2: Direction check 符号反转（最大影响）
- `run_5method_s43.py`: `peak_lag > 0` — **错误**，违反 C009/M035
- `batch_analysis.py`: `peak_lag < 0` — 正确
- 实测: peak_lag>0 → 0/8，peak_lag<0 → 6/8。diff_xcorr 核心计算完全一致，计数差异 100% 来自方向判定

### RC-3: TY Granger 实现完全不同（4 处分歧）
1. **ADF regression**: `"c"` vs `"ct"` → d_max 判定不同
2. **`_determine_d_max` bug (batch_analysis)**: T=10 时 ADF 在差分后序列上因 maxlag 违反 `regression="ct"` 约束而 crash，异常被静默捕获返回 d_max=1 — 不是真正的平稳性判定
3. **Lag 选择**: AIC 搜索 {1,2} vs 固定 1
4. **检验统计量**: F-test vs Wald χ²（T≤11 时差异巨大）

实测 TY 计数：a060_s43 上 run_5method=2/8 vs batch_analysis=4/8，6/8 pair 结论相反

### PermG 一致的原因
代码路径完全相同、参数相同、不依赖 ADF/direction filter

## 影响与建议
- **run_5method_s43.py 应废弃**（方向错误、downstreams 错误、硬编码路径）
- **batch_analysis.py 的 `_determine_d_max` 需修 bug**（maxlag 未考虑 ct 约束）
- **K≥3 投票**：TY 不可信，短期建议仅基于 PermG + threshold_onset + diff_xcorr (batch_analysis)

报告位于: `artifacts/ty_diff_investigation/cross_script_comparison.md`

---
