# infra qwen3 4b traj eval launch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen3-4b-traj-eval-launch_20260518T222922_result.json`
- **Structured JSON:** [`564d28a4272f53944a8c.json`](../../sessions/56/564d28a4272f53944a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成。结果：

| 指标 | 值 |
|------|-----|
| **脚本** | `eval_traj_verifier.py` |
| **Overall Accuracy** | **72.9%** |
| **F1 macro** | 72.62% |
| **vs Majority baseline** | +18.8pp (54.2% → 72.9%) |
| **Unresolved** | P=71.4%, R=68.2%, F1=69.8% |
| **Resolved** | P=74.1%, R=76.9%, F1=75.5% |
| **Per-test consistency** | 72.9% (35/48) |
| **耗时** | ~15s (48 test samples) |

输出保存在 `/root/autodl-tmp/eval_results/qwen3_4b_traj_repo_s42_best/eval_test_s42.json`。

---
