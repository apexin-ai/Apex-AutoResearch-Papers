# ops disk cleanup 37g

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-37g_20260515T124637_result.json`
- **Structured JSON:** [`28203f3d7f32c85d9403.json`](../../sessions/28/28203f3d7f32c85d9403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 项清理完成。

## 清理结果

| # | 目标 | 回收 |
|---|------|------|
| 1 | exp1_isr_b03_s42_1000/checkpoint-1000 | ~15G |
| 2 | plan018_additive_random_b01_s42_1000/checkpoint-1000 | ~15G |
| 3 | .hf_cache/Qwen/Qwen2.5-1.5B-Instruct | ~3G |
| 4 | .hf_cache/Qwen/Qwen2.5-0.5B | ~1G |
| 5 | .hf_cache/openai-community | ~1G |
| 6 | .hf_cache/models--openai-community--gpt2 | ~0.4G |
| 7 | gpt2-small | ~0.5G |

**总回收：~36G**
**磁盘状态：217G/250G (87%) → 181G/250G (73%)**

无异常，所有目标均存在且内容符合预期，两个 checkpoint 删除前已确认父目录有完整模型权重。

---
