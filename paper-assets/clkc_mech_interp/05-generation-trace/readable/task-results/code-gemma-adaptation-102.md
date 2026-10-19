# code gemma adaptation 102

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-adaptation-102_20260522T030538_result.json`
- **Structured JSON:** [`d5be147d828c81398d22.json`](../../sessions/d5/d5be147d828c81398d22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。兼容性检查结果：

**三个脚本均无需代码修改**，直接通过命令行参数切换即可用于 Gemma-2-9B-IT。

| 脚本 | 状态 | 说明 |
|------|------|------|
| verify_parametric_knowledge.py | ✅ 兼容 | `enable_thinking=False` 被 Gemma 静默接受；`strip_think_tags` 无副作用 |
| collect_activations.py | ✅ 兼容 | `model.model.layers` 结构一致（42层 Gemma2DecoderLayer）；padding_side=left 一致 |
| train_probe.py | ✅ 兼容 | 无硬编码维度，自动适配 hidden_size=3584 |

Gemma-2-9B 关键参数：42层、hidden_size=3584、GQA(16h/8kv)、无 thinking mode、专用 pad_token。数据目录 `data/gemma2/` 已创建。报告已写入 `memory.md`。

---
