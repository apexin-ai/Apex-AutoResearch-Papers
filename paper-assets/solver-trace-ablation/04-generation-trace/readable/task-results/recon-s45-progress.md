# recon s45 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_s45-progress_20260522T014130_result.json`
- **Structured JSON:** [`afa27801ebd88974d3da.json`](../../sessions/af/afa27801ebd88974d3da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**s45 训练状态：正在运行**

| 指标 | 值 |
|------|-----|
| 当前 step | 865 / 1000 |
| 进度 | 86% |
| 已运行 | ~1h58m |
| 剩余估计 | ~17 min |
| GPU 占用 | 64,577 / 97,887 MiB (66%) |
| GPU 利用率 | 55% |
| Checkpoint | 已保存（最新） |
| Eval | 未生成 |

近几步 reward 偏低（step 862-865 连续 reward=0），prove_rate=0，entropy 很低（~0.02-0.03），有 collapse 迹象。预计约 17 分钟后完成 1000 步。

---
