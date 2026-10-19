# eval universal 3seed v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_universal_3seed_v2_20260516T231122_result.json`
- **Structured JSON:** [`0874a03b2a79f3a1ccc6.json`](../../sessions/08/0874a03b2a79f3a1ccc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Universal LoRA r16 eval 已在 cuda:3 上运行 (PID 287920)：
- **配置**: 8 perturbation types × 3 seeds × 20 episodes = 480 episodes
- **LoRA checkpoint**: `/root/autodl-tmp/checkpoints/v3_lora_universal_r16/v3lora_universal_r16/final/` (72 modules, scaling=2.0)
- **初步观察**: nominal seed=42 前 11 episodes 中 8/11 OK (~73%)
- **预计完成**: ~50 分钟
- **Baseline eval** 同时在 cuda:0 上并行运行

15 分钟后检查进度。

---
