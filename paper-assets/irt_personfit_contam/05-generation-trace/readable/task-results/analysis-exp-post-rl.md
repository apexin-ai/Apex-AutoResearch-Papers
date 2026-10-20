# analysis exp post rl

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-post-rl_20260521T050508_result.json`
- **Structured JSON:** [`6083a45602d03f850257.json`](../../sessions/60/6083a45602d03f850257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

**GRPO 训练进行中** — 688/7021 steps (~10%), ETA ~3h20m（12:43 启动，预计约 16:05 完成）

**已完成**：
- 修复了 eval_lz.py 的 bug：`--stage grpo` 原来直接在 base model 上加 GRPO adapter（错误），改为 base → merge SFT adapter → apply GRPO adapter，与训练时的模型构建方式一致

**待训练完成后执行**：
1. 运行 `python eval_lz.py --stage grpo --gpu 0`（使用 CUDA_VISIBLE_DEVICES=2 映射的 gpu 0）
2. 计算对比指标：Δlz*, Cohen's d, signal retention ratio
3. 保存结果到 `results/post_rl_results.json`

需要我设置定时轮询训练进度，还是你稍后手动触发继续？

---
