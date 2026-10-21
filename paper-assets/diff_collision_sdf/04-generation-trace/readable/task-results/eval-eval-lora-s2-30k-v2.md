# eval eval lora s2 30k v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_eval_lora_s2_30k_v2_20260527T135937_result.json`
- **Structured JSON:** [`60c0eea67738ea3dde96.json`](../../sessions/60/60c0eea67738ea3dde96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现 GPU 冲突**：旧作业 `eval_lora_baseline_30k_s2` (PID 512147) 已在 cuda:0 上运行相同 eval，已完成 10/50 episodes。新提交的 `eval_lora_s2_30k_v2` 刚开始加载模型，两者在同一 GPU 上会互相干扰。

两个作业参数完全一致（同 checkpoint、同 config、同 seed 7、同 50 episodes）。

**建议**：kill 新作业 `eval_lora_s2_30k_v2`，让已经跑到 10/50 的旧作业继续完成。需要 kill 新作业吗？还是你希望反过来 kill 旧作业？

---
