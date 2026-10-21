# ops checkpoint integrity audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint_integrity_audit_20260525T194947_result.json`
- **Structured JSON:** [`0c6d38619d307812c64a.json`](../../sessions/0c/0c6d38619d307812c64a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。所有 `best/` 目录的 base-only 问题**已经被修复过了**（存在 `model_base_backup.safetensors`）。

## 审计结果

| 目录 | model.safetensors 大小 | 状态 | model_lora.safetensors | 操作 |
|------|----------------------|------|----------------------|------|
| seed0_l005/best/ | — | NOT FOUND (无 best/ 目录) | 无 | — |
| seed0_l005/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed0_l01/best/ | — | NOT FOUND (无 best/ 目录) | 无 | — |
| seed0_l01/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed1_l005/best/ | symlink → model_lora.safetensors | ✅ 已修复 | 有 (7.54GB) | 已修复 |
| seed1_l005/29999/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed1_l005/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed1_l01/best/ | symlink → model_lora.safetensors | ✅ 已修复 | 有 (7.54GB) | 已修复 |
| seed1_l01/29999/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed1_l01/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed2_l005/best/ | symlink → model_lora.safetensors | ✅ 已修复 | 有 (7.54GB) | 已修复 |
| seed2_l005/29999/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed2_l005/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed2_l01/best/ | symlink → model_lora.safetensors | ✅ 已修复 | 有 (7.54GB) | 已修复 |
| seed2_l01/29999/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed2_l01/30000/ | 7,540,115,784 | ✅ OK | 无 | 无需 |
| seed0_l005_p2abl/ | — | 无 checkpoint（仅 wandb_id.txt） | — | — |
| phase2_lambda0_s0_stage1/ | — | 无 checkpoint（仅 wandb_id.txt） | — | — |

## 总结

- **base-only 问题**：4 个 `best/` 目录曾有此问题（seed1_l005, seed1_l01, seed2_l005, seed2_l01），**全部已修复**（symlink → model_lora.safetensors，原 base-only 文件保留为 model_base_backup.safetensors）
- **所有数字 checkpoint（29999/, 30000/）**：均为 7,540,115,784 bytes，正确含 LoRA weights，无需修复
- **seed0_l005 和 seed0_l01 没有 `best/` 目录**：只有 `30000/`，这不是 base-only 问题，而是缺少 best checkpoint 选择。如果 eval 需要用 best/，需要单独处理（可将 30000/ 作为 best 或重新运行 best selection）
- **无法修复的情况**：0 个

---
