# verify sft confound check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_sft_confound_check_20260518T013431_result.json`
- **Structured JSON:** [`e99ab5071166a3babaad.json`](../../sessions/e9/e99ab5071166a3babaad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：无 Confound

所有实验的 `model_path` 完全一致：

| 实验 | 服务器 | model_path |
|------|--------|-----------|
| hsweep_h2 (seed1/seed2) | bjb1-17606 | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` |
| factorial_h2_episode_adv | bjb1-17606 | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` |
| factorial_h2_episode_adv | westd-47453 | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` |
| exp029_episode_level | bjb1-17606 | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` |
| exp028c_selfguide_recipe | bjb1-17606 | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` |

**全部 5 个实验均使用同一 SFT checkpoint (`qwen3_exp021_ragen_sft_v4`) 作为起点。** Reviewer 的担忧不成立，2×2 factorial 设计不存在模型起点的 confound。

---
