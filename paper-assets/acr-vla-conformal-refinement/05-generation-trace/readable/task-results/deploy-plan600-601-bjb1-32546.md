# deploy plan600 601 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_plan600-601-bjb1-32546_20260528T040144_result.json`
- **Structured JSON:** [`ce911f2a5959e941fb80.json`](../../sessions/ce/ce911f2a5959e941fb80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 和 cuda:4 上正在跑 `crm_perdof` 实验（已运行约 42 分钟）：
- cuda:3: `perdof_norm003_s44_v3`（max_correction_norm=0.03）
- cuda:4: `perdof_norm005_s44_v3`（max_correction_norm=0.05）

**这两张卡当前被占用，无法部署你要求的实验。**

可选方案：
1. **等这两个实验跑完**再提交（perdof 实验通常还需要一段时间）
2. **用 cuda:5**（空闲）先跑其中一个实验，另一个等卡空出来
3. **换到其他服务器**部署

需要哪个方案？

---
