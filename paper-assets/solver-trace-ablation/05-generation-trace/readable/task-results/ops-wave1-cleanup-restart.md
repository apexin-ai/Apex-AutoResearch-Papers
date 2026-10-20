# ops wave1 cleanup restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wave1-cleanup-restart_20260517T062326_result.json`
- **Structured JSON:** [`d654d72ad300d468a1cb.json`](../../sessions/d6/d654d72ad300d468a1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**
- 清理释放：autodl-tmp 从 ~190G used 恢复到 61G 可用（释放约 ~30G 失败 checkpoint）
- 根分区：21G 可用
- **实验 1** (plan018-additive-random-b01-s45)：PID 171186，cuda:0，48.6GB 显存，94% util
- **实验 2** (sweep-random-b005-s42)：PID 171264，cuda:1，44.8GB 显存，95% util

两个实验均正常运行，各自独占一张 GPU，无越界。

---
