# check sft eval s43 s44 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sft_eval_s43_s44_results_20260518T152252_result.json`
- **Structured JSON:** [`1e35c620690c905b7b09.json`](../../sessions/1e/1e35c620690c905b7b09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### SFT s43 eval — 失败
**错误**: `inference.py` 检测到 `/root/autodl-tmp/sft_output_seed43/` 是 LoRA adapter，触发了要求 `--sft_adapter` 的校验。这个校验是为 RSFT/DPO/GRPO 设计的——SFT adapter 本身不需要 `--sft_adapter`，但代码逻辑把所有 adapter 都拦截了。

### SFT s44 eval — 失败
**错误**: 同上，`/root/autodl-tmp/sft_output_seed44/` 被同一校验拦截。

### GPU 状态
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 0 MiB | 空闲 |
| 1 | 0 MiB | 空闲 |
| 2 | 16631 MiB (PID 542126) | 占用 |
| 3 | 0 MiB | 空闲 |

### 问题分析

`inference.py:420` 的校验逻辑有 bug：它检测到 adapter_config.json 就要求 `--sft_adapter`，但 SFT adapter 本身作为 model_path 时不需要这个参数。需要看一下这个校验逻辑，区分"model_path 本身就是 SFT adapter"和"model_path 是 RSFT/DPO adapter 需要先合并 SFT"的情况。

要我查看 `inference.py` 的校验逻辑并修复吗？

---
