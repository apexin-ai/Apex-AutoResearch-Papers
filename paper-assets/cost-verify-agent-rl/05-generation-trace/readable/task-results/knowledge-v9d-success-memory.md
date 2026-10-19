# knowledge v9d success memory

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_v9d_success_memory_20260520T095446_result.json`
- **Structured JSON:** [`42d4f2f7bcf6460975a7.json`](../../sessions/42/42d4f2f7bcf6460975a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 4 条新经验：

1. **save_contents yaml 路径** — 必须在 `actor_rollout_ref.actor.checkpoint` 下，错误路径导致 92GB vs 33GB checkpoint
2. **FSDP2 checkpoint 格式** — rank shards 需 `convert_fsdp_to_hf.py` 合并才能部署
3. **NCCL deadlock 模式** — 0% GPU util + 高显存占用 = collective 死锁，直接 kill
4. **8B GRPO 饱和速度** — ≤15 steps 即饱和，需提前规划 OOD eval 和 early stopping

---
