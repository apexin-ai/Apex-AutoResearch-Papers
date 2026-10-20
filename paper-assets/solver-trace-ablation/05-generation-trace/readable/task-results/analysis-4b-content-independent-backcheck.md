# analysis 4b content independent backcheck

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-content-independent-backcheck_20260518T001553_result.json`
- **Structured JSON:** [`e11cd960d2ca6ed9cf3c.json`](../../sessions/e1/e11cd960d2ca6ed9cf3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**4B genuine 数据无 content_independent 高估问题。**

核心发现：
- 三个 genuine>0 的 seed（s42/s45/s46），genuine 样本中 content_independent = **0**
- 4B 模型使用内容相关谓词（Lawyer, Chef, Defender），不像 1.7B 抽象为单字母（P, Q, R）
- genuine 样本展示真实多步推理链（如 Centerback→Defender→Player→¬BasketballPlayer）
- s42 整体 CI=19，但全部落在 H7/H1/H8 分类中，不在 genuine 中
- pooled genuine mean 15.8% 无需修正

报告已注册：`d130_4b_content_independent_backcheck`

---
