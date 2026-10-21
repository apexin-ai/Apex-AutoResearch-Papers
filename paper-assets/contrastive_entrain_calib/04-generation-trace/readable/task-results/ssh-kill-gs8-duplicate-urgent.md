# ssh kill gs8 duplicate urgent

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-gs8-duplicate-urgent_20260522T163843_result.json`
- **Structured JSON:** [`217dbb3fbc2a20468506.json`](../../sessions/21/217dbb3fbc2a20468506.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

```
1. Kill 结果: PID 519538 — KILLED ✓
2. 存活 gs8 进程: PID 516696, step 71/8000 (仍在运行)
3. Step time: kill 后仍 ~65s/it，未恢复
   ⚠️ 原因: eval ckpt-7500 (PID 517336) 也在 GPU0 上，占用 16.9GB 显存 + 178% CPU
   GPU0 总占用 55GB/98GB，但 compute 争用导致 step time 未降
4. Eval 进程:
   - ckpt-7500 (PID 517336): 正在运行，GPU0, 进度 180/362，已跑 1h
   - ckpt-8000 (PID 517417): 正在运行，GPU1, 进度 240/362，已跑 1h
   两个 eval 都在正常推进，不是卡住
5. Checkpoints (exp003_gs8): 0 个 — 训练刚到 step 71，还没到第一个 save point
   seed2 已完成的 checkpoints (500~8000 + final) 完整
```

**Step time 没恢复的根因是 eval ckpt-7500 在 GPU0 上跟训练抢 compute。** ckpt-8000 eval 预计再 ~25min 完成 (240/362)，ckpt-7500 eval 预计再 ~35min 完成 (180/362)。ckpt-7500 结束后 GPU0 上只剩训练进程，step time 应恢复到 ~25s。

要不要现在 kill 掉 GPU0 上的 eval ckpt-7500 (PID 517336) 来立即恢复训练速度？它可以之后单独重跑。

---
