# check adaptive fix fresh progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_adaptive_fix_fresh_progress_20260514T173116_result.json`
- **Structured JSON:** [`2986972c9e0c535b9d38.json`](../../sessions/29/2986972c9e0c535b9d38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## adaptive_fix 状态

**重要纠正**：之前报的 8477 是 eval 数据集的 batch 数（eval 进度条），**实际训练总步数是 6103**（200M tokens / (4×4×2048)）。三组全部仍在训练中。

| exp_id | 状态 | training step | 最新 eval_loss (step) | eval_ppl_holdout | 训练ETA | 预估总ETA |
|--------|------|--------------|----------------------|-----------------|---------|----------|
| adaptive_fix_seed42 | 训练中 | 1789/6103 (29%) | 3.0869 (step 1500) | **21.91** | ~2h44m | ~9h20m |
| adaptive_fix_seed123 | eval中 | ~1554/6103 (25%) | 3.1045 (step 1000) | **22.30** | ~2h51m | ~9h27m |
| adaptive_fix_seed456 | 训练中 | 1304/6103 (21%) | 3.1047 (step 1000) | **22.31** | ~2h59m | ~10h19m |

**关键数据**：
- eval_ppl_holdout 计算：`exp(eval_loss)`
- 三组在相同 step 的 PPL 非常接近（seed123 和 seed456 在 step 1000 几乎一致），说明可重复性好
- seed123 正在运行 step 1500 的 eval（8327/8477，~46s 完成），完成后会有新的 eval_loss

**总 ETA 很长的原因**：每 500 步触发一次 eval，每次 eval 遍历 8477 个 batch 需要 ~44 分钟。剩余 9-10 次 eval 贡献了 ~6.5-7.3h 的纯 eval 时间。

---
