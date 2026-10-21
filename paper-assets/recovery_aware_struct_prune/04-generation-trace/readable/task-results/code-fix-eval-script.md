# code fix eval script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-script_20260514T200504_result.json`
- **Structured JSON:** [`3298d3b63c9687d4ede6.json`](../../sessions/32/3298d3b63c9687d4ede6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查：`/root/recovery_aware_struct_prune/src/run_full_eval_all.sh`

改动点：
- GPU0 队列开头新增 baseline eval（`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` → `results/eval_baseline_7b_full.json`）
- 原有 4 个模型 eval 保持不变，全量 1319 samples，`--max_new_tokens 4096`
- GPU0 跑 3 个（baseline + RASP prune + RASP recovery），GPU1 跑 2 个（Standard prune + Standard recovery）

训练完成后执行：`bash src/run_full_eval_all.sh`

---
