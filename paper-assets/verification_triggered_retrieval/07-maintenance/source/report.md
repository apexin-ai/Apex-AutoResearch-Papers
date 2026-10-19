# Handover — 2026-05-17

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **mvp_002** (negative): mvp_001 在小 corpus (~2000 passages) 上无差异是因为 entity matching 主导导致两种 query 返回相同文档（无 discriminative power）。在 full Wikipedia (~5M passages) 上，verification queries 应检索到更高 entailment 的 evidence（top-5 overlap rate < 60% 且 entailment diff > 0），因为大 corpus 中 query formulation 对 ranking 的影响不再被高覆盖率掩盖。 ← 基于 mvp_001
- **mvp_001** (negative): NLI-style verification queries (claim-as-query) retrieve evidence with significantly higher entailment scores than standard answer-seeking queries (>5pp difference, p<0.05), because assertion-form queries better match the declarative structure of supporting passages in Wikipedia.

## 趋势
成功 0 / 负向 2 / 失败 0 / 共 2

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-46807: 无 GPU 信息

## 告警
（无）
