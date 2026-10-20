# ssh diagnose mf3 n500 exit westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_mf3_n500_exit_westb1_20260522T142817_result.json`
- **Structured JSON:** [`533013c1faf3f99dd3a0.json`](../../sessions/53/533013c1faf3f99dd3a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

1. **进程退出原因：被 kill**。日志中无 error/traceback/signal 记录，日志仅 8 行（停在 26/500，约 5% 进度）。从 v2 的启动命令可以看到 `kill 217502` 前缀，确认是被主动 kill 后重启的。原始 PID 202364 已不存在。

2. **无结果 JSON**。`eval_gsm8k_grpo_qwen_math_cka_only_20_n500.json` 不存在——进程在完成前被终止，未产出结果。

3. **v2 已在运行**。PID 217798，使用 `max_new_tokens=2048`，输出到 `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2.json`，刚启动约 30 秒，正在加载中。

---
