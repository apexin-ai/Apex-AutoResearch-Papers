# ops full gpu status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_status_check_20260524T040658_result.json`
- **Structured JSON:** [`6343aad99e18e099599e.json`](../../sessions/63/6343aad99e18e099599e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894
| GPU | exp_id | 状态 | 进度 | ETA (UTC) |
|-----|--------|------|------|-----------|
| 0 | cutoff_s2_v2 | **即将完成** | 47902/50005 (96%) | ~04:40 (~30min) |
| 1 | detach_ln_s0 | 训练中 | 37121/50005 (74%) | ~07:28 |
| 2 | detach_ln_s1 | 训练中 | 36864/50005 (74%) | ~07:31 |
| 3 | detach_ln_s2 | 训练中 | 36941/50005 (74%) | ~07:30 |

全部 4 GPU 99% 利用率，~62GB 显存占用，正常。

## westd-34685
| GPU | exp_id | 状态 | 进度 | ETA (UTC) |
|-----|--------|------|------|-----------|
| 0 | cutoff_45k_s0 | 训练中 | 29593/50005 (59%) | ~09:25 |
| 1 | cutoff_15k_s0 | 训练中 | 30426/50005 (61%) | ~09:19 |
| 2 | cutoff_25k_s1 | 训练中 | 16605/50005 (33%) | ~12:55 |
| 3 | reverse_cutoff_s1 | 训练中 | 16632/50005 (33%) | ~12:49 |

4 GPU 均有进程，当前 GPU-Util 0%（cutoff_15k_s0 刚保存 step-30000 checkpoint，可能引起短暂空闲）。

### 需要注意

1. **cutoff_s2_v2** 约 30 分钟后完成。checkpoint 目录已有 40000 步的 checkpoint，预计 50005 步后会保存最终 checkpoint。GPU 0 完成后将空闲。
2. **reverse_cutoff_s1 occ_loss 异常偏高**：`occ_loss=0.1791`，其他实验同阶段在 0.009-0.013 范围。可能存在问题，建议关注。
3. **34685 迭代速度有波动**：cutoff_45k_s0 和 cutoff_15k_s0 出现间歇性慢迭代（4-5s/it vs 正常 ~0.93s/it），疑似 checkpoint 保存或数据加载抖动，整体进度正常。

---
