# code sync 021 script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync-021-script_20260517T105559_result.json`
- **Structured JSON:** [`928cad421baabdc84c3e.json`](../../sessions/92/928cad421baabdc84c3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。结果汇总：

**脚本同步** — 已写入 `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/exp_021_full_sgs_cheetah_s1.sh` 并 chmod +x，内容与本地一致。

**验证结果**:
- `full_sgs` 参数在 configs.yaml 中存在（找到 key `['full_sgs']`）
- logdir 下无 `021` 相关目录，路径无冲突
- `MUJOCO_EGL_DEVICE_ID=0` 已在脚本中确认

**exp_019b 进度**: step **141000** / train_return 14.6 / 705 episodes。

---
