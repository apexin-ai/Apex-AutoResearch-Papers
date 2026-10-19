# train lora baseline s2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_lora_baseline_s2_20260526T023547_result.json`
- **Structured JSON:** [`445b912d87700cadfec6.json`](../../sessions/44/445b912d87700cadfec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并开始迭代：

- **服务器**: westd-45947, GPU 0 (19093 MiB / 97887 MiB)
- **进度**: step 16/30000，~1.2s/it
- **Loss**: ~0.13（Phase 1 LoRA frozen，正常初始值）
- **预估总时长**: ~10h（与 seed0/seed1 的 ~4.6s/step 相比更快，因 RTX PRO 6000 96GB 够大无需 gradient checkpointing 开销；稳定后速度可能回到 ~1.2s/step）
- **Registry**: `train_pi05_lora_baseline_s2` → RUNNING

---
