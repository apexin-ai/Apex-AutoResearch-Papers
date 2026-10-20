# westd-29022 磁盘清理报告

**日期**: 2026-05-20
**目标磁盘**: /dev/md0 → /root/autodl-tmp
**清理目标**: ≥100GB 可用空间

## 清理前状态

| 指标 | 值 |
|------|------|
| 总容量 | 619G |
| 已用 | 550G |
| 可用 | 70G |
| 使用率 | 89% |

## 删除明细

### 1. optimizer.pt 文件（Director 明确批准）

| 文件 | 大小 |
|------|------|
| grpo_cka_only_20/checkpoint-100/optimizer.pt | 15G |
| grpo_shortgpt_20/checkpoint-100/optimizer.pt | 6.9G |
| **小计** | **~22G** |

### 2. 冗余 checkpoint-100 目录

以下实验 root 目录已有最终 model.safetensors，checkpoint-100/ 为完全冗余副本（模型大小一致），安全删除。

| 目录 | 大小 |
|------|------|
| grpo_cka_only_20/checkpoint-100/ | 12G |
| grpo_rasp_25/checkpoint-100/ | 11G |
| grpo_stage2_rasp_20_fair/checkpoint-100/ | 12G |
| grpo_stage2_standard_20_fair/checkpoint-100/ | 12G |
| grpo_standard_20_seed123/checkpoint-100/ | 12G |
| grpo_standard_20_seed456/checkpoint-100/ | 12G |
| grpo_standard_25/checkpoint-100/ | 11G |
| grpo_unpruned_v2/checkpoint-100/ | 15G |
| **小计** | **~97G** |

### 跳过（安全保留）

| 目录 | 原因 |
|------|------|
| grpo_cka_only_15/checkpoint-20 | 无 root model，checkpoint 是唯一副本 |
| grpo_shortgpt_20/checkpoint-100 | 无 root model，checkpoint 是唯一副本 |
| grpo_standard_15/checkpoint-20 | 无 root model |
| /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B (15G) | 不在项目目录下，按安全规则不可删除 |

## 清理后状态

| 指标 | 值 |
|------|------|
| 总容量 | 619G |
| 已用 | 435G |
| 可用 | **185G** |
| 使用率 | 71% |
| **总释放** | **~115G** |

## 结论

目标达成。可用空间 185G，远超 100G 要求，足够支撑 15% GRPO 重启（~120GB checkpoint 空间）。
