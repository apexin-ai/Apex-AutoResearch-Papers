# ops falcon3 cqa1 kill restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-cqa1-kill-restart_20260522T074755_result.json`
- **Structured JSON:** [`cadaf70cb36a9dd2203c.json`](../../sessions/ca/cadaf70cb36a9dd2203c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

### 报告

1. **旧进程已终止**: 父进程 652456 + 5 个子进程（652461, 652759-652762）全部 kill -9 终止
2. **错误 checkpoint 已清理**: `Falcon3-7B-Base_d100_s42/` 目录和 log 文件已删除
3. **新训练状态**:
   - PID: 666093
   - GPU 0: 19545 MiB / 24564 MiB（与之前 19.5GB 一致）
   - 训练速度: ~4s/step，总 4159 steps，预计约 4.6 小时
   - `--lr 5e-5` 已通过 `/proc/666093/cmdline` 确认正确传入
   - LoRA config: r=16, alpha=32（正确）
   - bitsandbytes warning 非致命，不影响训练
4. **无异常**

---
