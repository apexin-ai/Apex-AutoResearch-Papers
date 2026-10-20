# analysis carr fullft k4 probe 03

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_fullft_k4_probe_03_20260516T203628_result.json`
- **Structured JSON:** [`6b40cf76dadffb1fd1db.json`](../../sessions/6b/6b40cf76dadffb1fd1db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：carr_fullft_k4_probe_03

### 每代指标

| Gen | Quality | Vendi Score | Self-BLEU | Perplexity | NN Distance | Complexity |
|-----|---------|-------------|-----------|------------|-------------|------------|
| 0   | 0.1145  | 107.10      | 0.0038    | 9.10       | 0.7073      | 2.858      |
| 1   | 0.1141  | 107.61      | 0.0060    | 8.66       | 0.7091      | 2.853      |
| 2   | 0.1131  | 108.07      | 0.0044    | 9.21       | 0.7108      | 2.813      |

### P1 判定

- Vendi Score 变化：107.10 → 108.07 (**+0.91%**)
- 阈值：≤ -5%
- **P1 FAIL** — 无 collapse 发生

### 与 LoRA 实验对比

| 实验条件 | Vendi 变化 | Collapse? |
|----------|-----------|-----------|
| K=4 LoRA | -0.27% | No |
| K=8 LoRA | -0.03% | No |
| No-curation baseline | +3.13% | No |
| **K=4 Full-FT** | **+0.91%** | **No** |

### 结论

**假设被否定。** 移除 LoRA 约束改用 Full-FT（596M 全参数可训练）并未导致 collapse。K=4 选择压力在 3 代 × 2000 prompts 的设定下，无论 LoRA 还是 Full-FT，Vendi Score 都保持稳定甚至微升。

这意味着：
1. LoRA 不是阻止 collapse 的关键约束因素
2. K=4 的选择压力本身就不足以在短期内引发可观测的多样性下降
3. 如果要观测 collapse，可能需要更大 K（如 K=16+）、更多代数（>10 代）、或更极端的 curation 策略

---
