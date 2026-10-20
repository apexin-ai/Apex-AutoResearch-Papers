# code spectral metric comparison

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_spectral-metric-comparison_20260513T081946_result.json`
- **Structured JSON:** [`13ee65b1d750a237a7b8.json`](../../sessions/13/13ee65b1d750a237a7b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。`evaluate_spectral_metrics.py` 已写入 `artifacts/code/`。

脚本结构：
- `collect_hidden_states` — 收集 final-layer mean-pooled hidden states，返回 (N, D) 矩阵
- `compute_all_spectral_metrics` — 从 E 矩阵计算 4 种谱指标（eff_rank / condition_number / trace_norm / spectral_gap）
- `evaluate_checkpoint` — 加载单个 checkpoint，计算谱指标 + PPL
- `compute_leading_indicator_ranking` — 以首个 checkpoint 为 baseline，找各指标最早超过 2σ 偏离的位置，输出排名
- `discover_checkpoints` — 自动扫描 G*/training/checkpoint-* 和 G*/final_model/
- holdout 数据用 wikitext-103-raw-v1 test split tokenize + pack

---
