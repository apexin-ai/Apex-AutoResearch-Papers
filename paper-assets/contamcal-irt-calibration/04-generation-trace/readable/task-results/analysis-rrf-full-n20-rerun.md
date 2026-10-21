# analysis rrf full n20 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rrf_full_n20_rerun_20260516T131509_result.json`
- **Structured JSON:** [`9c6e96a4ba4eb9b46fbf.json`](../../sessions/9c/9c6e96a4ba4eb9b46fbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

IRT 正在运行，MMLU 的 chain 1 已在 sampling 阶段。

## 报告

### RRF 聚合结果
- **N=25 respondents**（新 `exposure_scores.json` 路径：`/root/autodl-tmp/exp003/rrf_n20_all/exposure_scores.json`）
- 组成：
  - 0.5B s42: 4 (d000/d005/d025/d100)
  - 0.5B s123: 4 (d000/d005/d025/d100)
  - 1.5B s42: 4 (d000/d005/d025/d100)
  - 1.5B s123: 4 (d000/d005/d025/d100)
  - 3B s42: 4 (d000_a32, d005_a32, d025_v3, d100_a32)
  - 3B s123: 4 (d000_s123_a32, d005, d025, d100_a32)
  - Base: 1 (`Qwen2.5-0.5B-Instruct`，来自 signal 目录自动发现)
- 比旧 N=23 多了 `Qwen2.5-3B_d000_s123_a32`（仅 MMLU）和 `Qwen2.5-0.5B-Instruct`

### 注意事项
- `Qwen2.5-0.5B-Instruct` 是 base model（无 dose/seed），RRF 脚本自动发现了它。IRT 侧依赖 eval_results 目录匹配，不会影响 IRT
- `Qwen2.5-3B_d000_s123_a32` 只有 MMLU 的 4 个文件（可能不完整，仅 1 benchmark 有 signal）
- 3B s42 中 d025 使用的是 `d025_v3` 命名（无 `_a32_`），但来自 alpha=32 重训

### Pooled IRT 2PL+γ
- **PID=785832**，运行中
- MMLU: N_models=13（D045 排除了 8 个 0.5B）, 300 items (subsampled)
- 4 chains x 1000 warmup + 1000 samples, adapt_delta=0.95
- 日志：`/tmp/irt_pooled_n20.log`
- 输出：`/root/autodl-tmp/exp006/results_pooled_n20/`

---
