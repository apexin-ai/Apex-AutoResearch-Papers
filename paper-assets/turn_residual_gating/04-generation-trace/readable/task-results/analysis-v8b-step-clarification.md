# analysis v8b step clarification

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_step_clarification_20260521T130409_result.json`
- **Structured JSON:** [`d117efee17d5a3fe646d.json`](../../sessions/d1/d117efee17d5a3fe646d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**日志中的 Step = microstep（dataloader 迭代），每个 epoch 重置。**

代码证据：
- L326: `for step, batch in enumerate(dataloader):` — `step` 是 enumerate 索引
- L544: 打印的是 `Step {step}`（microstep），不是 `global_step`（optimizer step）
- L525: `global_step += 1` 在 grad accumulation 完成后才递增
- L271: `total_steps = len(dataloader) * epochs // grad_accum` = 8000×3//8 = 3000（scheduler 用的 optimizer steps）

**计数：**

| 指标 | 值 |
|------|-----|
| 日志 Step | microstep（per-epoch，0-7999） |
| 总 microsteps | 24,000（8000 × 3 epochs） |
| 总 optimizer steps | 3,000（24000 / 8 grad_accum） |
| 已完成 microsteps | 19,700（8000+8000+3700） |
| 当前 optimizer step | ~2,462（19700 / 8） |
| 进度 | 82.1% |

**ETA：**
- 开始：12:28，最后日志 21:05（历时 ~8h37m）
- 速率：~38 microsteps/min
- 剩余：4,300 microsteps ≈ **1h53min**
- 预计完成：**~22:58 (+0800)**

---
