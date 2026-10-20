# urgent kill eval and cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill-eval-and-cleanup_20260514T115006_result.json`
- **Structured JSON:** [`07a9525884763c369f2e.json`](../../sessions/07/07a9525884763c369f2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告：

1. **进程清理**: 4 个问题进程 (567813, 570264, 570911, 565583) 全部成功 kill
2. **GPU VRAM**:
   - GPU 0: 80223/97887 MiB (91%) — 另一个训练任务 PID 564905
   - GPU 1: 55903/97887 MiB (7%) — 仅剩 plan009-sft-r4 (PID 572609)，eval 进程占用的 VRAM 已释放
3. **plan009-sft-r4**: 正常运行，step 100/500，速度 ~1.25 it/s
4. **卡死原因**: `eval_results.json` 存在 (441KB, 19:48 写入)，说明 eval 可能在评估完成后的后处理阶段卡住（而非文件锁问题）。已删除可能损坏的输出文件
5. **当前 GPU 状态**: 两张卡各跑一个训练任务，无残留 eval 进程

---
