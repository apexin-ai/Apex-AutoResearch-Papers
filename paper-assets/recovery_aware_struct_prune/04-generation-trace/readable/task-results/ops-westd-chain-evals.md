# ops westd chain evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-chain-evals_20260515T154434_result.json`
- **Structured JSON:** [`c44779d9417d29ebbf63.json`](../../sessions/c4/c44779d9417d29ebbf63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 tmux session 全部就位：

| Session | GPU | 状态 |
|---------|-----|------|
| `eval_sft_alpha_2p0` | cuda:1 | 正在运行 α=2.0 eval |
| `eval_sft_alpha_0p5` | cuda:1 | 等待 PID 45428 (α=2.0) 退出后自动启动 |
| `eval_sft_grasp_20` | cuda:0 | 等待 PID 38120 (GraSP pre-SFT) 退出后自动启动 |

Registry 已为 `eval_sft_grasp_20` 创建条目，状态 PREPARING。

---
