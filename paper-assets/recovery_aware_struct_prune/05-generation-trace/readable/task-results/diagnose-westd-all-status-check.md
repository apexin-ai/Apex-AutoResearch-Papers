# diagnose westd all status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_all_status_check_20260522T141111_result.json`
- **Structured JSON:** [`b828dde3cc13da1b30c6.json`](../../sessions/b8/b828dde3cc13da1b30c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== P0: MF5 depth-first eval 结果 ===
NO_RESULT_FILES (results/eval_gsm8k*depth_first*.json 不存在)
NO_RESULT_ALT (/root/autodl-tmp/ 路径也不存在)
NO_SFT_RESULT
NO_GRPO_RESULT
NO_SFT_LOG
NO_GRPO_LOG

=== P1: seed123 eval 进度 (westd:2) ===
Evaluating: 79% | 1041/1319 [1:33:40]
Progress @ 1000/1319: acc=0.5300, eos_rate=99.30%, avg_len=180
Progress @  950/1319: acc=0.5347, eos_rate=99.37%, avg_len=178

=== P2: α=3.0 GRPO eval 进度 (westd:0) ===
Evaluating: 81% | 1067/1319 [2:10:03]
Progress @ 1050/1319: acc=0.6343, eos_rate=98.67%, avg_len=218
Progress @ 1000/1319: acc=0.6300, eos_rate=98.60%, avg_len=221
NO_ALPHA3_V2_LOG

=== GPU 总览 ===
GPU  | mem_used   | mem_total  | util
  0  | 29599 MiB  | 97887 MiB  | 99%   ← PID 43755 (α=3.0 GRPO eval)
  1  |     0 MiB  | 97887 MiB  |  0%   ← idle
  2  | 26219 MiB  | 97887 MiB  | 90%   ← PID 46229 (seed123 eval)
  3  |     0 MiB  | 97887 MiB  |  0%   ← idle
```

**小结**：P0 depth-first 的 eval 结果文件和日志均不存在（未启动或路径不对）。P1 seed123 和 P2 α=3.0 两个 eval 都在跑，分别在 cuda:2 (79%, acc≈53%) 和 cuda:0 (81%, acc≈63.4%)，预计各剩 ~10-15 分钟。cuda:1 和 cuda:3 空闲。

---
