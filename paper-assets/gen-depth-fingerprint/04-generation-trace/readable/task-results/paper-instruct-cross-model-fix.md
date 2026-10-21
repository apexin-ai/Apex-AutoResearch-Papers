# paper instruct cross model fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_instruct-cross-model-fix_20260515T181700_result.json`
- **Structured JSON:** [`7c8c9c38952e5a0e18b3.json`](../../sessions/7c/7c8c9c38952e5a0e18b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个文件全部修改完成。变更摘要：

**discussion.tex** — instruct 段落重写：
- Entropy reversal 表述为跨三个 instruct 模型一致（partial ρ = +0.103/+0.161/+0.364），是 robust behavioral change
- Surface feature reversal 明确标注为 model-dependent：Qwen 保持正向（TTR +0.139/+0.130, hapax +0.125/+0.166），OLMo 保持与 base 同向的负值（TTR -0.241, hapax -0.198）
- 新增 OLMo paradox 段落：entropy 最强但 F1 最差，归因于 surface 与 entropy 极性矛盾导致分类器信号冲突

**limitations.tex** — instruct limitation 段落修正：
- 删除 "surface feature degradation is partially explained by length confounds" 的过度简化
- 改为 model-dependent 表述 + entropy reversal 一致性

artifacts/ 和 docs/paper/ 两处已同步。

---
