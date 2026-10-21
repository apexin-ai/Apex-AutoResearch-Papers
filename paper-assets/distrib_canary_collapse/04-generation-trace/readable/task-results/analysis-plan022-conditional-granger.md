# analysis plan022 conditional granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan022_conditional_granger_20260524T032050_result.json`
- **Structured JSON:** [`9b38db5884eefe88fb4a.json`](../../sessions/9b/9b38db5884eefe88fb4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已保存。汇报如下：

## Conditional Granger 分析结果 (lag=1)

| α | Seed | Test | Uncond p | Cond p | Survives? |
|---|------|------|----------|--------|-----------|
| 0.50 | s42 | ent→d1 | <0.001 | 0.135 | NO |
| 0.50 | s42 | ent→d2 | <0.001 | 0.056 | MARGINAL |
| 0.50 | s42 | ent→d3 | <0.001 | 0.852 | NO |
| 0.50 | s42 | ece→d1 | <0.001 | 0.307 | NO |
| 0.50 | s42 | ece→d2 | <0.001 | 0.339 | NO |
| 0.50 | s42 | ece→d3 | <0.001 | 0.332 | NO |
| 0.50 | s43 | ent→d1 | <0.001 | 0.458 | NO |
| 0.50 | s43 | ent→d2 | <0.001 | **0.010** | YES |
| 0.50 | s43 | ent→d3 | <0.001 | 0.657 | NO |
| 0.50 | s43 | ece→d1 | <0.001 | **0.020** | YES |
| 0.50 | s43 | ece→d2 | <0.001 | 0.173 | NO |
| 0.50 | s43 | ece→d3 | <0.001 | 0.332 | NO |
| 0.75 | s42 | ent→d1 | <0.001 | 0.221 | NO |
| 0.75 | s42 | ent→d2 | <0.001 | 0.055 | MARGINAL |
| 0.75 | s42 | ent→d3 | <0.001 | 0.080 | MARGINAL |
| 0.75 | s42 | ece→d1 | <0.001 | **<0.001** | YES |
| 0.75 | s42 | ece→d2 | <0.001 | **<0.001** | YES |
| 0.75 | s42 | ece→d3 | <0.001 | **0.001** | YES |
| 0.75 | s43 | ent→d1 | <0.001 | 0.132 | NO |
| 0.75 | s43 | ent→d2 | <0.001 | 0.656 | NO |
| 0.75 | s43 | ent→d3 | <0.001 | 0.306 | NO |
| 0.75 | s43 | ece→d1 | <0.001 | **<0.001** | YES |
| 0.75 | s43 | ece→d2 | <0.001 | 0.054 | MARGINAL |
| 0.75 | s43 | ece→d3 | <0.001 | 0.260 | NO |

## 聚合统计 (lag=1, p<.05)

| | Unconditional | Conditional | Survival rate |
|---|---|---|---|
| **Entropy→diversity** | 12/12 | **1/12** | 8% |
| **ECE→diversity** | 12/12 | **5/12** | 42% |

## 关键发现

1. **Entropy 的因果信号几乎完全被 ECE 吸收**：控制 ECE 后，entropy→diversity 从 12/12 降至 1/12 显著。Entropy 的预测力基本是和 ECE 共线性带来的。

2. **ECE 保留独立因果通道**：控制 entropy 后，ECE→diversity 仍有 5/12 显著，且集中在 α=0.75（4/6 survive vs α=0.50 仅 1/6）。ECE 携带 entropy 之外的独有预测信息。

3. **α 依赖模式**：高污染率下 ECE 成为主导独立因果通道；onset 附近两个 canary 信号更共线，条件检验后都减弱。

4. **两 canary 非因果链关系**：Entropy 在 3/4 条件下不 Granger-cause ECE（unconditional 就不显著），说明它们是共变而非一个驱动另一个。

**对审稿人 confounding 质疑的回应**：两个 canary 捕捉部分不同的信息，ECE 是通向 diversity collapse 的主要独立因果通路。Entropy 的作用更多是 correlated indicator 而非 independent cause。

---
