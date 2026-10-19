# infra disk cleanup bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup-bjb1_20260515T051142_result.json`
- **Structured JSON:** [`93cd6424f4ee87651c56.json`](../../sessions/93/93cd6424f4ee87651c56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**释放 ~135G，磁盘使用率从 94% 降至 39%**（98G/250G，剩余 153G）。

**删除内容：**
| 目录 | 释放空间 |
|------|---------|
| exp020b | 62G |
| exp022 | 21G |
| exp015 | 21G |
| exp016 | 21G |
| exp017_expert_sft | 13G |
| tmp/* | 132M |
| 空目录（exp019_INVALID, exp020, exp020c, exp020d, exp023） | ~0 |

**保留内容：**
- exp008_sft (3.3G) + symlink qwen3_sft_final
- exp019b_expert_sft_v3 (23G) + 2 个 symlink
- exp021_ragen_sft_v4 (23G) + symlink qwen3_exp021_ragen_sft_v4
- exp023c (21G) — 含 global_step_5

---
