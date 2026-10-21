# check cls home progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cls-home-progress_20260512T185915_result.json`
- **Structured JSON:** [`f5f246b398592cccf2d2.json`](../../sessions/f5/f5f246b398592cccf2d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**repo-level-cls-home 训练状态**

| 项目 | 值 |
|------|-----|
| 进程 | PID 2840844 存活，已运行 1h45m |
| GPU | 19456 MiB VRAM 占用 |
| 进度 | **862 / 6633** (13%) |
| 速度 | ~7.11 s/it |
| 已用时 | 1h 42m |
| 剩余预估 | **~11h 24m** |
| ETA | **2026-05-12 ~23:24 UTC** |
| Loss | 日志中未打印 loss（只有 tqdm 进度条） |
| Checkpoint | **无**（目录为空，尚未保存） |

注意：训练脚本没有在日志中输出 loss 值，且尚无 checkpoint 保存。如果需要 loss 监控或中途 checkpoint，可能需要检查训练脚本的 logging/save 配置。

---
