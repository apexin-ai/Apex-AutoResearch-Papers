# code data audit experiments tables

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_audit_experiments_tables_20260523T193629_result.json`
- **Structured JSON:** [`5601ea0072b133bb4ed8.json`](../../sessions/56/5601ea0072b133bb4ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/data_audit_part2.md`。

核查覆盖了 3 个 Table（62 cells）+ experiments.tex（~55 个数字）+ discussion.tex（~17 个数字）。

**需立即修正的 4 项**：

1. **Table 1 Ability quintile N**: 论文写 `~2,600/~2,600`，实际 `2,092/2,089` — 多报约 500/组
2. **§5.2 bootstrap CI [29.4%, 38.1%]**: 从 bootstrap_results.csv 计算为 `[29.2%, 37.8%]`
3. **§5.6 τ=0.958**: 六个 benchmark 的均值 τ=0.962、中位数 0.959、最小值 0.943 — 无解释可得 0.958
4. **§5.6 flip rate ≤2.8%**: WinoGrande=2.84%，超过 2.8%

其余 ⚠️ 项为措辞/四舍五入/上下文问题（AUC at N≥80 措辞、18.3%→18.4% 四舍五入、±800 对称性等），不影响结论但值得注意。

k=10/20/30 ΔFPR 值（summary_by_k_full.csv）、Table 3 全部 42 cells、base/instruct 分层数据均与源文件完全匹配。

---
