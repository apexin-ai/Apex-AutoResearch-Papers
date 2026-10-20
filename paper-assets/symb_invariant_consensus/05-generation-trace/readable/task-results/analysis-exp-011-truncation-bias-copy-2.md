# analysis exp 011 truncation bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-011-truncation-bias_20260517T081040_result.json`
- **Structured JSON:** [`1e15f2cf04d64a47fc03.json`](../../sessions/1e/1e15f2cf04d64a47fc03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-011 截断偏差分析报告

### 截断分布
- 44 条 truncated traces 分布在 16/60 个问题上（73% 的问题无截断）
- 截断集中在 ProofWriter（39/44），FOLIO 几乎无截断（5/44）
- 平均每题 0.73 条截断，中位数 0

### 核心发现：截断不偏向 SICA

**Discordant pairs 截断情况：**

| 类型 | n | 有截断的问题数 | 平均截断数 |
|------|---|---------------|-----------|
| SICA wins | 5 | 1 (仅 RelNeg-856_Q19, 3/12) | 0.60 |
| SC wins | 1 | 0 | 0.00 |

5 个 SICA-wins discordant pair 中，4 个完全无截断，只有 1 个有 3 条截断。

**统计检验（全部不显著）：**

| 检验 | 结果 |
|------|------|
| Fisher exact (discordant pairs: 截断 vs SICA胜) | p=1.000 |
| Mann-Whitney U (SICA-wins vs 其他的截断量) | p=0.615，方向相反（SICA-wins 截断更少） |
| Spearman ρ (截断率 vs SICA优势) | ρ=-0.002, p=0.987 |

**Median split：**
- 有截断组 (n=16): SICA-SC = +6.2pp
- 无截断组 (n=44): SICA-SC = +6.8pp
- 两组 SICA 增益几乎相同，无截断组反而略高

### 结论

**截断不构成系统性偏差。** SICA 的 +6.67pp 增益在有/无截断的问题子集上均一致存在（+6.2pp vs +6.8pp）。SICA 胜出的 5 个 discordant pair 中 4 个无截断，且 SICA-wins 组的平均截断量（0.60）低于全局均值（0.75）。所有统计检验均不显著。

对 exp-019 设计的启示：增加 max_tokens 是好的工程实践（减少信息丢失），但截断不是当前增益的驱动因素，不需要因此质疑 +6.67pp 的可信度。

---
