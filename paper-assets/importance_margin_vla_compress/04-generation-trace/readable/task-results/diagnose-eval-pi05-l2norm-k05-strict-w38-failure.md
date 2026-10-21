# diagnose eval pi05 l2norm k05 strict w38 failure

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k05_strict_w38_failure_20260527T123606_result.json`
- **Structured JSON:** [`351d509e8c5ff8479963.json`](../../sessions/35/351d509e8c5ff8479963.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结论

### 1. 原始失败原因 (`eval_pi05_l2norm_k05_long_seed42_strict_w38`)

日志共 30 行，最后一条输出 `T0 ep=10: 30%` (20:17:13 CST)，**无任何 error/traceback/CUDA error/OOM 信息**。进程静默消失。

**最可能原因：进程被外部 kill 或 SSH 会话断开导致 SIGHUP。** 证据：
- 日志输出直接截断，无 Python traceback → 不是代码异常
- 无 CUDA error → 不是 GPU 故障
- 该实验未通过 tmux/nohup 保护（日志在项目目录而非 `~/runs/`，ps 中无对应 tmux session）
- 替代实验 PID 250745 在 20:00 CST 已启动在 GPU3 上（比 _w38 的 20:10 早 10 分钟），两者共享 GPU3，可能被手动 kill 以避免冲突

### 2. 替代实验状态（PID 250745）— 正常推进

| 指标 | 值 |
|------|-----|
| 进程 | PID 250745, `nohup` 启动, GPU3 |
| Task 0 | **完成** — 29/50 = 58.0% (20.2min) |
| Task 1 | 进行中 — 16/30 = 53% (截至 20:34 CST) |
| GPU 占用 | 10670MiB, 29% util |
| 预估完成 | ~3h 总时长，约 23:00 CST |

### 3. GPU3 确认

nvidia-smi 显示 GPU3 仅有 PID 250745 一个进程，无资源冲突。

### 结论

无需进一步干预。替代实验运行正常，预计在截止时间前完成。原始失败是进程管理问题（缺 session 保护），非代码 bug。

---
