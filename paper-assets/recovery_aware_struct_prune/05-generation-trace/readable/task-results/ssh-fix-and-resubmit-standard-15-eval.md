# ssh fix and resubmit standard 15 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_and_resubmit_standard_15_eval_20260520T225530_result.json`
- **Structured JSON:** [`ab8b0f989e336db7cfdb.json`](../../sessions/ab/ab8b0f989e336db7cfdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已成功启动，模型正在加载中：

**修复内容：**
1. **seed456 tokenizer.json**：0 bytes 空文件，已从 seed123 复制（11MB）
2. **GSM8K 缓存**：设 `HF_HOME=/root/autodl-tmp/.hf_cache` 指向数据盘缓存（根分区缓存已删），去掉 `HF_DATASETS_OFFLINE=1`

**提交状态（westd-29022）：**
| Job | GPU | PID | 状态 |
|-----|-----|-----|------|
| eval_std15_seed123 | cuda:2 | 293079 | 模型加载中 |
| eval_std15_seed456 | cuda:3 | 293153 | 模型加载中 |

输出路径：
- `results/eval_gsm8k_grpo_standard_15_seed123_n1319.json`
- `results/eval_gsm8k_grpo_standard_15_seed456_n1319.json`

---
