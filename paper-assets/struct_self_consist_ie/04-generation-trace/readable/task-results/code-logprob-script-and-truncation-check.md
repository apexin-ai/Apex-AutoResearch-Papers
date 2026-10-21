# code logprob script and truncation check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_logprob_script_and_truncation_check_20260514T113358_result.json`
- **Structured JSON:** [`216ca8624ad287d7b2d8.json`](../../sessions/21/216ca8624ad287d7b2d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 总结

### Part A: exp-012 截断问题

| 指标 | 值 |
|------|-----|
| exp-012 max_tokens | 512（硬编码于 `extract_logprobs.py` L56, L67） |
| pilot 的 sampling.py 默认值 | 1024 |
| 恰好 512 tokens 的输出 | 235/4959 (4.7%) |
| 至少 1 个 sample 被截断的 instance | **45/551 (8.2%)** |
| 全部 8 个 sample 都被截断的 instance | 9/551 (1.6%) |

**结论：8.2% > 5% 阈值，exp-012 需要用 max_tokens=1024 重跑。** 被截断的 instance 倾向于实体/关系最多的复杂样本，截断导致 JSON 不完整，系统性压低 F1 和相关性分析。

### Part B: 修改完成

**evaluation.py** — 新增两个函数：
- `kendall_correlation()` — Kendall τ-b 相关系数
- `compute_auroc()` — 基于中位数二值化的 AUROC

**sampling.py** — 两处修改：
- `VLLMSampler.sample()` — 新增 `collect_logprobs=False` 参数；启用时设 `logprobs=1`，提取 `cumulative_logprob` / `n_tokens` / `mean_logprob`
- `run_sampling_pipeline()` — 新增 `collect_logprobs=False` 参数；启用时在 SampledInstance 中添加 `"logprobs": [per_sample_mean_logprob, ...]` 字段，并将 logprob 元数据嵌入每个 sample dict

**run_mvp_pilot.py** — 四处修改：
- `--max_tokens` 默认值 512 → 1024
- 新增 `--collect_logprobs` flag
- 分析部分新增 logprob baseline：Spearman ρ / Kendall τ / AUROC（full + conditional）
- 报告输出新增 logprob baseline 行

所有修改向后兼容——不加 `--collect_logprobs` 时行为与之前完全一致。

---
