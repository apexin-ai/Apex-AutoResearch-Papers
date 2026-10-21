# code kill magnitude start gradient

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kill_magnitude_start_gradient_20260517T073629_result.json`
- **Structured JSON:** [`d370b18b9f4d536870e9.json`](../../sessions/d3/d370b18b9f4d536870e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| **Magnitude SFT kill** | 已确认终止 (PID 689115, SIGTERM 成功) |
| **Gradient prune** | 已完成。MLP groups pruned: 200/784, actual sparsity: 19.09% |
| **Gradient eval/SFT pipeline** | 已排队在 `scoring_ablation_v2` tmux session，等 GPU 0 空闲后自动启动 |
| **Multiseed eval** | seed=456, 100/200 samples, ETA ~3-5 min |
| **后续 pipeline** | 脚本自动执行 gradient eval → SFT → eval → random 全流程 → cka_only 全流程 |

Pipeline 脚本 (`run_remaining_ablation.sh`) 包含完整的 gradient + random + cka_only 三个方法各 4 步。GPU 0 释放后（multiseed 约 3-5 min 完成）自动开始，全程 tee 到 `results/ablation_log.txt`。

---
