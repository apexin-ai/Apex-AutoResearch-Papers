# check all eval progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_eval_progress_20260520T110742_result.json`
- **Structured JSON:** [`b38768feadd1567b0c39.json`](../../sessions/b3/b38768feadd1567b0c39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 个 Eval 作业状态

### westd-29022 — Standard GRPO Seed Evals (N=1319)

| 作业 | 状态 | 进度 | 当前 Accuracy | ETA |
|------|------|------|--------------|-----|
| **seed123** | running | ~282/1319 (21%) | **62.40%** (@ 250 samples) | ~2h (avg ~2.3s/it) |
| **seed456** | running | ~321/1319 (24%) | **64.00%** (@ 300 samples) | ~2h (avg ~2.3s/it) |

两个都正常推进，速度合理。

### westb-23072 — Qwen-Math SFT Evals (N=200)

| 作业 | 状态 | 进度 | 速度 | 问题 |
|------|------|------|------|------|
| **PID 14641** CKA-only SFT | running | **7/200 (3.5%)** | ~303s/it | max_length 溢出 |
| **PID 14719** Standard SFT | running | **11/200 (5.5%)** | ~247s/it | max_length 溢出 |

**westb 两个作业严重异常。** 日志显示 `This is a friendly reminder - the current text generation call has exceeded the model's predefined maximum length (4096)`。模型在部分样本上生成到 4096 token 才停止，导致单样本耗时 5-6 分钟。按当前速度，200 样本需要 **13-17 小时**。

这两个 SFT checkpoint 可能没学好 EOS token。建议 kill 掉并加 `--max_new_tokens 2048` 限制生成长度重跑。

---
