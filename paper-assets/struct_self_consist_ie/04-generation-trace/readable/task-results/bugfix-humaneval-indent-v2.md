# bugfix humaneval indent v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_humaneval_indent_v2_20260520T212459_result.json`
- **Structured JSON:** [`f12bb40fa0ada3e93777.json`](../../sessions/f1/f12bb40fa0ada3e93777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完全有效：23/23 greedy pass, 179/184 samples pass (97.3%)。之前是 0/164 全挂。

**问题**：API 余额不足 (402 Insufficient balance)，实验在第 24 个 task 停止。已有 checkpoint，充值后可以断点续跑（脚本自带 resume 逻辑，直接重新启动即可从第 24 个 task 继续）。

需要充值 API 余额后重新启动：
```bash
nohup python -u run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results > humaneval_sc_v2.log 2>&1 &
```

---
