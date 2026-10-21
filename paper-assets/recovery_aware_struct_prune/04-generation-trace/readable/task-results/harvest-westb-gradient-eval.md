# harvest westb gradient eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westb-gradient-eval_20260517T103720_result.json`
- **Structured JSON:** [`30067c8e7137d299fb62.json`](../../sessions/30/30067c8e7137d299fb62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gradient post-SFT eval 结果

| 指标 | 值 |
|---|---|
| **模型** | `sft_gradient_20` |
| **GSM8K Accuracy** | **61.50% ± 3.44%** (123/200) |
| **EOS rate** | 99.5% (199/200 natural) |
| **Avg response length** | 167.5 tokens |
| **结果文件** | `eval_gradient_postsft.json`（非 `eval_gradient_sft_20.json`） |

## 当前 GPU 状态

| GPU | 状态 | 进程 |
|---|---|---|
| cuda:0 | 空闲 (0MiB) | — |
| cuda:1 | 76% (12.9GB) | `eval_postprune_random_20` (200 samples) 运行中 |

活跃 tmux: `scoring_ablation_random`, `scoring_ablation_v2`

## 磁盘

`/root/autodl-tmp`: 162G/250G (65%)

---
