# ops cellc v3 progress check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cellc-v3-progress-check_20260521T023645_result.json`
- **Structured JSON:** [`98788c60617b830cccf6.json`](../../sessions/98/98788c60617b830cccf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Cell C v3 状态

| 指标 | 值 |
|------|-----|
| **进程** | PID 88226，运行中，已运行 8h13m |
| **当前步数** | **3/15 (20%)** |
| **每步耗时** | step 1: 39m, step 2: 3h46m, step 3: 2h11m（平均 ~2h20m/step，step 1 是 warmup） |
| **预估剩余** | ~28h（进度条显示 28:08:26） |
| **预估完成** | 约 5月22日 下午 |

### Val 结果

仅有 **step 0**（baseline）的 val：
- success: **0.0**
- score: **2.71**
- pass@1: **0.0**
- reward/mean@32: **0.5**
- final_score: **5.0**

**Step 5 val 尚未产生**，当前才到 step 3。

### Train 指标（step 3）

- train success: 0.0，train score: 0.96
- reward mean: 0.153，KL loss: 0.613
- manager_invalid_action: **67.6%**（大量无效动作）
- action_is_valid: 9.4%
- throughput: 90.5 tokens/s

训练信号偏弱（success 仍为 0，reward 低），需关注后续 step 5 val 是否出现改善。

---
