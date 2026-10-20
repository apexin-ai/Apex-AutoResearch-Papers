# train ft 002

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ft_002_20260514T074046_result.json`
- **Structured JSON:** [`8d646613c819d26b4bfc.json`](../../sessions/8d/8d646613c819d26b4bfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ft_002 训练已启动。**

| 项目 | 值 |
|------|-----|
| 服务器 | autodl-5090, cuda:1 |
| PID | 19666 |
| 日志 | `/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log` |
| 总步数 | 585 steps (5 epochs × 117 steps/epoch) |
| 速度 | ~3.0s/step |
| 预估时间 | ~29 分钟 |
| Checkpoint 路径 | `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2` |

**ft_002 vs ft_001 改动**:
- LoRA r=32, alpha=64（trainable params 43M → 87.3M）
- 5 epochs（原 3）
- Prompt 增加 relation direction hint
- 原始数据已备份为 `llmfactory_{train,dev}_v1.json`

---
