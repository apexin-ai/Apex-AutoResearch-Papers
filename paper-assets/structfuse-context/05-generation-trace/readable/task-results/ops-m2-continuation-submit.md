# ops m2 continuation submit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m2-continuation-submit_20260513T085449_result.json`
- **Structured JSON:** [`aecfd7c728b5a5ec0a76.json`](../../sessions/ae/aecfd7c728b5a5ec0a76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

---

**Random 策略完成** (step 1642/1642)

| 指标 | Best @step500 | Final @step1642 |
|------|-----------|-------------|
| val_loss | **0.4834** | 0.5978 |
| R@1 | **0.5357** | 0.5122 |
| R@5 | 0.9808 | 0.9826 |
| R@10 | 1.0 | 1.0 |

- Best checkpoint: `.../random_s42/best` (step 500)
- Final checkpoint: `.../random_s42/final`
- 最佳模型在 Epoch 1 中段（step 500）取得，之后持续过拟合

**接续状态**：`run_m2_embed_verify.sh` 原脚本已自动启动 **embedding_distance** 策略（PID 37880, cuda:1, 18750 MiB, 17:04 开始），之后会自动继续 dataflow_aware。**不需要手动启动接续脚本**，否则会造成 GPU 冲突。

---
