# fix westd disk execute cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_disk_execute_cleanup_20260516T142447_result.json`
- **Structured JSON:** [`87b4d289ca38bc9dd228.json`](../../sessions/87/87b4d289ca38bc9dd228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理已被执行过。汇总：

**磁盘状态**: `/dev/md0` 750G, 已用 635G (85%), 剩余 **116G** — 不再紧急。

**Phase 1 — 损坏 checkpoint**: 4 个目录均已不存在（已清理）
- `/root/autodl-tmp/grpo_rasp_qwen_math/checkpoint-40` — 不存在
- `/root/autodl-tmp/grpo_standard_qwen_math/checkpoint-35` — 不存在
- `/root/autodl-tmp/grpo_rasp_25_qwen_math/checkpoint-25` — 不存在
- `/root/autodl-tmp/grpo_standard_25_qwen_math/checkpoint-25` — 不存在

**Phase 2 — 旧 checkpoint**: 4 个实验的整个输出目录均已不存在（已被彻底清理）
- `/root/autodl-tmp/grpo_rasp_qwen_math/` — 不存在
- `/root/autodl-tmp/grpo_standard_qwen_math/` — 不存在
- `/root/autodl-tmp/grpo_rasp_25_qwen_math/` — 不存在
- `/root/autodl-tmp/grpo_standard_25_qwen_math/` — 不存在

**运行中实验**: 两个进程均存活
- PID 13703 (cuda:0) — `grpo_rasp_qwen_math`，输出到 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math`
- PID 13783 (cuda:1) — `grpo_standard_qwen_math`，输出到 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math`

注意：运行中的实验写入路径是 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_*`，与清理目标 `/root/autodl-tmp/grpo_*` 是不同路径，未受影响。无需进一步操作。

---
