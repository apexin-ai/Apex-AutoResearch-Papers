# ssh westd emergency disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_emergency_disk_cleanup_20260521T031817_result.json`
- **Structured JSON:** [`b8f863a5f2258988bb80.json`](../../sessions/b8/b8f863a5f2258988bb80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

**清理前**: 619G/619G used, **1.4MB** 可用 (100%)
**清理后**: 599G/619G used, **21GB** 可用 (97%)

**已删除**:
| 文件 | 大小 |
|------|------|
| `grpo_cka_only_25/checkpoint-100/optimizer.pt` | 15GB |
| `grpo_rasp_20_seed456/checkpoint-100/optimizer.pt` | 6.8GB |
| **合计释放** | **~21.8GB** |

**未达 40GB 目标**。磁盘上没有更多 optimizer.pt 可删。以下是可进一步释放空间的候选项（需要你确认）：

| 候选 | 大小 | 说明 |
|------|------|------|
| `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` | 15GB | 基础模型，pruned 模型已独立保存 |
| `grpo_cka_only_20_seed456/checkpoint-100/` | 12GB | 父目录已有 final model，checkpoint 冗余 |
| 其他 7 个 checkpoint-100 目录 | 各 ~5-12GB | 同上，训练完成后的中间 checkpoint |

21GB 可用应足够保存一次 RASP checkpoint（model.safetensors ~11GB），但如果训练也保存 optimizer state 则可能不够。是否需要删除上述候选项？

---
