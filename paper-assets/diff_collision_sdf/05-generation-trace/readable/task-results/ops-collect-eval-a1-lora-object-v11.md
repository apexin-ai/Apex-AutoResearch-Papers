# ops collect eval a1 lora object v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_eval_a1_lora_object_v11_20260522T155254_result.json`
- **Structured JSON:** [`08ec088c7f72c25b285b.json`](../../sessions/08/08ec088c7f72c25b285b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**总结：A1 是目前 object suite 上最好的安全方案。**

- **CAR 90%** — 超过 LoRA baseline（82%）+8pp，超过 full-FT baseline（83%）+7pp
- 核心发现：task1 chocolate_pudding 从 46%→80%（+34pp），这是 LoRA baseline 最弱的任务，SDF training signal 大幅修复了它
- A3 runtime refinement 是有害的（74.5% vs 90%），问题定位清晰：**SDF 作为 training signal 有效，作为 runtime refinement 有害**
- Displacement 也大幅下降（0.0027m vs baseline 0.01m）
- TSR 仍为 0%（与所有 LoRA 方案一致，TSR 瓶颈不在安全模块）

---
