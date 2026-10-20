# paper sampling ablation appendix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_sampling-ablation-appendix_20260515T203008_result.json`
- **Structured JSON:** [`472e6fc6feb19dd40b4d.json`](../../sessions/47/472e6fc6feb19dd40b4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三处修改，两份副本已同步：

1. **appendix_classifier.tex** — 末尾新增 `Sampling Sensitivity Analysis` 段落，含 3 行 table 和 ~130 words 分析（low/default 差异 <0.3pp，high temp 退化 ~6pp，entropy 相关性从 -0.69 塌缩到 ~0，解释为高温随机性压平深度漂移信号）

2. **discussion.tex** — "Why are shape features stationary?" 段落末尾（hypothesis flag 前）插入一句 sampling ablation 总结，引用 appendix

3. **limitations.tex** — 原来的 "fixed decoding parameters...open question" 句子替换为引用 ablation 结果的定量描述，将 open question 转为已有初步答案

---
