# research exp leaderboard data recon

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp-leaderboard-data-recon_20260520T095549_result.json`
- **Structured JSON:** [`1cf60702491e20519319.json`](../../sessions/1c/1cf60702491e20519319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-leaderboard-data-recon → DONE (success)**

**核心结论**: Open LLM Leaderboard v1 的 `details` 数据集包含 **per-item binary response data**，覆盖 13,000+ 模型和我们 5 个 benchmark 中的 4 个（MMLU, HellaSwag, ARC-Challenge, GSM8K）。HumanEval 不在 v1 中。

**数据格式**: 每个模型一个 HF dataset (`open-llm-leaderboard-old/details_{model}`)，按 benchmark 分 config，每行一道题，包含 `acc`/`acc_norm` 二值字段（可直接转为 0/1 binary response）。Parquet 格式，`load_dataset()` 即可加载。

**GPU 预算**: 0 GPU-hours（数据已有）。仅 HumanEval 需自己跑推理（164 题，每个 7B 模型约 5 分钟）。

**下一步**: 写下载脚本，从 v1 details 中提取目标模型的 binary response matrix，对齐 PSN-IRT item parameters，计算 lz*。需注意 item ordering 对齐问题。

报告已保存至 `artifacts/leaderboard_data_recon/report.md`。

---
