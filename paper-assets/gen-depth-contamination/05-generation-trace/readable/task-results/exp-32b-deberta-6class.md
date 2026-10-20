# exp 32b deberta 6class

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_32b-deberta-6class_20260519T222823_result.json`
- **Structured JSON:** [`83b8d1aecd4e2c9563d9.json`](../../sessions/83/83b8d1aecd4e2c9563d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

**汇报：**

| 项目 | 详情 |
|------|------|
| **数据路径** | `/root/autodl-tmp/gen-depth-contamination/data/exp_32b_c4/` |
| **Depth 文件** | depth_0.jsonl ~ depth_5.jsonl（6 个全部存在） |
| **样本数** | 30,000（6 class × 5,000 docs） |
| **num_classes** | 6（depth 0-5），之前是 5（0-4） |
| **GPU** | cuda:0，PID 139848，13.9GB 显存，94% 利用率 |
| **cuda:1** | 空闲（3MiB） |
| **K\* 索引** | 已确认 1-indexed |
| **Tmux session** | `deberta_32b_6class` |
| **日志** | `logs/deberta_32b_6class.log` |
| **当前进度** | Fold 1/5 训练中 |
| **预计时长** | 之前 5-class 跑了 40 min，6-class 样本多 20%，预计 ~50 min |
| **结果输出** | `results/exp_deberta_c4/exp_32b_c4_results.json`（会覆盖旧的 5-class 结果） |

---
