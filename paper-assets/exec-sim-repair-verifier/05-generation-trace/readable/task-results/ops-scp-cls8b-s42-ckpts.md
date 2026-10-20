# ops scp cls8b s42 ckpts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-cls8b-s42-ckpts_20260514T151842_result.json`
- **Structured JSON:** [`2c81e7208fe17a9bbddd.json`](../../sessions/2c/2c81e7208fe17a9bbddd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输完成，临时文件已清理。

## 结果

| 目标路径 | Checkpoints | 总大小 |
|---------|-------------|--------|
| `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_8b_westd/` | checkpoint-200, 2400, 2600, 2800, 3000 | 880M |
| `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_8b_conda_westd/` | checkpoint-200, 400, 600 + train.log | 529M |

注意：westd 上的 `checkpoints_repo_cls_8b/` 只有 5 个 checkpoint（200, 2400-3000），中间的 400-2200 不在该目录下。

---
