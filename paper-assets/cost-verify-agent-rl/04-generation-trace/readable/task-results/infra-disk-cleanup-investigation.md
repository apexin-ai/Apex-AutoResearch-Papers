# infra disk cleanup investigation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup-investigation_20260514T124635_result.json`
- **Structured JSON:** [`8d26de776c8b242f9f88.json`](../../sessions/8d/8d26de776c8b242f9f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘调查报告

### 当前磁盘状态

磁盘已从任务描述的 95% 降到 **13%**，有其他进程在调查期间执行了清理。

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp | 250G | 32G | 219G | 13% |
| / (根分区) | 30G | 7.3G | 23G | 25% |

### /root/autodl-tmp 各目录明细

| 目录 | 大小 | 状态 | 说明 |
|------|------|------|------|
| `.hf_cache/` | **23G** | 可部分清理 | 见下方细分 |
| `models/Qwen/` | 3.8G | **保留** | Qwen3-1.7B base 模型 |
| `checkpoints/exp008_sft/final/` | 3.3G | **保留** | SFT warmup 最终模型（memory.md 引用） |
| `alfworld/` | 2.2G | **保留** | ALFWorld 环境数据 |
| `pgpf/` | 78M | 可删除 | 旧的 orthogonality 分析脚本，非核心 |
| `sft_data/` | 4.3M | **保留** | SFT 训练数据 |
| `logs/`, `ray_tmp/`, `tmp/` | ~0 | 空 | 已清理 |

### HF Cache 细分 (23G)

| 缓存条目 | 大小 | 建议 |
|----------|------|------|
| `models--dunzhang--stella_en_1.5B_v5` | **17G** | **可删除** — embedding 模型，非项目核心依赖 |
| `datasets--teknium--OpenHermes-2.5` | 1.9G | **可删除** — 通用指令数据集，未在当前实验使用 |
| `datasets--u-10bei--sft_alfworld_trajectory_dataset` | 4.9M | **保留** — ALFWorld SFT 数据 |

### 已被清理的内容（调查期间消失）

| 原目录 | 原大小 | 状态 |
|--------|--------|------|
| `checkpoints/exp013f/` (global_step_10-30) | 62G | 已删除 |
| `checkpoints/exp008_sft/checkpoint-75` | 9.7G | 已删除 |
| `checkpoints/exp008_sft/checkpoint-225` | 9.7G | 已删除 |

### 可释放空间汇总

| 项目 | 可释放 |
|------|--------|
| stella_en_1.5B_v5 (HF cache) | 17G |
| OpenHermes-2.5 (HF cache) | 1.9G |
| pgpf/ | 78M |
| **合计** | **~19G** |

### 结论

磁盘压力已解除（219G 可用）。如仍需进一步释放空间，可删除 stella embedding 模型缓存 (17G) 和 OpenHermes 数据集 (1.9G)。核心资产（exp008_sft/final、Qwen base、alfworld 数据、sft_data）均完好。

需要执行清理吗？

---
