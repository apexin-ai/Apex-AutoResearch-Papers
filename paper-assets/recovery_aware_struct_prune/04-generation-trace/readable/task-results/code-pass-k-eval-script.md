# code pass k eval script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pass_k_eval_script_20260516T155905_result.json`
- **Structured JSON:** [`c7b7c5077055c8d1f756.json`](../../sessions/c7/c7b7c5077055c8d1f756.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

- 新增 `pass_at_k_estimator()` — Chen et al. 2021 无偏估计器
- 新增 `evaluate_pass_at_k()` — 每个 prompt 生成 n 个样本，逐样本判断正确性，计算 pass@k
- 新增 CLI 参数 `--pass_k` (default=1) 和 `--num_samples_per_prompt` (default=1)
- `--pass_k > 1` 时自动启用 sampling (temperature 默认 fallback 0.7)，`--pass_k == 1` 时行为完全不变
- JSON 输出增加 `pass_at_k`, `k`, `temperature`, `num_samples_per_prompt`, `coverage` 字段，同时保留 `accuracy`

---
