# code m1v2 analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m1v2-analysis-prep_20260513T210243_result.json`
- **Structured JSON:** [`d07c07c5cb28b92ab80c.json`](../../sessions/d0/d07c07c5cb28b92ab80c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/pacs/profiling/analyze_results.py`。

**功能列表：**

1. **`load_results(input_dir)`** — 加载 `profiling_results.json`
2. **`build_ii_table(data)`** — 生成 per-phase × per-level 的 II 均值 + 95% CI 表，标注 pass/fail（CI 是否排除 0）
3. **`compare_phases(data)`** — 所有 phase 对的差异检验：CI 不重叠 或 符号反转
4. **`analyze_sparsity(data)`** — 从 diagnostics 提取全局 sparsity values，运行 `fit_gmm_bic` + `segment_by_quantile`，对比 GMM best_k 与 KDE 检测的 phase 数
5. **`compute_verdict(data, comparisons)`** — MVP Pass 判定：任一 phase 对显著即 PASS
6. **`run(input_dir)`** — 主流程，输出格式化表格到 stdout + 保存 `analysis_summary.json`
7. **`main()`** — CLI 入口，`python -m pacs.profiling.analyze_results --input_dir /path/to/output`

---
