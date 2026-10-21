# analysis exp010 reward shaping

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp010-reward-shaping_20260514T052920_result.json`
- **Structured JSON:** [`19f0f72186b7f5b7a8ee.json`](../../sessions/19/19f0f72186b7f5b7a8ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入并注册。

**根因**: Format penalty (-0.1/turn) 在零成功 group 中成为 GRPO advantage 的唯一信号源。Step 1 时 62.5% 的 group 没有任何成功轨迹，这些 group 的梯度全部指向"减少格式错误"而非"完成任务"。随着 success 降至 0%（Step 2-3），100% 的 group 都只有 format penalty 信号，模型完全转向学习生成合法但无效的动作。

**关键数据**:
- Step 1→10: action_is_valid 58.8%→68.3%（在学），success 4.7%→0%（在退化）
- 零成功步（2-3, 8-10）的 score_max = 0.0，全部 reward 为负值，GRPO advantage 完全由 format penalty 差异驱动

**建议**:
1. **必做**: 用 AlfWorld 的连续 score 替代纯 won-based 稀疏奖励 + 把 format_penalty 从 -0.1 降到 -0.01 或 0
2. **强烈建议**: group_size 从 8 增到 16+
3. 从 step 5 checkpoint 恢复（success 尚未归零）

---
