# diag exp052 exit check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp052-exit-check_20260519T010407_result.json`
- **Structured JSON:** [`f70269d31ecadf2adb6f.json`](../../sessions/f7/f70269d31ecadf2adb6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成。

```
exp-052: COMPLETED
  结果文件: 存在 (313KB, May 19 09:03)
  intermediates: 3 files
  wall time: 81.9 min
  SICA = 57.4% (117/204)
  SC   = 53.9% (110/204)
  delta = SICA - SC = +3.5pp
  extraction rate: 97.1%, contradiction rate: 3.4%

exp-053: COMPLETED
  结果文件: 存在 (317KB, May 19 09:02)
  intermediates: 3 files
  wall time: 80.8 min
  SICA = 55.9% (114/204)
  SC   = 56.4% (115/204)
  delta = SICA - SC = -0.5pp
  extraction rate: 97.0%, contradiction rate: 3.3%
```

Cron 报告正确——进程已退出是因为实验跑完了，不是失败。

vLLM 仍在 8002/8003 端口运行（GPU 0-1 100% util 在服务请求，GPU 2-3 idle）。如果不再需要，可以关掉释放 GPU。

**Seed 间差异**：exp-052 (seed=123) SICA 优于 SC +3.5pp，但 exp-053 (seed=456) SICA 略低于 SC -0.5pp，说明 SICA 的优势在 seed 间不稳定。

---
