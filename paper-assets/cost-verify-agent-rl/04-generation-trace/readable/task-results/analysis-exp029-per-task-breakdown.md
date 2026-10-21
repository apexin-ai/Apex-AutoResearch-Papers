# analysis exp029 per task breakdown

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp029_per_task_breakdown_20260519T140819_result.json`
- **Structured JSON:** [`a5e539ac7dcfae7b4673.json`](../../sessions/a5/a5e539ac7dcfae7b4673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp029_per_task_breakdown_analysis.md`。

核心发现：

1. **T=0.0 整体 16.4% (22/134)**，比 T=0.4 的 23.88% 低 7.5pp — greedy 解码更差，模型需要采样多样性来逃脱 action 循环。

2. **两个明显梯队**：look_at_obj (27.8%) / pick_clean (25.8%) / pick_and_place (20.8%) vs pick_cool (9.5%) / pick_two_obj (5.9%) / pick_heat (4.3%)。

3. **Information loss hypothesis 部分成立但需修正**：不是简单的"步骤越多越差"。`pick_clean` 是 2-step 任务却表现优于 1-step 的 `pick_and_place`。真正的瓶颈是**特定电器交互的泛化能力** — 微波炉/冰箱的 OOD 泛化远差于水槽。

4. **二元行为模式**：成功 episode 极快（8-15 步），失败 episode 全部撞到 50 步上限，没有中间状态。

5. `pick_cool` 的 valid action rate 很高 (0.729) 但 success rate 低 (9.5%)，说明是**规划失败**而非动作空间理解失败 — 模型能生成合法冰箱操作但无法完成完整序列。

---
