# analysis exp 009 v3 final harvest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_v3_final_harvest_20260517T070309_result.json`
- **Structured JSON:** [`b2d3bb910cc0c84e9fe0.json`](../../sessions/b2/b2d3bb910cc0c84e9fe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp-009 v3 状态报告

### 1. 完成状态：**未完成**

v3 实验在平台重启后因 `python` 不在 PATH（conda 环境未加载）而**立即失败**（每个 log 仅 54 字节，内容为 `python: command not found`）。无进程运行，无 tmux session 存活。

结果来自 v2 运行，v3 没有产生任何新结果。

### 2. 已有结果汇总（v2 产出）

| Ratio | Strategy | Seeds | MMLU (mean±std) | HellaSwag (mean±std) |
|-------|----------|-------|-----------------|---------------------|
| 10% | no_filter | 4/5 | 0.6058±0.0002 | 0.6687±0.0006 |
| 10% | binary_ours | 4/5 | 0.6080±0.0006 | 0.6728±0.0008 |
| 10% | graduated | 3/5 | 0.6064±0.0015 | 0.6693±0.0017 |
| 30% | no_filter | 4/5 | 0.6068±0.0008 | 0.6670±0.0016 |
| 30% | binary_ours | 4/5 | 0.6080±0.0014 | 0.6723±0.0004 |
| 30% | graduated | 3/5 | 0.6075±0.0006 | 0.6663±0.0012 |
| 50% | no_filter | 4/5 | 0.6064±0.0015 | 0.6682±0.0004 |
| 50% | binary_ours | 3/5 | 0.6085±0.0008 | 0.6729±0.0004 |
| 50% | graduated | 3/5 | 0.6069±0.0001 | 0.6680±0.0001 |

### 3. Graduated vs Binary_ours 差值

| Ratio | MMLU diff | HellaSwag diff |
|-------|-----------|----------------|
| 10% | -0.0015 | -0.0035 |
| 30% | -0.0005 | -0.0059 |
| 50% | -0.0016 | -0.0049 |

Graduated 在所有 ratio 上均**略逊于** binary_ours。

Binary_ours vs No_filter（过滤收益）：

| Ratio | MMLU diff | HellaSwag diff |
|-------|-----------|----------------|
| 10% | +0.0022 | +0.0041 |
| 30% | +0.0012 | +0.0053 |
| 50% | +0.0020 | +0.0047 |

Binary 过滤在所有条件下均有正向提升。

### 4. GPU 状态

| GPU | Utilization | Memory |
|-----|-------------|--------|
| 0 | 0% | 0/24564 MiB |
| 1 | 0% | 0/24564 MiB |
| 2 | 0% | 0/24564 MiB |
| 3 | 0% | 0/24564 MiB |

4×GPU 完全空闲。

### 5. 缺失数据

| Ratio | Strategy | Missing Seeds |
|-------|----------|---------------|
| 10% | no_filter | seed 4 |
| 10% | binary_ours | seed 4 |
| 10% | graduated | seed 3, 4 |
| 30% | no_filter | seed 4 |
| 30% | binary_ours | seed 4 |
| 30% | graduated | seed 3, 4 |
| 50% | no_filter | seed 4 |
| 50% | binary_ours | seed 3, 4 |
| 50% | graduated | seed 3, 4 |

总计缺失：32/45 中完成 32 个... 不对，已完成 **32 个结果文件**中有 **32 个**（实际 11+11+10=32）。缺失 **13 个**（每个 ratio 缺 4-5 个）。

### 6. 问题根因与修复

平台重启后 conda 环境未自动激活，导致 `python` 命令不可用。需要在启动脚本中显式 source conda：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

或直接用 `/root/miniconda3/bin/python` 作为解释器重新启动缺失 seeds 的实验。

需要我现在修复环境并重启缺失 seeds 的实验吗？

---
