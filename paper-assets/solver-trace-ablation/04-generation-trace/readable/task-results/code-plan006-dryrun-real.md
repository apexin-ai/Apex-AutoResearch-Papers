# code plan006 dryrun real

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-dryrun-real_20260514T083440_result.json`
- **Structured JSON:** [`0916cd3941d7d319b43b.json`](../../sessions/09/0916cd3941d7d319b43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

**3 步全部成功完成，无 crash/OOM。**

### 各步指标

| Step | prove_rate | parse_rate | ISR | reward | loss | step_time (s) |
|------|-----------|------------|-----|--------|------|---------------|
| 1 | 0.000 | 1.000 | 0.000 | 0.0000 | 0.0 | 6.10 |
| 2 | 0.000 | 1.000 | 0.000 | 0.0000 | 0.0 | 8.44 |
| 3 | 0.250 | 1.000 | 0.050 | 0.2500 | 0.0216 | 14.01 |

### 关键数据

1. **初始 prove_rate**: 前两步为 0，第 3 步跳到 0.25 — 初始 PR 极低，建议 **K=16**
2. **parse_rate**: 全程 1.000（完美）
3. **每步耗时**: 6~14 秒，总训练时间 53 秒
4. **第 3 步出现学习信号**: loss=0.0216, grad_norm=4.52, 说明 reward 有方差后梯度开始流动

---
