# ssh diff and rsync hf checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diff_and_rsync_hf_checkpoints_20260523T043918_result.json`
- **Structured JSON:** [`d0cfa98291c865d1f4cd.json`](../../sessions/d0/d0cfa98291c865d1f4cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**bjb1 已有全部 westd HF checkpoint，无需传输。**

对比结果：

| 位置 | checkpoint 数量 |
|------|----------------|
| bjb1 `/checkpoints/` (本地) | 6 个 |
| bjb1 `/westd_backup/checkpoints/` | 10 个 — westd 全部 10 个已同步 |
| westd `/checkpoints/` | 10 个 |

westd 的 10 个 HF checkpoint 在 bjb1 的 `westd_backup/checkpoints/` 中全部存在：
- exp029_seed100_step5_hf
- exp029_seed2_step15_hf
- exp029_seed42_step5_hf
- exp029_seed7_high_kl_step5_hf
- exp029_seed7_high_kl_step7_hf
- intervention_c_hard_cap_step5_hf
- intervention_c_hard_cap_step7_hf
- qwen_c_prime_step5_hf
- qwen_exp029_seed100_step10_hf
- qwen_exp029_seed8_step5_hf

不需要启动 rsync。

---
