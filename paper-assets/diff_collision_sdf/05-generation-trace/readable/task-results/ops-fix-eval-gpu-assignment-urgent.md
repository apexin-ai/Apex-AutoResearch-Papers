# ops fix eval gpu assignment urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_gpu_assignment_urgent_20260522T154305_result.json`
- **Structured JSON:** [`cc6ccf1ce606b060275e.json`](../../sessions/cc/cc6ccf1ce606b060275e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 分配全部正确。

**最终状态：**

| GPU | 进程 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | a1_lora_spatial 训练 | 299910 | 23892 MiB |
| cuda:1 | baseline fullft spatial eval | 697980 | 8163 MiB |
| cuda:2 | oracle A3 force_refine eval | 697903 | 8625 MiB |
| cuda:3 | a1 lora object eval | 660998 | 8527 MiB |

- 3 个错误进程 (686035, 688244, 690045) 已 kill
- PID 660998 原本就在 cuda:3，未受影响
- 两个新 eval 已在正确 GPU 上运行，tmux session: `oracle_a3_force_refine` (pts/7) 和 `eval_baseline_fullft_spatial_v11` (pts/8)

---
