# ops westd redeploy 4gpu v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_redeploy_4gpu_v2_20260516T111715_result.json`
- **Structured JSON:** [`0495462787e5ea71736e.json`](../../sessions/04/0495462787e5ea71736e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个任务运行正常。

---

## 产出汇总

| GPU | 任务 | PID | 模型路径 | 状态 |
|-----|------|-----|----------|------|
| cuda:0 | RASP 20% eval N=200 | 1911→1917 | `sft_qwen_math_rasp_20` | ~44/200 推进中, ~2.5s/it |
| cuda:1 | Standard 20% eval N=200 | 2008→2013 | `sft_qwen_math_standard_20` | 运行中 |
| cuda:2 | RASP 25% SFT | 2525→2530 | `pruned_rasp_25_qwen_math` | 34/1870 训练中, ~1.1it/s |
| cuda:3 | Standard 25% SFT | 2621 | `pruned_standard_25_qwen_math` | 1/1870 训练中 |

**GPU 内存占用**: 0→12.7GB, 1→12.7GB, 2→11.8GB, 3→11.8GB

**EOS 修复内容** (eval_gsm8k.py):
- 两处 `gen_kwargs` 均添加 `eos_token_id=[151643, 151645]`（Qwen 的 `<|im_end|>` + `<|endoftext|>`）
- 两处 `hit_eos` 检查改为 `generated[-1].item() in (151643, 151645)`

---
