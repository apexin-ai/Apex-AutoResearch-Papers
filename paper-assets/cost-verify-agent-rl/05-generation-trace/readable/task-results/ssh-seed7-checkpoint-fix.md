# ssh seed7 checkpoint fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed7_checkpoint_fix_20260522T222603_result.json`
- **Structured JSON:** [`01a970c9ff41fd4f46f1.json`](../../sessions/01/01a970c9ff41fd4f46f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### bjb1-17606

**seed7 checkpoint 状态：**
| 目录 | 状态 |
|------|------|
| `qwen_exp029_seed7_high_kl_step5_hf` | 已存在（无需重命名） |
| `qwen_exp029_seed7_high_kl_step7_hf` | 刚完成重命名 (从 `exp029_seed7_high_kl_step7_hf`) |
| `exp029_seed7_high_kl_step5_hf` | 旧目录仍在，可清理 |
| `seed7-step5-mask-check` | 调试目录 |

**GPU 状态：** 两张卡均空闲（0 MiB / 97887 MiB）

### westd-47453

**seed7 checkpoint 副本完整：**
- `/root/autodl-tmp/checkpoints/qwen_exp029_seed7_high_kl_step5_hf`
- `/root/autodl-tmp/checkpoints/qwen_exp029_seed7_high_kl_step7_hf`
- `/root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf`（旧名副本）
- `/root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step7_hf`（旧名副本）

westd 上 qwen_ 前缀版本均已存在，无需操作。bjb1 的 step7 已修复，seed7 eval 可以重跑。

---
