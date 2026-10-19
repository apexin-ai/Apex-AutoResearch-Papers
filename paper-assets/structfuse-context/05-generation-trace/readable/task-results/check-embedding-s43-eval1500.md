# check embedding s43 eval1500

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_embedding-s43-eval1500_20260515T065712_result.json`
- **Structured JSON:** [`c4953c184441cd610dd0.json`](../../sessions/c4/c4953c184441cd610dd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## embedding_distance_s43 结果报告

### eval@1500 结果
| 指标 | 值 |
|------|-----|
| **R@1** | **0.5606** |
| R@5 | 0.9630 |
| R@10 | 1.0 |
| val_loss | 0.4926 |

### Early stopping
**已触发。** step 1500 时 val_loss 连续 2 次未改善（patience=2），触发 early stop。best val_loss=0.4541 @ step 500。

### Final eval（early stop 后跑的最终评估）
| 指标 | 值 |
|------|-----|
| R@1 | 0.5655 |
| R@5 | 0.9663 |
| val_loss | 0.4876 |

### best_by_R@1
**0.5606**（step 1500 的 checkpoint，保存时间 14:28）

注意 final eval 的 R@1=0.5655 略高于 best checkpoint 的 0.5606，但 final checkpoint 是按 val_loss 判断 early stop 后单独跑的评估，best_by_recall_at_1 保存的是 step 1500 的模型。

### vs random_s43 对比

| 策略 | best R@1 | 胜负 |
|------|----------|------|
| random_s43 | 0.5554 | |
| **embedding_distance_s43** | **0.5606** | **+0.52pp, embedding_distance 胜** |

Seed 43 上 embedding_distance 以 +0.52 个百分点优于 random。如果以 final eval 计算则差距更大（0.5655 vs 0.5554, +1.01pp）。

### 进程状态
PID 337267 仍在运行（19h33m），两块 GPU 100% 占用——说明 `run_m2_full_qwen.sh` 脚本正在运行后续实验（embedding_distance_s43 已完成）。

---
