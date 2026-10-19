# diagnose eval obs only object norm003 seed47 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed47-r2_20260519T125353_result.json`
- **Structured JSON:** [`0fbc4eeed4f51c19cbb3.json`](../../sessions/0f/0fbc4eeed4f51c19cbb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中无 error/oom/traceback 相关关键词，已有足够信息得出结论。

## 诊断结论

**根因：SIGHUP（信号1 → EXIT_CODE=128+1=129）**。进程在运行过程中收到 SIGHUP 信号被终止，日志最后一行显示 `Terminated`。这通常是 **tmux/screen session 断开或被关闭** 导致的——当承载进程的终端会话丢失时，系统会向前台进程发送 SIGHUP。日志中没有任何 OOM、CUDA error、Python traceback 或异常堆栈，排除代码 bug 和内存不足。

**最后进度**：10 个 task 中已完成 4 个（task 0-3），正在执行第 5 个 task（`pick_up_the_ketchup`）的第 5/10 个 rollout 时被终止。已完成的 4 个 task 成功率分别为 0%、0%、20%、30%。

**cuda:3 当前状态**：可用，显存占用 3871/24564 MiB（16%），GPU 利用率 27%，说明原进程已释放资源，GPU 可正常使用。

**部分结果**：输出 JSON 文件 `eval_object_obs_only_norm003_seed47.json` 不存在，说明评估脚本在全部 task 完成前被杀，没有写出结果文件，无部分结果可用。

---
