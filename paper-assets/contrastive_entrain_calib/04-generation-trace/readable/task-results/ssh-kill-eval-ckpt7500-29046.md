# ssh kill eval ckpt7500 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-eval-ckpt7500-29046_20260522T172718_result.json`
- **Structured JSON:** [`806aedd39c8e29562661.json`](../../sessions/80/806aedd39c8e29562661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据很清晰了。gs8 step time 已经在快速恢复，从 kill 前 ~44s 降到最新 ~24.5s。

汇报：

```
1. eval ckpt-7500 (PID 517336): ✅ KILLED (SIGTERM 成功)
2. gs8 step time: kill 前 ~44s → kill 后 ~24.5s (已恢复正常)
   - step 125-134: 42-44s/it (eval 占 GPU0 期间)
   - step 135: 39.8s (eval 刚被 kill)
   - step 139: 28.5s (恢复中)
   - step 143-144: 24.5-24.8s (已恢复到正常水平)
3. gs8 current step: 144/8000 (1.8%)
4. eval ckpt-8000 (PID 517417): ✅ 已完成 (EXIT_CODE=0, 362 samples, 耗时 5010s)
5. exp-004-s2-v2: step 4610/8000 (57.6%), step_time ~9.2s, 运行 6h38m
```

---
