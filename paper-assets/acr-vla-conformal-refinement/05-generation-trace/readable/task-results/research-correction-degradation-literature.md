# research correction degradation literature

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_correction-degradation-literature_20260514T072644_result.json`
- **Structured JSON:** [`e75f1f173f12bd797593.json`](../../sessions/e7/e75f1f173f12bd797593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入并注册 `art_20260514_d21dd2`。核心结论：

**退化最可能的原因**（按优先级）：
1. **Distribution shift 导致 CP 保证失效** — LIBERO spatial eval 分布偏离 CRM 训练分布，失效的 CP 给出错误 uncertainty signal，CRM 向错误方向修正
2. **Correction magnitude 无界** — 无显式约束的修正幅度在 uncertainty 不准时 overshoot
3. **Cascading error** — 单步过修正在 action sequence 时间维度上累积
4. **好样本被破坏** — SampleConsensus 42.9% 说明 VLA 已能生成好样本，CRM 对所有样本统一修正反而将好样本推离最优

**最值得优先尝试的补救**：
- **Correction magnitude clipping**（clip CRM 输出 L2 norm）— 零成本，直接测
- **Confidence-gated correction**（仅高 uncertainty 时修正）— 保护好样本
- **Hybrid: SampleConsensus top-K → bounded correction** — 结合 selection 的稳定性和 correction 的精度
- **借鉴 GDP 的 population-based selection** — 在生成过程中即做 OoD-aware filtering，NeurIPS 2025 报告 14 任务平均 +20%

---
