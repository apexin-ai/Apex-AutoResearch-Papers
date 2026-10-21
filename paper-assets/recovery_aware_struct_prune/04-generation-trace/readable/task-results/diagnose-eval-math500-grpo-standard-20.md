# diagnose eval math500 grpo standard 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_grpo_standard_20_20260518T031704_result.json`
- **Structured JSON:** [`f47f881d18537469495e.json`](../../sessions/f4/f47f881d18537469495e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**进程正常运行，无需 kill。**

- **状态**：PID 14556 在 cuda:1 上活跃（GPU 98%, 34.5GB 显存, 1081min CPU 时间）
- **当前进度**：**409/500**（81.8%），最新日志时间约 17h47m（进程运行时间内）
- **中间准确率**：400 题时 Acc = **0.2525**（25.25%）
- **平均速度**：约 2.6 min/sample（波动范围 ~1-5 min/sample）
- **预估剩余**：91 题 × ~2.6 min ≈ **4 小时**左右完成
- **日志位置**：`/root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log`（非标准位置，不在 `/root/runs/` 下）
- **tmux session**：进程不在以 `eval_math500_grpo_standard_20` 命名的 tmux session 中（可能直接在后台启动或 session 名不同）

结论：让它继续跑，预计再约 4 小时完成全部 500 题。

---
