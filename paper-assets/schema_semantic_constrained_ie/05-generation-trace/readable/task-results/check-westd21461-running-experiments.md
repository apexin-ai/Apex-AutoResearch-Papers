# check westd21461 running experiments

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd21461-running-experiments_20260523T020308_result.json`
- **Structured JSON:** [`0cbdc3908265cf636222.json`](../../sessions/0c/0cbdc3908265cf636222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

两个实验均在 **运行中**，启动于 08:40（约 1h24m 前）。

| 实验 | GPU | PID | 已完成 | 进度 | 预估剩余 |
|------|-----|-----|--------|------|----------|
| **eval_70b_zs_docred_200_full_s1** | GPU 0 | 88685 | 159/200 | 79.5% | ~25 min |
| **eval_70b_lora_docred_200_full_s2** | GPU 1 (w/ LoRA ckpt-1146) | 88995 | 46/200 | 23% | ~4.5h |

注意：s2 的日志里有 93 条 `pad_token_id` 消息但 output jsonl 只有 46 行，可能是因为 full_s2 每个 sample 需要多轮生成（先 entity 再 relation），每个 sample 输出两条日志。

ZS S1 实验预计约 25 分钟完成；LoRA S2 实验因为两阶段解码，预计还需约 4-5 小时。

---
