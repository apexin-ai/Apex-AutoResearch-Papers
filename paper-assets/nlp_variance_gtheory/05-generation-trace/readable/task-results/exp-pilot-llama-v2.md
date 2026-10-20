# exp pilot llama v2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pilot_llama_v2_20260520T233718_result.json`
- **Structured JSON:** [`5c5bfa321d1a227af2e9.json`](../../sessions/5c/5c5bfa321d1a227af2e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部在跑，GPU 分配正确（每卡 ~89GB 独立显存）。10 分钟后轮询进度。

当前状态：
- GPU 0: 领先（已产出 1600+ records，~8/25 conditions）
- GPU 1/2/3: 刚完成模型加载，开始推理第一个 condition
- 预计总耗时：~15-20 分钟（GPU 1/2/3 落后 GPU 0 约 5 分钟）

---
