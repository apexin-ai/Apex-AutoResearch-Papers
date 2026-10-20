# diagnose westd full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_full_status_20260522T121343_result.json`
- **Structured JSON:** [`cd796d2b6dc7773c920b.json`](../../sessions/cd/cd796d2b6dc7773c920b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU STATUS ===
0, 29137 MiB, 97887 MiB, 93 %
1, 17651 MiB, 97887 MiB, 98 %
2, 0 MiB, 97887 MiB, 0 %
3, 31358 MiB, 97887 MiB, 95 %

=== α=3.0 GRPO eval (GPU 0, PID 43755) ===
 43755       19:17  130
RUNNING
Evaluating:  15%|█▌        | 200/1319 — acc=0.6500, eos_rate=100.00%, avg_len=165
（最新进度约 15%，已运行 19m17s）

=== α=3.0 SFT eval (GPU 2) ===
NO_RESULT_FILE
NO_LOG

=== GRPO random seed123 eval (GPU 3) ===
NO_LOG（进程在跑但 log 可能被 tee 缓冲）

=== MF5 depth-first (GPU 3) ===
depth-first GRPO eval 正在 GPU 3 上运行（PID 40073，已运行 73m）

=== MATH-500 (GPU 1) ===
NO_LOG

=== ALL RUNNING PYTHON PROCS ===
- PID 43755 (GPU 0): eval_gsm8k GRPO RASP α=3.0 — 运行中
- PID 40073 (GPU 3→实际占用): eval_gsm8k GRPO depth-first — 运行中 (73m)
- PID 41541 (GPU 3): eval_gsm8k GRPO random seed123 — 运行中 (56m)
- GPU 1: MATH-500 相关进程在跑（17.6GB 显存占用）但未匹配 grep 模式
- GPU 2: 空闲（0 MiB）
```

---
