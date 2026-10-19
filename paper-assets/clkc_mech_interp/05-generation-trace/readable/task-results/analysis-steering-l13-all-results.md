# analysis steering L13 all results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_steering-L13-all-results_20260522T151732_result.json`
- **Structured JSON:** [`9252e68f98e19350b26a.json`](../../sessions/92/9252e68f98e19350b26a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## Llama L13 All-Position Steering 结果

| Alpha | Steer Flips | Control Flips | p→c | c→p | Fisher p | Sig? |
|-------|------------|--------------|-----|-----|----------|------|
| **-20** | 49 (36.0%) | 24 (17.6%) | 1 | 5 | **0.0009** | **YES** |
| -10 | 31 (22.8%) | 25 (18.4%) | 2 | 1 | 0.4536 | No |
| -5 | 22 (16.2%) | 17 (12.5%) | 2 | 1 | 0.4893 | No |
| **+5** | 27 (19.9%) | 9 (6.6%) | 4 | 0 | **0.0020** | **YES** |
| +10 | 31 (22.8%) | 20 (14.7%) | 2 | 0 | 0.1197 | No |
| +20 | 28 (20.6%) | 43 (31.6%) | 2 | 2 | 0.0528 | Marginal |

### 关键发现

**All-position 与 last-token 结果完全一致**——每个 alpha 的 flip counts 和 Fisher p 数值完全相同。这意味着：
1. L13 的因果信号**完全集中在 last token position**
2. 对 non-last tokens 施加 steering 零额外效应
3. 排除了冲突信号在 token positions 间分布式编码的假设

### Gemma L17 状态

- 进程 493756 仍在运行（已 38 分钟），结果文件尚未生成
- GPU 2: 18.6GB 显存占用，13% 利用率

---
