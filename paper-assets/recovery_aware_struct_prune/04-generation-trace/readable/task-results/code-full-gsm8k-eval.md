# code full gsm8k eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full_gsm8k_eval_20260515T034742_result.json`
- **Structured JSON:** [`3a2fb9b65a92ee3c41fb.json`](../../sessions/3a/3a2fb9b65a92ee3c41fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码和脚本都已验证通过。总结完成的工作：

---

### 已完成

**`eval_gsm8k.py` 更新：**
- 新增 `--voting` 参数：启用 majority voting (self-consistency)
- 新增 `--num_samples_per_question`（默认 K=8）、`--voting_temperature`（默认 0.7）、`--voting_top_p`（默认 0.95）
- 新增 `binomial_stderr(p, n)` 函数，所有模式输出 `stderr` 字段
- 新增 `evaluate_majority_voting()` 函数：每题采样 K 次，用 Counter 取多数答案
- 输出 JSON 统一包含 `accuracy`, `stderr`, `n_correct`, `n_total`, `mode`, `eos_stats`
- 修复 greedy 模式下传 `temperature=0.0` 导致 transformers 警告的问题

**`scripts/run_full_eval.sh` 更新：**
- 新增 `voting` 子命令：对所有可用模型跑 majority voting K=8
- 新增 `full` 子命令：greedy (phase1-3) + voting 一起跑
- 添加 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1`（AutoDL 必需）
- Summary 输出包含 stderr（`accuracy ± stderr`）

### 未完成

Dry-run 验证未能执行 — 两张 GPU 正在跑 GRPO v2 训练（PID 274156, 276978），无可用显存。GRPO 训练完成后即可执行 eval。

---
