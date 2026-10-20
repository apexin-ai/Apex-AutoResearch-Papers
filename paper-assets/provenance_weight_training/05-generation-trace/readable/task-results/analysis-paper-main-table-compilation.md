# analysis paper main table compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-main-table-compilation_20260518T212919_result.json`
- **Structured JSON:** [`fa464b9fc7d025dd93e9.json`](../../sessions/fa/fa464b9fc7d025dd93e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_main_table_data.md`，包含 9 张表格数据。

**核心发现汇总：**

| 表格 | 关键结论 |
|------|---------|
| Table 1 (Main) | Adaptive -0.043 PPL vs Uniform (3 seeds), Random +0.109 证实 detector signal load-bearing |
| Table 2 (Grid-b) | 最优 b≈0.2-0.3，Adaptive 自动匹配 grid-best |
| Table 3 (D&R) | 多 epoch D&R=17.28，epoch-matched D&R=17.66 ≈ Adaptive=17.651 |
| Table 4 (ρ) | ρ=0.2 adaptive 反而有害；ρ=0.4 有效 (-0.043)；ρ=0.6 有效 (-0.028) |
| Table 5 (Multi-det) | TF-IDF 已验证；N-gram 训练完缺 eval；GPT-2 未开始 |
| Table 6 (1.7B) | Eval 正在跑 |
| Table 7 (Llama-3B) | PPL +0.05 (微劣)，MMLU +1.57pp (3.9σ 显著提升) |
| Table 8 (τ) | 最优 τ=0.8；τ≥0.9 有害 |
| Table 9 (bs/n_min) | coupling rule n_min=max(2,bs//2) 验证有效 |

**阻塞项：** N-gram eval、GPT-2 实验、1.7B eval 尚未完成。

---
