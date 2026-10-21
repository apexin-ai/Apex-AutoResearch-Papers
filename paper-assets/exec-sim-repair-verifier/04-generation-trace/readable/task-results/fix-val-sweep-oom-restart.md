# fix val sweep oom restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_val-sweep-oom-restart_20260515T172200_result.json`
- **Structured JSON:** [`95f4c60875499387d432.json`](../../sessions/95/95f4c60875499387d432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **cuda:0 空闲** ✓ — 0 MiB，旧进程 393951 已死，无残余进程
2. **脚本修改** — 原 `--batch_size 8` 删除后默认值是 16（更糟），最终显式设为 `--batch_size 1`，并加 `PYTORCH_ALLOC_CONF=expandable_segments:True`
3. **已完成 checkpoint** — 无（eval_results 目录为空，从 ckpt-1800 开始全量重跑）
4. **新 PID** — 396591
5. **启动验证** ✓
   - 进程存活，运行 35 秒
   - cuda:0 占用 17.8GB / 32GB（headroom 充足）
   - 日志正常推理中：ckpt-1800 已到 150/9335，running_acc=86.0%

---
