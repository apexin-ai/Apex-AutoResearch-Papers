# ops collect starcoder trajectories

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-starcoder-trajectories_20260515T183226_result.json`
- **Structured JSON:** [`28a666e018656a5db0c0.json`](../../sessions/28/28a666e018656a5db0c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出：

**文件**: `artifacts/analysis/starcoder_training_trajectories.json` (art_20260515_223d71)

**3 个已完成 runs 摘要**:

| Run | Best R@1 | Best val_loss | Early Stop | Trajectory Length |
|-----|----------|---------------|------------|-------------------|
| random_s42 | 0.4604 (step 2500) | 0.6134 (step 1000) | 无 (3 epochs, timeout@4200/4242) | 8 eval points |
| random_s43 | 0.4912 (step 1500) | 0.5239 (step 1500) | step 2500 | 5 eval points + final eval |
| random_s44 | 0.4871 (step 1500) | 0.5913 (step 500) | step 1500 | 3 eval points + final eval |

**Random baseline 汇总**: mean R@1 = 0.4796 ± 0.016

**embedding_distance_s42**: 运行中，step 250，尚无 eval 数据（首次 eval 在 step 500）。

---
