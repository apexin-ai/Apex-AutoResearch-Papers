# check exp 055 cron exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_055_cron_exit_20260523T233107_result.json`
- **Structured JSON:** [`b99d50c08f5b77c4eae6.json`](../../sessions/b9/b99d50c08f5b77c4eae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清除或未在本 session 创建）。

```
=== exp_055 PegInsertion trained s1 ===
进程退出原因: 正常完成（无 error/traceback）
最终步数: 222.4K（目标 210K）
ve_ratio_max: 3.08 @92.5K
ve_ratio_final: 0.50 @212.5K
eval_peak: 24.05 @112.5K
eval_final: 11.44 @212.5K
conclusion: success

s1 确认 PegInsertion CIVO 跨 seed 可复现（s0 peak 10.05, s1 peak 3.08）。
s1 严重程度较低，且部分自修复（3.08→0.50）。Eval 整体低（PegInsertion 本身难），
但 CIVO 期间（52.5K-102.5K）eval 进一步被压制（7-10 vs 后期 20+）。
```

---
