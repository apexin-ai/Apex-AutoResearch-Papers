# monitor datagen progress check 3

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_datagen-progress-check-3_20260519T184734_result.json`
- **Structured JSON:** [`de7efbe75590cb411fc4.json`](../../sessions/de/de7efbe75590cb411fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen 任务只有 progress 文件没有最终 jsonl，说明脚本先写 progress，完成后才生成最终文件。

| GPU | 任务 | 进程 | 进度 | 上次→本次 | 速率 | 状态 | ETA |
|-----|------|------|------|-----------|------|------|-----|
| 0 | Llama jailbreak | 无（已释放） | **251/250** | 217→251 | — | **已完成** ✓ | — |
| 1 | Llama benign | PID 278684 (18.3GB) | **193/250** (77%) | 138→193 (+55) | ~55/h | 运行中 | ~1h |
| 2 | Qwen jailbreak | PID 281219 (19.0GB) | **158/250** (63%) | 104→158 (+54) | ~54/h | 运行中 | ~1.7h |
| 3 | Qwen benign | PID 281298 (19.0GB) | **120/250** (48%) | 80→120 (+40) | ~40/h | 运行中 | ~3.2h |

**Llama jailbreak 已完成**：251 行（含可能的表头或多生成 1 条），文件 4.3MB，字段包含 `conversation_id, turns, label, source, attack_type, num_turns, strategy_sequence, metadata`，格式正确。

其余 3 个任务正常推进，无异常。Qwen benign 最慢，预计还需 ~3 小时。

---
