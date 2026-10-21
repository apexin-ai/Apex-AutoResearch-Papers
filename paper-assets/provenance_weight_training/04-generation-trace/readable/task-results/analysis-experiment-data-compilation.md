# analysis experiment data compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment-data-compilation_20260516T051015_result.json`
- **Structured JSON:** [`c6ba0c3099192582730b.json`](../../sessions/c6/c6ba0c3099192582730b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已生成并注册：

- `artifacts/experiment_tables.md` — 6 张 Markdown 表格（Tables A-F）
- `artifacts/experiment_data.csv` — 62 行机器可读 CSV

关键发现：
- **最优方法**: adaptive n_min=3 (Mean PPL 17.639)，其次 grid_b0.5 (17.646)、adaptive_fix n_min=2 (17.651)
- **最优 τ**: 0.8（PPL 17.653），过低/过高均降低性能
- **n_min**: 3 最佳，1 过于激进（b*_mean=7.2），4 退化为 uniform
- **ρ=0.6**: 所有方法 PPL 增加 0.04-0.09，grid_b0.5 最鲁棒（Δ=0.053）
- **Batch size**: bs=4 优于 bs=8
- **Baseline**: Qwen3-0.6B 未训练 PPL=22.970，训练后所有方法均显著提升

---
