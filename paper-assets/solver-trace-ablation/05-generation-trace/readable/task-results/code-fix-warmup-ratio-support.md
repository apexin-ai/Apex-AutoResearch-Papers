# code fix warmup ratio support

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-warmup-ratio-support_20260514T071030_result.json`
- **Structured JSON:** [`45dc9c0486c7695c119d.json`](../../sessions/45/45dc9c0486c7695c119d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

- **L342**: `parser.add_argument("--warmup_ratio", type=float, default=0.0)` — CLI 参数已添加，`--help` 可见
- **L424**: `warmup_ratio=args.warmup_ratio` — 已传入 GRPOConfig
- YAML 配置 `grpo_prolog_exec_only_k16_warmup.yaml` 中 `warmup_ratio: 0.1` 会通过现有的 config merge 逻辑自动加载到 `args.warmup_ratio`

---
