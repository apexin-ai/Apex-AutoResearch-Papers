# eval exp017 sft fast

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp017-sft-fast_20260514T162028_result.json`
- **Structured JSON:** [`579f458a008174b695c7.json`](../../sessions/57/579f458a008174b695c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp017 SFT Checkpoint 评估结果

| 指标 | 值 |
|------|-----|
| **success rate** | **5.0% (1/20)** |
| action_is_valid rate | 63.8% |
| format_ok rate | 75.0% |
| avg steps/episode | 22.0 |
| eval time | 126.3s (6.3s/episode) |
| total time | 149.6s |

**Per-task-type:**
| Type | Count | Success | Rate |
|------|-------|---------|------|
| put | 10 | 0 | 0% |
| clean | 4 | 0 | 0% |
| cool | 3 | 1 | 33.3% |
| heat | 2 | 0 | 0% |
| examine | 1 | 0 | 0% |

**分析：**
- success rate 5% (1/20)，低于 10% 门槛
- 唯一成功的是 1 个 cool 任务（EP 8，15 步完成）
- format 学得不错（75%），说明 SFT 学到了 `&lt;think>...&lt;answer>` 格式
- valid action rate 63.8% 说明模型大致知道该做什么动作，但常选到不在 admissible list 中的动作
- 有 5 个 episode（EP 7/12/16/17/18）只有 1 步就退出（parse 失败导致空 action）
- put 任务占一半但 0 成功——模型在多步导航+交互的 put 任务上最弱

**结论：** 5% < 10%，按判定标准直接上 GRPO 风险较高。建议分析失败 episode 的具体行为（是否在重复无效动作循环），考虑是否需要更多/更好的 SFT 数据，或者调整 GRPO 的 reward shaping 来补偿 SFT baseline 偏弱的问题。

---
