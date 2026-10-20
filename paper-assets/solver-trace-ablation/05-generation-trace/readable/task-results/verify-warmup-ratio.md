# verify warmup ratio

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_warmup-ratio_20260514T122944_result.json`
- **Structured JSON:** [`28b2fb65b18160475971.json`](../../sessions/28/28b2fb65b18160475971.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. train_grpo.py 是否接受 --warmup_ratio？
**是。** line 348: `parser.add_argument("--warmup_ratio", type=float, default=0.0)`，line 430 传给 GRPOConfig: `warmup_ratio=args.warmup_ratio`。

### 2. s42 实际 warmup_ratio = **0.0**
- 配置文件 `grpo_prolog_exec_only.yaml` **不含** warmup_ratio
- s42 命令行未传 `--warmup_ratio`（log 中 grep warmup 无结果）
- CLI default = 0.0
- **LR 证据**：step 2 LR=1e-06（满值），step 3 LR=9.98e-07（递减）→ 无 warmup，直接从 max LR 开始衰减

### 3. s43 实际 warmup_ratio = **0.1**
- `/proc/587155/cmdline` 确认命令行有 `--warmup_ratio 0.1`
- **LR 证据**：step 13 LR=2.2e-07，step 16 LR=2.8e-07，step 36 LR=6.8e-07 → LR 在递增，warmup 阶段进行中

### 4. 结论：**两者不一致，3-seed 对比无效**

| | s42 | s43 |
|---|---|---|
| warmup_ratio | 0.0 | 0.1 |
| LR schedule | 从 1e-06 直接衰减 | 前 50 步从 0 线性升到 1e-06 |

s43 当前在 **step 36/500**，warmup 阶段（0.1 × 500 = 50 步）**尚未结束**。

**s43 需要 kill 并以 warmup_ratio=0.0（或不传该参数）重新提交，才能与 s42 可比。**

---
