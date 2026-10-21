# analysis d154 8b exec s42 k4v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d154-8b-exec-s42-k4v2_20260520T092557_result.json`
- **Structured JSON:** [`66eb1fcab787c6ee32c9.json`](../../sessions/66/66eb1fcab787c6ee32c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/d154-8b-exec-s42-k4v2-analysis.md` 并注册。

**核心结论：NEGATIVE**

8B 和 4B 表现出完全不同的失败模式：

| | 4B (d146-pf-exec) | 8B (D154, this) |
|---|---|---|
| 最终 prove_rate | **1.0** | **0.155** |
| 是否收敛 | 是（reward→1.0） | 否（flat，极度 noisy） |
| 失败模式 | Goodhart collapse（reward↑ via hacking） | 训练停滞（reward 无提升） |

**根因**：K=4 对 8B 模型太小。大部分 step 中 4 个 sample 输出几乎相同（frac_reward_zero_std=1.0），GRPO 无对比梯度信号。模型 entropy 从 ~0.07 降到 ~0.04（mode collapse），但 collapse 到的分布不能解题。

Hypothesis "8B 也出现 Goodhart collapse" **未被验证**。这更可能是 config 问题（K 太低）而非 model-size 效应。建议 K=8/16 或更高 LR 重跑以区分。

---
