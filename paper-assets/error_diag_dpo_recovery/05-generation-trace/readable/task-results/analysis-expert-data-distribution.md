# analysis expert data distribution

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_expert-data-distribution_20260512T162224_result.json`
- **Structured JSON:** [`3ead564e511d25a05d03.json`](../../sessions/3e/3ead564e511d25a05d03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已注册为 artifact `art_20260512_f992a4`。

**核心结论**：

- **3119 条 expert 数据**，6 种 task type 全覆盖，945 种 unique goals，108 个 scenes
- **分布不均**：pick 最多（759, 24.3%），examine 最少（279, 8.9%）
- **步数**：mean 9.8，74.3% 在 10 步内完成；puttwo 最长（mean 14.2），pick 最短（mean 7.3）
- **旧失败轨迹不可用**：仅 88 条，game_file 与 expert 零 overlap，且受 boundary 污染
- **DPO 建议**：重新收集失败轨迹时优先覆盖 puttwo（步数长、失败率高、DPO 收益最大）和 examine（expert 样本最少需确保覆盖），按同 game_file 配对为主

---
