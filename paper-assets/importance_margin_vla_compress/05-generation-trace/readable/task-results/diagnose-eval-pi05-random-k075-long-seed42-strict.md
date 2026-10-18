# diagnose eval pi05 random k075 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k075_long_seed42_strict_20260527T053816_result.json`
- **Structured JSON:** [`2e58c80a3e5bef315264.json`](../../sessions/2e/2e58c80a3e5bef315264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验没有失败，仍在运行中。CRON 误报。**

**根因**：进程启动时缺少 `-u` 标志（unbuffered），Python 默认缓冲 stdout，导致日志文件只写入了初始化部分的 18 行（1.5KB）。CRON 检查日志未找到 W&B metrics，误判为进程退出。

关键证据：
- **PID 177597** 正在 GPU 1 上运行，10.7GB 显存，35% GPU 利用率
- `fd/1` → 指向目标日志文件 `eval_pi05_random_k075_long_seed42_strict.log`
- `CUDA_VISIBLE_DEVICES=1`，进程启动于 13:36:48
- cmdline: `python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 ...`（无 `-u`）
- 对比：同服务器上其他 pi05 进程（PID 94308, 94384）都有 `-u` 标志

**不需要重跑。** 等进程完成或 buffer flush 后日志会自动写入完整结果。

**后续建议**：启动命令应改为 `python -u eval_pi05_pruning_libero.py ...` 以避免再次误报。

---
