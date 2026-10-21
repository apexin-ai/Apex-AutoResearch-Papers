# eval 10894 batch cutoff s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_10894_batch_cutoff_s3_20260526T080014_result.json`
- **Structured JSON:** [`5ec26a4cda6167c8913c.json`](../../sessions/5e/5ec26a4cda6167c8913c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Eval 已启动
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| cutoff_45k_s2_v2 | cuda:0 | 114371 | **eval 运行中**，已开始 rollout (Task 0, 1/50) |

### 仍在训练（未启动 eval）
| 实验 | GPU | 训练进度 | 最新 checkpoint |
|------|-----|---------|----------------|
| mvp_occ_s3_v2 | cuda:1 | ~60% (30000/50000) | 30000_chkpt |
| full_occ_ln_s3_v2 | cuda:2 | ~60% (30000/50000) | 30000_chkpt |
| ablation_occ_detach_s3_v2 | cuda:3 | ~60% (30000/50000) | 30000_chkpt |

### GPU 使用
| GPU | 显存占用 |
|-----|---------|
| cuda:0 | 16,778 / 97,887 MiB (eval) |
| cuda:1 | 62,203 / 97,887 MiB (训练) |
| cuda:2 | 62,203 / 97,887 MiB (训练) |
| cuda:3 | 62,203 / 97,887 MiB (训练) |

三个训练实验均在 30k/50k 步，预计还需数小时完成。50k checkpoint 就绪后即可启动各自的 eval。

---
