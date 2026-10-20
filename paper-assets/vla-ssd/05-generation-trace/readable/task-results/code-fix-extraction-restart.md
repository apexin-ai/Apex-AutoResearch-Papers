# code fix extraction restart

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-extraction-restart_20260515T125118_result.json`
- **Structured JSON:** [`782ddddc889118a5a141.json`](../../sessions/78/782ddddc889118a5a141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**总结：**

| 操作 | 结果 |
|------|------|
| Kill stray train_probes.py | 7 个进程全部清除 |
| Kill untrained extraction | 已终止（PID 28160） |
| Trained extraction | 自然完成（EXIT_CODE=0，185.3 min） |
| 修复 extract_features.py | 264→2 次 .cpu()/batch + 增量写盘 |
| Untrained 重跑 | 2 个 task（LIVING_ROOM_SCENE6 + STUDY_SCENE1）18.5 min 完成 |

**特征文件完整性：**
- `features/trained/` — 10/10 task .h5 文件 ✓
- `features/untrained/` — 10/10 task .h5 文件 ✓

**性能改善：** 0.8 step/s → ~42 step/s（52x 加速）

---
