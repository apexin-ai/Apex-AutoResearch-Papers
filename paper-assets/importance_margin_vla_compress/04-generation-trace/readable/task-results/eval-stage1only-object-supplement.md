# eval stage1only object supplement

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_stage1only_object_supplement_20260517T132153_result.json`
- **Structured JSON:** [`983087fff4874c172d68.json`](../../sessions/98/983087fff4874c172d68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已经很清楚了：

**eval 已完成，无需补跑。** `eval_stage1only_object_v2_fixed.json` 已包含全部 10 个 tasks (0-9)，每个 50 episodes，共 500 episodes。

### 汇报

| Task | Description | SR |
|------|------------|-----|
| 0 | pick up the alphabet soup | 0/50 = 0% |
| 1 | pick up the cream cheese | 0/50 = 0% |
| 2 | pick up the salad dressing | 0/50 = 0% |
| 3 | pick up the bbq sauce | 0/50 = 0% |
| 4 | pick up the ketchup | 0/50 = 0% |
| 5 | pick up the tomato sauce | 0/50 = 0% |
| 6 | pick up the butter | 0/50 = 0% |
| 7 | pick up the milk | 0/50 = 0% |
| 8 | pick up the chocolate pudding | 0/50 = 0% |
| 9 | pick up the orange juice | 0/50 = 0% |

**Overall: 0/500, Wilson CI 95% [0, 0.76%]**

注意：结果文件记录的 checkpoint 是 `libero_imm_twostage_fullft`（不是 `acis_stage1only_k05`，后者不存在）。如果这不是预期的 checkpoint，需要确认。

---
