# ops fix westb ssh and read logs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_westb_ssh_and_read_logs_20260518T013606_result.json`
- **Structured JSON:** [`cc021d64046444d3d743.json`](../../sessions/cc/cc021d64046444d3d743.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**SSH**: 免密登录正常，无需修复。

**训练状态**: 两个实验仍在运行，接近完成：
- `grpo_cka_only_20`: step 94/100
- `grpo_random_20`: step 97/100

**核心发现**:

| | CKA-only 20% | Random 20% |
|---|---|---|
| Best Reward | 0.3544 (step 50) | 0.19 (step 70) |
| Mean Reward | 0.2834 | 0.1653 |
| Mean grad_norm | 1.78 | 5.23 |

CKA 模型 GRPO 效果远优于 Random（reward +71%，训练更稳定）。

**CKA step 70-90 下降确认**: reward 从 0.3419 (step 80) 降至 0.2419 (step 90)，frac_zero_std 从 0.125 (step 70) 升至 0.3 (step 90)，late-stage collapse 信号明确。

产出已写入 `artifacts/westb_grpo_complete_metrics.md`。

---
