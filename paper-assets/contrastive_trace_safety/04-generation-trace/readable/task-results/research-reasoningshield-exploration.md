# research reasoningshield exploration

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reasoningshield_exploration_20260519T184024_result.json`
- **Structured JSON:** [`4f71804bf40a18e7bde6.json`](../../sessions/4f/4f71804bf40a18e7bde6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探索完成。核心发现：

**数据集概况**: 9,200 条，3 个 config（SFT 4358 / DPO 2642 / Test 2200），8 个 LRM 模型。

**CP 兼容性: 中等**
- **无 step-level 安全标注** — 只有 trace-level 3-tier 标签（safe 0.0 / borderline 0.5 / unsafe 1.0）
- 需自行切分 + 逐句打分来定位 CP
- 281 条 refusal→comply traces + 334 条 borderline traces = **615 条可用于 CP 分析**，超过 100 条目标
- **r1-8b 存在**（Test 360 条，SFT 862 条），直接对应我们的实验模型

**主要限制**: model_thinking 是纯文本（无 `&lt;think>` 标签），median 仅 692 tokens，CP 需要外部 safety classifier 辅助定位。

**转换代码量**: ~120–200 行。

报告已写入 `artifacts/reasoningshield_exploration.md`，探索脚本在服务器 `src/reasoningshield_explore.py`。

---
