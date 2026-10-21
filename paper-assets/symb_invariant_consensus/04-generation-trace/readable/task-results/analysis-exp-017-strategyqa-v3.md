# analysis exp 017 strategyqa v3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-017-strategyqa-v3_20260517T042717_result.json`
- **Structured JSON:** [`65b2d1390f77d5648ba5.json`](../../sessions/65/65b2d1390f77d5648ba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新，conclusion = **success**。

**核心结论**: SICA 56.67% vs SC 53.33%，+3.33pp 但不显著 (McNemar p>0.05, bootstrap p=0.13)。与 parent 实验一致，支持 capability trap 跨域（数学→常识推理）泛化假说。

关键发现:
- v3 修复确认成功：问题级提取率 100%（v2 仅 26.7%）
- 仅 2 个 discordant pairs，均 SICA 胜出（SICA 通过约束推翻了 SC 多数票的错误答案）
- 整体准确率偏低（~57% on Yes/No），模型在 StrategyQA 上表现不佳
- unique constraints 极少（平均 1.0），Yes/No 任务约束多样性不足

---
