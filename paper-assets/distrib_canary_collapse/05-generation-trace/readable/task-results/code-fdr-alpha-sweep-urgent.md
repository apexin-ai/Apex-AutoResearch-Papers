# code fdr alpha sweep urgent

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fdr-alpha-sweep-urgent_20260514T213026_result.json`
- **Structured JSON:** [`111e1104777337ab7bba.json`](../../sessions/11/111e1104777337ab7bba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**完成情况：**

- **脚本路径**: `/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py`
- **功能**: 自动发现 α-sweep 运行目录，对所有 canary (token_entropy, ece) × downstream (distinct_1, distinct_2, distinct_3, perplexity) = 8 对执行三方法分析 + BH FDR 校正

**集成内容：**

1. **BH FDR 校正** — 每个 α 值内、每种方法的所有 pair p-value 通过 `statsmodels.stats.multitest.multipletests(method='fdr_bh')` 校正。输出同时保留 `p_raw` 和 `p_fdr`，判显著改用 `significant_fdr`

2. **Canary channels 补全** — 覆盖 2×4 = 8 对（token_entropy/ece × distinct_1/2/3/perplexity），α 值从目录自动发现

3. **三方法框架**:
   - Naive cross-correlation（raw levels + permutation test）
   - Differenced cross-correlation（Δ-series + permutation test）
   - Toda-Yamamoto Granger causality（augmented-lag Wald F-test）
   - 每对输出方法一致性矩阵（≥2 methods = consensus）

4. **Effect size** — xcorr 方法报告 `effect_size_r` + Cohen's 分类；TY 报告 `effect_size_f2` + Cohen's f² 分类

**Dry-run 结果（a000_s42, 6 gens）：**
- 1 个 naive raw-sig (ece→distinct_1, p=0.046) 被 FDR 校正降为 n.s. — 符合预期（8 tests 校正）
- TY 因 T=6 不够残差自由度全部返回 N/A — 等实验跑完 10 gen 后会有效
- a025_s42 仅 1 gen 被正确跳过
- 输出：`results/alpha_sweep/analysis/alpha_sweep_analysis.json` + `summary.txt`

---
