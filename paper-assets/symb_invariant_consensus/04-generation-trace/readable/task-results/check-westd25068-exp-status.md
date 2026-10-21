# check westd25068 exp status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd25068-exp-status_20260518T153301_result.json`
- **Structured JSON:** [`0b014c5a63e83711e6f6.json`](../../sessions/0b/0b014c5a63e83711e6f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。报告如下：

## 进程状态

| 实验 | PID | 状态 | GPU | 进度 | ETA |
|------|-----|------|-----|------|-----|
| exp-027 (Qwen3 non-thinking) | 38106 | **ALIVE** | GPU 1 (97%, 88GB) | ~98/204 | ~93 min |
| exp-028 (Qwen3 thinking) | 40990 | **ALIVE** | GPU 2 (97%, 88GB) | ~16/204 | ~856 min (~14h) |
| exp-030 (Cross-model Mistral) | 46525 | **ALIVE** | GPU 0 (96%, 88GB) | 139/204 | ~20 min |
| exp-029 (Contrastive) | 42353 | **DEAD (完成)** | GPU 3 (idle) | 182/182 | -- |

## GPU 分配
- **GPU 0**: vLLM Mistral-7B (port 8000) → exp-030
- **GPU 1**: vLLM Qwen3-14B non-thinking (port 8001) → exp-027
- **GPU 2**: vLLM Qwen3-14B thinking (port 8002) → exp-028
- **GPU 3**: 空闲 (exp-029 已完成并释放)

## exp-029 结果
- Contrastive SICA: **0.7253** (132/182)
- SC baseline: **0.7363** (134/182)
- Delta: **-0.0110** (负值，contrastive 未带来增益)
- EXIT_CODE=0，耗时 47.2 min

## Registry 修复
- exp-027: PREPARING → **RUNNING** ✓
- exp-028: PREPARING → **RUNNING** ✓
- exp-030: PREPARING → **RUNNING** ✓
- exp-029: RUNNING → **DONE(success)** ✓

注意：exp-028 (thinking mode) 速度极慢（~53s/题 vs exp-027 的正常速度），预计还需 14 小时，可能是 thinking mode 生成长 CoT 导致。

---
