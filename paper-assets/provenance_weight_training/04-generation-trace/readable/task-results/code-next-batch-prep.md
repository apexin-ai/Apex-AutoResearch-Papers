# code next batch prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_next_batch_prep_20260515T192642_result.json`
- **Structured JSON:** [`7c2522be63d7d75e6386.json`](../../sessions/7c/7c2522be63d7d75e6386.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法检查通过。总结：

### 任务 1: grid_b_low seed42

`run_grid_b_low_seed42_v2.sh` 已就绪。与旧版差异：
- 补了 `--tau 0.8`、`--eval_steps 500`、`export HF_HOME`
- 每个 b 值训练后自动跑 holdout perplexity eval（结果存 `output/eval/`）
- 使用 loop 结构更简洁

### 任务 2: ρ=0.6 数据

`--contamination_ratio` 是纯元数据，不影响采样。需要重新混合数据。

已创建：
- `scripts/prepare_rho06_data.py` — 从 164,889 human + 采样 247,334 synthetic 合成 ρ=0.6 数据，用 TF-IDF detector 评分
- `scripts/run_prepare_rho06.sh` — 启动器（CPU only，可立即运行）
- 输出：`data/scored_data_rho06.jsonl`

### README

`output/next_batch_prep.md` 记录了所有启动步骤和参数说明。

---
