# setup openvla oft download

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_openvla-oft-download_20260522T050256_result.json`
- **Structured JSON:** [`991560bc1a6cd8e1ffcb.json`](../../sessions/99/991560bc1a6cd8e1ffcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成。总结：

| 项目 | 结果 |
|------|------|
| **HuggingFace Model ID** | `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` |
| **模型路径** | `/root/autodl-tmp/models/openvla-oft/` (15GB) |
| **代码仓库** | `/root/openvla-oft-code/` (github.com/moojink/openvla-oft) |
| **磁盘剩余** | 74GB (250GB 中用了 177GB) |
| **下载状态** | ✅ 完成 (25/25 files, 6分19秒) |

模型组成：
- 4 个 safetensors 分片 (4.6G + 4.7G + 4.7G + 251M = ~14.2GB base weights)
- `action_head--300000_checkpoint.pt` (289MB) — action head
- `proprio_projector--300000_checkpoint.pt` (65MB) — proprioception projector
- `lora_adapter/` — LoRA adapter weights
- tokenizer + config 文件

这个是覆盖全部 LIBERO 子任务 (spatial + object + goal + 10) 的综合 fine-tuned 版本。

---
