# ssh kill duplicate paraphrase

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-duplicate-paraphrase_20260513T190848_result.json`
- **Structured JSON:** [`423d2527ec1ba018a5eb.json`](../../sessions/42/423d2527ec1ba018a5eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Cleanup Summary ===
Killed PIDs: 191459, 196320, 196968 (confirmed dead)
Surviving:
  GPU 0: MMLU - PID 200967 - ✗ DEAD (残留显存 22951 MiB)
  GPU 1: GSM8K - PID 189375 - ✓ alive, 67% (28/42 batches, ~42s/batch)
  GPU 2: ARC - PID 190717 - ✓ alive, 62% (23/37 batches, ~49s/batch)
  GPU 3: idle ✓
  GPU 4: HumanEval - PID 201102 - ✓ alive, vLLM processing (~97%)
  GPU 5: idle ✓
Corrupt files cleaned: 0 (output目录为空，尚无 .json 文件输出)
```

**需要注意**: MMLU 进程 (PID 200967) 已死，GPU 0 残留 ~23GB 显存。可能是被误杀（它可能是被 kill 的某个 PID 的子进程），或者自行崩溃。MMLU 的 vLLM 日志 (phase1_mmlu_vllm) 显示处理到 98% 时停止。

需要决定是否重启 MMLU 任务。

---
