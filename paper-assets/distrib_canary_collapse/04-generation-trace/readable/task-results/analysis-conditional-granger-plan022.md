# analysis conditional granger plan022

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conditional_granger_plan022_20260521T021117_result.json`
- **Structured JSON:** [`0f7a877fb0617d3b0993.json`](../../sessions/0f/0f7a877fb0617d3b0993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Token_entropy 和 ECE 是同一机制的两个冗余表现，不是独立通道。ECE 是主通道。**

关键数据：
- 两者高度反相关（r = −0.84 to −0.98）
- Unconditional Granger 显著率 79% → conditional 后分别降至 35%（entropy）和 48%（ECE）
- 33% 的 pair 属于纯冗余（unconditional 显著但 conditional 两者都不显著）
- Partial R²：ECE 在 73% 的比较中胜出（mean pR² 0.448 vs 0.346）
- 大模型（pythia-1b, smollm-3b）在 diversity metrics 上表现出更多"双独立"模式

**论文建议**：canary 信号来自单一的 calibration collapse 机制，ECE 是更直接的度量。这强化了 phase transition 的单机制解释。

报告在 `artifacts/conditional_granger_analysis.md`，完整 JSON 在服务器 `results/analysis/conditional_granger_v2.json`。

---
