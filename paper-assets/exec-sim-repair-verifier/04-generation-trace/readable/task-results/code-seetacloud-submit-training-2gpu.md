# code seetacloud submit training 2gpu

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seetacloud-submit-training-2gpu_20260512T062657_result.json`
- **Structured JSON:** [`587862e77296bfb43fdc.json`](../../sessions/58/587862e77296bfb43fdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动，正在加载模型：

| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| model-size-scaling-cls8b | cuda:0 | model-size-scaling-cls8b | tokenizer 已加载，数据 train=15290/val=1896，正在加载 8B 模型 |
| model-size-scaling-cwm8b | cuda:1 | model-size-scaling-cwm8b | tokenizer 已加载，数据 train=15290/val=1896，正在加载 8B 模型 |

模型路径: `/root/autodl-tmp/models/Qwen/Qwen3-8B`。8B 模型加载到显存需要约 1-2 分钟，之后 `nvidia-smi` 会看到显存占用。

---
