# ops traj repo 8k cuda3 seeds

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-repo-8k-cuda3-seeds_20260516T162134_result.json`
- **Structured JSON:** [`d81a31202568a86d301a.json`](../../sessions/d8/d81a31202568a86d301a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Both seeds trained and evaluated on cuda:3.

## Final Report: TRAJ repo-8k Multi-Seed Results

| Seed | Accuracy | F1 Macro | Resolved F1 | Unresolved F1 | Unparseable | Best Eval Loss |
|------|----------|----------|-------------|---------------|-------------|----------------|
| 456  | 75.0%    | 75.00%   | 75.0%       | 75.0%         | 0           | 0.1547         |
| 999  | **79.2%** | **78.57%** | **82.1%**  | 75.0%         | 0           | 0.1565         |

Both experiments registered as DONE with conclusion=success. Checkpoints at:
- `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s456/best/`
- `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s999/best/`

---
