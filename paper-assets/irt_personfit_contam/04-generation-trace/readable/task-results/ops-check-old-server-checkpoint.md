# ops check old server checkpoint

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-old-server-checkpoint_20260523T124311_result.json`
- **Structured JSON:** [`d34ef6e9577dbdd69bb4.json`](../../sessions/d3/d34ef6e9577dbdd69bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从 training_args 中可以确认 `seed=42` (K* = 0x2A = 42)。所有旧 Llama s1 checkpoints 已在 westd-35694 上。

## 结果

**旧 Llama s1 (seed 42) checkpoints 已在 westd-35694 上，无需访问 19912。**

路径：`/root/autodl-tmp/ctrl_contam_llama/checkpoints/`

| 条件 | 目录 | 中间 checkpoints | adapter 大小 |
|------|------|-----------------|-------------|
| clean | `clean/` | 313, 626, 939 | 26MB |
| contam_15 | `contam_15/` | 445, 890, 1335 | 26MB |
| contam_50 | `contam_50/` | 752, 1504, 2256 | 26MB |

- 总大小：**4.5GB**（含所有 16 个子目录，包括 s2-s10 的 clean 变体和 contam_5/contam_25）
- seed 确认：training_args 中 `seed=42`
- base model：`Meta-Llama-3.1-8B-Instruct`（LoRA r=16, alpha=32）
- 19912 不在 SSH config 中，但不需要连——数据已在本地

可以直接用新代码在 westd-35694 上 re-eval 这些 checkpoint。

---
