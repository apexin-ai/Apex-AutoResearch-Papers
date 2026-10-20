# run cleanup 5090 check 32b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_cleanup_5090_check_32b_20260521T053116_result.json`
- **Structured JSON:** [`422e00442069272ee189.json`](../../sessions/42/422e00442069272ee189.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报如下：

---

### 1. rsync/auto-launch 清理
**已全部清理。** 0 个残留进程。

### 2. 32B 模型
**存在**，路径 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-merged/`，大小 **62GB**（14 个 safetensors 分片，完整）。今天 08:19 写入完成。

### 3. 5090 上所有可用模型

| 模型 | 路径 | 大小 | 类型 |
|------|------|------|------|
| **Qwen2.5-32B FewNERD merged** | `checkpoints/qwen25-32b-fewnerd-merged/` | 62G | merged 完整模型 |
| **Qwen3-8B FewNERD exp021 merged** | `checkpoints/qwen3-8b-fewnerd-exp021-merged/` | 22G | merged 完整模型 |
| **Qwen3-8B CoNLL2003 merged** | `checkpoints/qwen3-8b-conll2003-merged/` | 5.2G | merged 完整模型 |
| Qwen3-8B FewNERD 5epoch LoRA | `checkpoints/qwen3-8b-fewnerd-5epoch-lora/` | 3.4G | LoRA adapter |
| Qwen3-8B SciERC LoRA v2 | `checkpoints/qwen3-8b-scierc-lora-v2/` | 3.4G | LoRA adapter |
| Qwen3-4B SciERC LoRA | `checkpoints/qwen3-4b-scierc-lora/` | 2.6G | LoRA adapter |
| Qwen3-8B CoNLL2003 LoRA | `checkpoints/qwen3-8b-conll2003-lora/` | 2.0G | LoRA adapter |
| Qwen3-8B SciERC 10epoch LoRA | `checkpoints/qwen3-8b-scierc-10epoch-lora/` | 1.4G | LoRA adapter |
| Qwen3-8B SciERC 3epoch LoRA | `checkpoints/qwen3-8b-scierc-3epoch-lora/` | 1.4G | LoRA adapter |
| Qwen3-8B SciERC LoRA rank8 | `checkpoints/qwen3-8b-scierc-lora-rank8/` | 895M | LoRA adapter |

基座模型在 `/root/autodl-tmp/models/`：Qwen2.5-7B-Instruct、Qwen3-4B。HF cache 仅有 deberta-v3-base。

### 4. GPU 状态
4 张 GPU **全部空闲**：

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 2 MiB | 0% |
| 1 | 2 MiB | 0% |
| 2 | 2 MiB | 0% |
| 3 | 2 MiB | 0% |

---
