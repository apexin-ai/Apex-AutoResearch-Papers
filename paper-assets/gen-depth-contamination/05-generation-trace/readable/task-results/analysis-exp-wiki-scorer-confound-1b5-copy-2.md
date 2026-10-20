# analysis exp wiki scorer confound 1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_scorer_confound_1b5_20260517T233956_result.json`
- **Structured JSON:** [`ed7ad26c737336ff9c28.json`](../../sessions/ed/ed7ad26c737336ff9c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验仍在运行中，尚未完成。

**当前状态：**
- 开始时间：07:22 CST (May 18, 2026)
- 当前时间：07:41 CST
- 当前进度：正在生成 depth 1 数据（301/313 batches, ~96%）
- 速率：~3.7s/batch

**预估剩余时间：**
- Depth 1 剩余：~45s
- Depth 2-5 生成：每层 ~19 min × 4 = ~76 min
- Scoring 阶段：~15-30 min
- **总计约 1.5-2 小时后完成**

**注意：** pipeline 检测到 symlink 的文件没有 model metadata，触发了重新生成所有 depth 数据（而非直接复用 exp_023_wiki 数据）。这意味着它在用 Qwen-1.5B 重新生成 depth 1-5，然后再用 Pythia-1.4B scorer 评分。

结果目录 `results/exp_wiki_scorer_confound_1b5/` 当前为空，需等实验完成后再读取。建议约 2 小时后再检查。

---
