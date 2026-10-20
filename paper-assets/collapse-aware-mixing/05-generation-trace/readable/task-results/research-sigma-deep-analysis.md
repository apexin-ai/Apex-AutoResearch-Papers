# research sigma deep analysis

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sigma-deep-analysis_20260512T172849_result.json`
- **Structured JSON:** [`92767ff4c6998181801e.json`](../../sessions/92/92767ff4c6998181801e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/sigma_deep_analysis.md`。核心发现：

**SIGMA 与我们的 4 个关键差异：**

1. **谱指标不同**：SIGMA 用 log-determinant（`Σ log λⱼ`），我们用 spectral effective rank（`exp(H(σ))`）。后者有界 [1,m]，更适合作为控制器输入。

2. **纯监控 vs 闭环控制**：SIGMA 无任何干预/控制机制，未来工作方向是 Koopman operator 预测（仍是被动）。我们有 PI 控制器做实时 real/synthetic 比例调节。

3. **未验证 leading indicator**：SIGMA 未做谱指标与 PPL 的时序对比，自承"measures collapse states but does not predict failure"。这是我们的核心假设验证。

4. **实验设置差异大**：OPT-125M + 64K tokens + 外部 sentence encoder vs 我们的 Pythia-1B + wikitext-103 + 模型自身 hidden states。

**Positioning 一句话**：SIGMA 证明了"谱分析能检测 collapse"；我们回答"检测到之后怎么办"——从 passive monitoring 到 active closed-loop control。

Sources:
- [SIGMA: Scalable Spectral Insights for LLM Model Collapse](https://arxiv.org/abs/2601.03385)
- [SIGMA HTML full text](https://arxiv.org/html/2601.03385)

---
