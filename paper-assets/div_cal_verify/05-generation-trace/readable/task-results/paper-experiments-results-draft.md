# paper experiments results draft

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments_results_draft_20260513T213345_result.json`
- **Structured JSON:** [`acb5cbb07cd89ccf9e75.json`](../../sessions/ac/acb5cbb07cd89ccf9e75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入：

- `docs/paper/experiments.tex` — 实验配置、训练超参、选择算法（eigenvalue variance minimization + PCA 32d）、5 项评估指标、GPT2-Medium scaling TODO
- `docs/paper/results.tex` — C1（RGDS PPL 78.32±4.60, +82% vs random）、C2（External 47.59±2.93, ratio >1.0）、C3（RGDS vs Random 控制消融）、S3（Random vs Uncurated p≈0.10 方向性观察）、lexical diversity 趋势、RankMe 失效

`main.tex` 已更新，`\input{experiments}` 和 `\input{results}` 已取消注释。

注意事项：
- methodology.tex 中 grad_accum=8（effective 32），experiments.tex 按指定写的 grad_accum=4（effective 16），需要统一
- External/RGDS 标注了 $n{=}2$†，TODO 标注了 seed=456 更新位置和 GPT2-medium 占位

---
