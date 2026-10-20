# code exp 002 k ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_002_k_ablation_20260516T192159_result.json`
- **Structured JSON:** [`c8dfff6316c470e566ea.json`](../../sessions/c8/c8dfff6316c470e566ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-002 启动成功。

**状态**:
- **tmux session**: `exp002`
- **PID**: 235733
- **进度**: Phase 1 进行中 (trace generation), 第 1 题 31.6s → ~32s/problem

**时间预估**:
- Phase 1 (生成 K=20 traces, 804题): 804 × ~32s ≈ **7.1h**
- Phase 2 (5 个 K 值的 constraint extraction + scoring): 每个 K 约 573 min (与 exp-001 类似) → 总计 ~**48h**
- **总计 ≈ 55h**

**产出文件**:
- traces cache: `results/k_ablation/traces_k20.json` (Phase 1 每题 checkpoint)
- 每个 K: `results/k_ablation/sica_k{6,8,11,16,20}_14b.json`
- 汇总: `results/k_ablation/sica_k_ablation_14b.json`

**断点续跑**: 若中断，同一命令重跑即可（Phase 1 从 traces cache 恢复已完成的题目）。Phase 2 的 `--resume` flag 可跳过整个 Phase 1。

**监控**: `tmux capture-pane -t exp002 -p | tail -20` 或查 log `results/k_ablation/exp002.log`

---
