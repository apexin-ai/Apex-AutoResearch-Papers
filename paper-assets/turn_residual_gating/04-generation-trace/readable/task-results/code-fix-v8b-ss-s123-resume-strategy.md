# code fix v8b ss s123 resume strategy

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_v8b_ss_s123_resume_strategy_20260520T202838_result.json`
- **Structured JSON:** [`7a1283a0c4f82589f401.json`](../../sessions/7a/7a1283a0c4f82589f401.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the finding:

## SS Ratio 调度逻辑

```python
# line 348-350
effective_step = max(0, global_step - ss_warmup_steps)  # ss_warmup_steps default=0
effective_total = max(1, total_steps - ss_warmup_steps)
ss_ratio = min(effective_step / effective_total, ss_max_ratio)
```

- `total_steps = len(dataloader) * epochs // grad_accum = 8000 * 3 // 8 = 3000`
- SS ratio 是**按 global_step 全局线性**增长，不是按 epoch

## s42 实际行为

s42 的 Phase A 命令包含 `--scheduled-sampling --ss-max-ratio 0.5`，所以 **epoch 0 并非"无 SS"**，而是 SS ratio 从 0 线性涨到 0.333。

s42 train_config.json 确认：`total_steps=3000, ss_warmup_steps=0, ss_used_count=7668/16000 (47.9%)`。

## Resume 逻辑（line 297-302）

```python
if args.resume and start_epoch > 0:
    global_step = steps_per_epoch * start_epoch  # = 1000
    for _ in range(global_step):
        scheduler.step()  # LR fast-forward
```

关键点：
- **global_step 从 1000 开始** → SS ratio 从 0.333 继续，与连续训练一致
- **LR scheduler 被 fast-forward** → LR 正确
- **optimizer state NOT restored** → momentum/adaptive state 丢失（唯一差异）

## 等价性分析

| 维度 | s42 两阶段 | s123 连续 3 epoch |
|------|-----------|-------------------|
| SS ratio 轨迹 | 0→0.333 (ep0) → 0.333→0.5 (ep1-2) | 0→0.5 (ep0-2) |
| global_step 映射 | 0→3000 | 0→3000 |
| 任意 step 的 SS ratio | min(step/3000, 0.5) | min(step/3000, 0.5) |
| LR schedule | ✓ 一致（fast-forward） | ✓ 一致 |
| **Optimizer state** | **ep1 开始时重置（OOM 事故）** | **连续** |

**SS ratio 轨迹完全相同。** 唯一差异是 s42 的 optimizer state 在 epoch boundary 被意外重置（因 OOM crash，非设计意图）。s123 连续运行反而是更 principled 的做法。

## 结论

**现有 `launch_v8b_ss_s123.sh` 已经正确，无需修改。** s42 的"两阶段"是 OOM 事故导致，不是刻意设计。

需要在脚本里加注释说明吗？

---
