# analysis sft alpha4 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_alpha4_20_v2_20260521T185627_result.json`
- **Structured JSON:** [`4e00105a417dec9c9b01.json`](../../sessions/4e/4e00105a417dec9c9b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中无 W&B 记录，网络不通导致未上传。已有足够信息汇总。

---

## sft_alpha4_20_v2 实验结果

**Conclusion: SUCCESS**

### 训练概况
| 指标 | 值 |
|------|-----|
| 状态 | 正常完成 (EXIT_CODE=0) |
| 总 steps | 936 (2 epochs × 468 steps) |
| 训练样本 | 7,473 (GSM8K) |
| 训练时长 | ~18 min 49 sec |
| GPU | cuda:0 (CUDA_VISIBLE_DEVICES=2) |

### Loss 趋势
| 阶段 | Loss | Token Accuracy |
|------|------|---------------|
| 开始 (epoch 0.02) | 1.295 | 0.711 |
| 中间 (epoch 1.0) | ~0.78 | ~0.80 |
| 结束 (epoch 2.0) | ~0.70 | ~0.82 |
| **平均 train_loss** | **0.8118** | **0.8165** |

Loss 从 1.295 稳定下降至 ~0.70，收敛良好，无异常波动。

### Checkpoint
| 项目 | 值 |
|------|-----|
| checkpoint_path | `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20/` |
| 模型文件 | `model.safetensors` (11.5 GB) |
| 总大小 | 23 GB (含 checkpoint-936 子目录) |
| 格式 | safetensors, 1 shard |
| log_path | `/root/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log` |

### 备注
- `save_only_model=True` 修复了 parent 的磁盘溢出问题，checkpoint 成功保存到数据盘
- 网络不可达，W&B 未记录，数据仅在本地日志中
- 无 eval metrics（SFT 阶段不评估，等后续 GRPO→eval pipeline）
- 模型已就绪，可进入下一步 GRPO 训练

---
