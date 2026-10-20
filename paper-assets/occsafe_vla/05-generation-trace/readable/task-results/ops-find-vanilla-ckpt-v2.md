# ops find vanilla ckpt v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find_vanilla_ckpt_v2_20260523T034143_result.json`
- **Structured JSON:** [`3df044bc714e9d7f0afa.json`](../../sessions/3d/3df044bc714e9d7f0afa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 完整清单

### westd-10894（50K checkpoint）

| 条件 | 50K checkpoint | 大小 |
|------|---------------|------|
| ablation_occ_detach_s2 (Detach) | **有** | 15G |
| ablation_random_occ_s2 (Random OCC) | **有** | 15G |
| depth_s2 | **有** | 15G |
| depth_s3 | **有** | 15G |
| cutoff_s2 | **无**（训练中） | — |

### westd-34685（50K checkpoint）

| 条件 | 50K checkpoint | 大小 |
|------|---------------|------|
| cutoff_s0 | **有** | 15G |
| cutoff_s1 | **有** | 15G |
| depth_s0 | **有** | 15G |
| depth_s1 | **有** | 15G |

### Vanilla checkpoint

**两台服务器均不存在任何 vanilla checkpoint 目录。** westd-10894 上仅有一个 `vanilla_s2_train.log` 日志文件和一个名为 `vanilla_s0` 的 tmux session，但无 checkpoint 数据。

### cutoff_s2 训练进度

- 当前 step: **22,511 / 50,005**（45%）
- 速度: ~2.06 it/s
- 已有 checkpoint: 10K、20K
- 预计剩余: ~3h42m，预计完成时间约今天 15:25 左右
- occ_loss cutoff 设在 step 35,000

**结论：梯度分析所需的 4 个条件中，Detach (s2) 和 Random OCC (s2) 的 50K checkpoint 就绪；cutoff_s2 还在训练中；Vanilla 的 50K checkpoint 在两台服务器上均缺失，需要确认之前的训练产出去了哪里或是否需要重新训练。**

---
