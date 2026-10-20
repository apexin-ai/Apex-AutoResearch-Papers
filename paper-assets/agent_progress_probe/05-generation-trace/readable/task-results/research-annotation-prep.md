# research annotation prep

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_annotation-prep_20260514T111216_result.json`
- **Structured JSON:** [`f2ffc427e48b1959b00f.json`](../../sessions/f2/f2ffc427e48b1959b00f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三份文档已全部产出并注册：

1. **annotation_sampling_strategy.md** — 450 窗口分 6 层采样：核心标签×置信度 (300) + LF 分歧 (50) + Probe 高置信错误 (40) + 尾部 outcome (25) + OpenHands 跨 agent (20) + 短 trajectory (15)。刻意过采样 stagnation 到 ~44%。指出现有 `annotation_sample_450.csv` 缺少 probe 错误层和跨 agent 层，建议重新生成。

2. **annotation_guidelines.md** — 标注者完整指南：任务定义、progress/stagnation 判断标准、7 类边界情况裁定规则、3 级置信度说明、6 个真实数据标注示例（3 progress + 3 stagnation，含实际 agent 行为和判断理由）。

3. **annotation_interface.md** — 推荐 Google Sheets（快速启动）或 Label Studio（正式标注）；定义了展示格式（隐藏 majority_label 避免锚定偏差）、3 阶段流程（校准 15 窗口 → 主标注 450 窗口 × 3 人 → 裁决）、Fleiss κ 计算代码、标注者漂移检测方案、5/15-5/21 时间线。

---
