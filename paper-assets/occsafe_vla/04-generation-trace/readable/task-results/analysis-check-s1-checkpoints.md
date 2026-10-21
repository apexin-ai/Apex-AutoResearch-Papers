# analysis check s1 checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_s1_checkpoints_20260525T074534_result.json`
- **Structured JSON:** [`46027fa8d808d7629469.json`](../../sessions/46/46027fa8d808d7629469.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### S1 Checkpoint 可用性

| Checkpoint | 状态 | 位置 | 详情 |
|---|---|---|---|
| **cutoff_15k_s1** | ✅ 可用 | 34685: 15G (完整 merged model + lora_adapter)&lt;br>10894: 463M (仅 lora_adapter) | 34685 上有完整的 50000_chkpt，含 4 个 safetensors shard + action_head/occ_head/proprio_projector |
| **cutoff_25k_s1** | ❌ 丢失 | 两台服务器均不存在 | |
| **cutoff_s1** (50k) | ❌ 丢失 | 两台服务器均不存在 | |
| **cutoff_45k_s1** | ❌ 不可用 | 34685: 目录存在但仅含 dataset_statistics.json (4K)，无模型文件 | 旧训练未完成/失败 |
| **reverse_cutoff_s0** | ❌ 丢失 | 两台服务器均不存在 | |
| **reverse_cutoff_s1** | ❌ 丢失 | 两台服务器均不存在 | |

**结论：6 个目标 checkpoint 中，仅 cutoff_15k_s1 可用（在 34685 上）。**

### 正在训练的实验 (34685) — 中间 checkpoint 状态

4 个实验均已产生 `10000_chkpt` 中间 checkpoint：

| 实验 | 中间 checkpoint | 目录大小 |
|---|---|---|
| cutoff_25k_s2_v3 | ✅ 有 10000_chkpt | — |
| reverse_cutoff_s2_v3 | ✅ 有 10000_chkpt | — |
| cutoff_45k_s1_v3 | ✅ 有 10000_chkpt | 15G |
| cutoff_15k_s2_v2 | ✅ 有 10000_chkpt | — |

注意 `cutoff_45k_s1_v3` 总共 15G，说明其 10000_chkpt 已保存了完整模型。该实验完成后将填补 cutoff_45k_s1 的空缺。

### 磁盘
- 34685: `/root/autodl-tmp/` 350G 总量，已用 216G，剩余 135G (62%)

---
