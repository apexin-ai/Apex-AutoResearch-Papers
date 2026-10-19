# research prepare ci fallback narrative

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prepare-ci-fallback-narrative_20260516T075032_result.json`
- **Structured JSON:** [`87f3699fce3aba3adf27.json`](../../sessions/87/87f3699fce3aba3adf27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出在 `artifacts/fallback_narrative_draft.md`，包含：

1. **Claim 重构** — 从 "significantly improves" 转为 "consistent directional improvement with structured magnitude sensitivity"
2. **Evidence stack** — 四层证据不依赖 p<0.05：inverted-U magnitude curve（机制证据）、跨 seed 方向一致性、Cohen's h + bootstrap CI、per-task 分层分析
3. **论文各章节调整方案** — abstract/intro/results 的具体措辞修改 + 图表重排（magnitude curve 提为 lead figure）
4. **Reviewer 对话** — 预写 limitations 段落 + 三个预期质疑的回应模板
5. **Decision framework** — 根据 3-seed 结果的 5 种场景选择对应策略

核心策略：用 magnitude curve 的 inverted-U 形状作为不可伪造的机制证据（随机噪声无法产生单峰响应），将 pooled SR difference 降级为 evidence stack 中的一个元素而非唯一判据。

---
