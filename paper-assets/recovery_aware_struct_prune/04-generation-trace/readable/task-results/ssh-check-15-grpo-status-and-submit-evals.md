# ssh check 15 grpo status and submit evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_15_grpo_status_and_submit_evals_20260520T213054_result.json`
- **Structured JSON:** [`0fb6e4413e15f3812b54.json`](../../sessions/0f/0fb6e4413e15f3812b54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常加载模型。

---

## 汇报

### 训练状态

| 实验 | 状态 | 说明 |
|------|------|------|
| grpo_cka_only_15_seed123 | **DONE (success)** | 100/100 steps, model.safetensors 完整 (13,065,303,184 bytes = v2 参考) |
| grpo_cka_only_15_seed456 | **DONE (success)** | 100/100 steps, model.safetensors 完整 (同上) |
| grpo_standard_15_seed123 | **DONE (failed)** | model.safetensors 截断 3.6G/13G (29%), 需重训 |
| grpo_standard_15_seed456 | **DONE (failed)** | model.safetensors 截断 11G/13G (88%), 需重训 |

**失败原因**: `/root/autodl-tmp/` 磁盘 100% 满（619G/619G）。4 个训练同时保存 checkpoint-100 时写满了数据盘。cka_only 的 model 权重先保存成功，standard 的 model 权重在后面保存时磁盘已满。

### 已提交 Eval

| Eval | GPU | 状态 |
|------|-----|------|
| eval_gsm8k_grpo_cka_only_15_seed123 | cuda:0 | **已启动** (tmux: eval_cka_15_s123) |
| eval_gsm8k_grpo_cka_only_15_seed456 | cuda:1 | **已启动** (tmux: eval_cka_15_s456) |

### 磁盘清理
已删除截断的 standard checkpoint 和 cka_only 的 optimizer.pt，释放 42G → 当前 578G/619G (94%)。

### 待办
- **standard_15 seed123 + seed456 需要重训**。建议先进一步清理磁盘（v2 的 optimizer.pt、旧 wandb offline runs 等）腾出空间后再跑。

---
