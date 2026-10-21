# ssh checkpoint discovery

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_checkpoint-discovery_20260519T223534_result.json`
- **Structured JSON:** [`c5a80f1dd81c14231136.json`](../../sessions/c5/c5a80f1dd81c14231136.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 0 僵尸进程
已 `kill -9`，GPU 0 显存 **0 MiB** — 清空成功。

### Checkpoint 清单

| 路径 | 可用 Checkpoint |
|------|----------------|
| **CWM 8B s123** (`checkpoints_repo_cwm_8b_s123/`) | `checkpoint-100`, `checkpoint-200`, `checkpoint-300` |
| **CLS 8B s456 v2** (`checkpoints_repo_cls_8b_s456_v2/`) | `checkpoint-600`, `checkpoint-1600`, `checkpoint-1800`, `checkpoint-2000`, `checkpoint-2200` |
| **DeepSeek CLS s456 v2** (`checkpoints_deepseek_cls_repo_s456_v2/`) | `checkpoint-2163` (仅一个) |
| **DeepSeek CLS s456 v3** | 路径不存在 |

### 训练进度

| 任务 | 状态 |
|------|------|
| **DeepSeek CLS s456 v2** | **正在训练**，step 2333/6489 (36%)，epoch 1 eval_loss=0.0724，~11s/it，预估剩余 ~13h |
| **CWM 8B s123** | **正在训练**，step 2117/9335 (23%)，~7 it/s，进展正常 |

两个训练都在正常跑。DeepSeek CLS 只存了一个 checkpoint（step 2163，epoch 1 结束时），v3 路径不存在说明没有 v3 训练。

---
