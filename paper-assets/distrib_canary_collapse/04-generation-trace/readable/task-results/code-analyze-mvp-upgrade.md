# code analyze mvp upgrade

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-mvp-upgrade_20260514T083241_result.json`
- **Structured JSON:** [`c3cbd13626bcd3be756f.json`](../../sessions/c3/c3cbd13626bcd3be756f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 AST 解析通过，4 个 CLI 参数（`--results_dir`, `--seeds`, `--max_lag`, `--n_permutations`）均已注册。本地无 matplotlib 所以无法直接运行 `--help`，但语法和参数定义正确。

实现的 6 项检查：

1. **`permutation_test()`** — B=10000 次 shuffle downstream，计算 max|r| 的 p-value
2. **Per-seed significance** — 每个 triplet 调 permutation_test，`classify_pair()` 按 3/3 seeds 规则判定 SIGNIFICANT/WEAK/NO LEAD
3. **`check_mauve_floor()`** — Gen 0 MAUVE < 0.10 且 CV < 0.50 时 demote
4. **`check_effective_rank_monotonicity()`** — Gen 4-9 OLS 斜率一致性检查
5. **`compute_verdict()`** — STRONG PASS / PASS / CONDITIONAL PASS / FAIL，排除 inconclusive 的 effective_rank 和 demoted 的 MAUVE
6. **`compute_lag_dispersion()`** — mean/std/min/max lag，std > 2.0 标记 high_dispersion

所有现有功能（plots, CSV, console report）保留，`analysis_summary.json` 输出结构符合要求规格。

---
