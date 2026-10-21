# ops harvest standard 1p5b and launch seed123

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_standard_1p5b_and_launch_seed123_20260519T033333_result.json`
- **Structured JSON:** [`e8d8eb65d9d3d07d90d9.json`](../../sessions/e8/e8d8eb65d9d3d07d90d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据集准备中，进程活跃（CPU 731%），GPU 已占用 12.5 GB。这对 7B 模型的 GRPO 初始化是正常的。

## 汇总

**任务 A — eval_gsm8k_sft_standard_20_1p5b（已完成）:**
| 指标 | 值 |
|---|---|
| Accuracy | **22.90%** |
| n_correct / n_total | 302 / 1319 |
| EOS rate | 90.4% |
| Avg response length | 516.7 tokens |

**任务 B — grpo_cka_only_20_seed123（已启动）:**
- tmux session: `grpo_cka_only_20_seed123`
- GPU: cuda:1, 已占 12,497 MiB
- 状态: 模型加载完成，正在准备 GSM8K 训练数据集
- 日志: `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_20_seed123.log`

---
