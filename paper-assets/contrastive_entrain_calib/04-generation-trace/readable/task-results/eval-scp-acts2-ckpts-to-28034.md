# eval scp acts2 ckpts to 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_scp-acts2-ckpts-to-28034_20260522T134005_result.json`
- **Structured JSON:** [`5a773b0dfde45a8eba79.json`](../../sessions/5a/5a773b0dfde45a8eba79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**汇报：**

- **SCP**: checkpoint-2000 和 checkpoint-3000 从 29046 成功传到 28034（通过 SSH 密钥中转，各 ~698MB adapter）
  - 注意：29046 上没有 checkpoint-2500，实际只有 checkpoint-2000 和 checkpoint-3000，已传这两个
- **Eval 已启动**:
  - GPU0: `eval_acts2_ckpt2000` — checkpoint-2000, 362 pairs, 运行中
  - GPU1: `eval_acts2_ckpt3000` — checkpoint-3000, 362 pairs, 运行中
  - GPU2/GPU3 空闲

---
