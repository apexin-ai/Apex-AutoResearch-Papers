# harvest and fill mbpp cka and cuda1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_and_fill_mbpp_cka_and_cuda1_20260519T172022_result.json`
- **Structured JSON:** [`6183a882fc4999b7bed0.json`](../../sessions/61/6183a882fc4999b7bed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个问题：

1. **`sft_rasp_20` 不存在**。只有 `sft_rasp_20_westd` (12G) 和 `sft_rasp_20_1p5b` (2.8G)。
2. **数据盘 100% 满**，无法写入任何结果文件。

清理候选（中间 checkpoints）：

| 目录 | 大小 | 可清理的中间 checkpoints |
|------|------|------------------------|
| `grpo_standard_20_extended_300` | 91G | checkpoint-280, checkpoint-290 (~28G) |
| `grpo_stage2_standard_20_fair` | 61G | checkpoint-80, checkpoint-90 (~28G) |

需要你确认：
1. **SFT RASP 模型路径**：用 `sft_rasp_20_westd` 还是其他路径？
2. **磁盘清理**：是否可以删除上述目录中的中间 checkpoints（保留最终 checkpoint 和 model.safetensors）？只需清理几个就能腾出足够空间。

---
