# ops fill cuda0 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_cuda0_35807_20260527T035357_result.json`
- **Structured JSON:** [`f6c297e20a7b35bf5483.json`](../../sessions/f6/f6c297e20a7b35bf5483.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

- **选择任务**：Priority 2 — λ=0.1 s0 24K step-wise eval（Priority 1 的 spatial_bowl SDF eval 之前已跑完，DONE/negative）
- **原因**：s0 step-wise curve 已有 16K→20K→22K 三个点，24K 是最新可用的中间 checkpoint，延续 learning curve
- **已提交**：`eval_stepwise_s0_l1_24k` → westd-35807 cuda:0，PID 575130，状态 RUNNING
- **预计完成**：eval 200 episodes 约 1.5-2 小时
- **关注点**：22K 时 CAR 跳到 60.5（前两个点 55-55.5），看 24K 能否保持上升趋势

---
