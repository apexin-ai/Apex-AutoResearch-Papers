# infra westd16639 recovery gpu saturation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd16639-recovery-gpu-saturation_20260518T173853_result.json`
- **Structured JSON:** [`101056999340867e3641.json`](../../sessions/10/101056999340867e3641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**westd-16639 恢复完成，4 张 GPU 全部 100% 饱和运行。**

| GPU | 实验 | 模型 | 数据集 | 问题数 |
|-----|------|------|--------|--------|
| 0 | exp-032 | Qwen2.5-14B | ProofWriter | 600 |
| 1 | exp-033 | Qwen3-14B (non-thinking) | ProofWriter | 600 |
| 2 | exp-036 | Qwen2.5-14B | FOLIO | 204 |
| 3 | exp-038 | Qwen2.5-14B | LogiQA | 200 |

**与计划偏差**：
- 实例被重置，所有历史 intermediates 丢失，实验从头开始
- ARC 数据不存在，GPU2 改为 FOLIO204
- Mistral-7B 模型损坏（shard 截断），GPU3 改为 Qwen2.5-14B LogiQA200；Mistral 正在后台重新下载
- exp-032 ETA ~7.5h（~45s/题），exp-036/038 预计更快完成

---
