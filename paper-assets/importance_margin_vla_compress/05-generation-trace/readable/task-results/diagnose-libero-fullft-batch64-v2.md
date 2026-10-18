# diagnose libero fullft batch64 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_libero_fullft_batch64_v2_20260517T081148_result.json`
- **Structured JSON:** [`58cbe0df76dde09557bc.json`](../../sessions/58/58cbe0df76dde09557bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diagnosis_fullft_batch64_v2_crash.md`。

## 结论

**崩溃原因: native code segfault (SIGSEGV)**, 高置信度。

核心证据:
- Run 2 证明 SIGTERM handler 正常工作，但 Run 1/3 的 handler 从未触发 — 进程被不可捕获的信号杀死
- `faulthandler` 未启用，segfault 不产生任何输出，完美解释"静默死亡"
- 崩溃点不固定 (step 3550 vs step 100)，符合 native 内存损坏的非确定性特征
- 已排除 cgroup OOM (oom_kill=0)、CUDA OOM、磁盘满、GPU 硬件错误
- 嫌疑最大的是 `libsvtav1` 视频编解码器，每个 batch 都调用

**当前状态**: 手动重启 (PID 17960) 也已失败，因为未设 `HF_HUB_OFFLINE=1` 导致 HF Hub 网络错误。GPU 全部空闲，无训练在跑。

**下一步**: 在 train.py 开头加 `faulthandler.enable()`，重新启动训练。下次崩溃时就能看到完整的 C-level stack trace，精确定位 segfault 来源。

---
